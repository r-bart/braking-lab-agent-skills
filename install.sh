#!/bin/sh
# Install the Braking Lab Race Engineer skills without npm.
set -eu

VERSION=1.0.0
REPO=r-bart/braking-lab-agent-skills
MCP_URL=https://mcp.brakinglab.com/mcp
SKILLS='calendar-events debrief lap-comparison race-engineer race-week setup-coaching setup-evaluation setup-library track-notes training'

agent=
scope=
selection=
archive=
skip_mcp=0
yes=0
temp_dir=

usage() {
  cat <<'EOF'
Braking Lab Race Engineer installer

Usage: sh install.sh [options]
  --agent codex|claude-code|cursor|generic
  --scope user|project
  --skills all|name[,name...]
  --no-mcp             Install skills only
  --yes                Use defaults without prompts
  --list               List available skills
  --help               Show this help

Run without options to choose an agent, scope, and skills interactively.
The installer never asks for a Braking Lab password or token.
EOF
}

die() { printf 'Error: %s\n' "$*" >&2; exit 1; }
cleanup() { if [ -n "$temp_dir" ]; then rm -rf "$temp_dir"; fi; }
trap cleanup EXIT HUP INT TERM

prompt() {
  [ -r /dev/tty ] || die 'Interactive input needs a terminal. Pass --agent, --scope, and --skills.'
  printf '%s' "$1" >&2
  IFS= read -r answer </dev/tty || die 'Could not read a choice.'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent|--scope|--skills|--archive)
      [ "$#" -ge 2 ] || die "Missing value for $1"
      case "$1" in
        --agent) agent=$2 ;;
        --scope) scope=$2 ;;
        --skills) selection=$2 ;;
        --archive) archive=$2 ;;
      esac
      shift 2 ;;
    --no-mcp) skip_mcp=1; shift ;;
    --yes) yes=1; shift ;;
    --list) printf '%s\n' $SKILLS; exit 0 ;;
    --help|-h) usage; exit 0 ;;
    *) die "Unknown option: $1" ;;
  esac
done

if [ -z "$agent" ]; then
  if [ "$yes" -eq 1 ]; then agent=codex; else
    printf 'Choose an agent: 1) Codex  2) Claude Code  3) Cursor  4) Other\n' >&2
    prompt 'Agent [1]: '
    case "$answer" in ''|1) agent=codex ;; 2) agent=claude-code ;; 3) agent=cursor ;; 4) agent=generic ;; *) die 'Invalid agent choice.' ;; esac
  fi
fi
case "$agent" in codex|claude-code|cursor|generic) ;; *) die "Unsupported agent: $agent" ;; esac

if [ -z "$scope" ]; then
  if [ "$yes" -eq 1 ]; then scope=user; else
    prompt 'Install globally for your user or in this project? [user/project, default user]: '
    scope=${answer:-user}
  fi
fi
case "$scope" in user|project) ;; *) die "Unsupported scope: $scope" ;; esac

if [ -z "$selection" ]; then
  if [ "$yes" -eq 1 ]; then selection=all; else
    printf 'Available skills:\n%s\n' "$SKILLS" >&2
    prompt 'Skills [all, or comma-separated names]: '
    selection=${answer:-all}
  fi
fi

if [ "$selection" = all ]; then
  selected=$SKILLS
else
  selected=$(printf '%s' "$selection" | tr ',' ' ')
  [ -n "$selected" ] || die 'Choose at least one skill.'
  seen=' '
  for skill in $selected; do
    case " $SKILLS " in *" $skill "*) ;; *) die "Unknown skill: $skill" ;; esac
    case "$seen" in *" $skill "*) die "Duplicate skill: $skill" ;; esac
    seen="$seen$skill "
  done
fi

case "$agent:$scope" in
  codex:user) base="$HOME/.codex/skills" ;;
  codex:project) base="$PWD/.agents/skills" ;;
  claude-code:user) base="$HOME/.claude/skills" ;;
  claude-code:project) base="$PWD/.claude/skills" ;;
  cursor:user) base="$HOME/.cursor/skills" ;;
  cursor:project) base="$PWD/.cursor/skills" ;;
  generic:user) base="$HOME/.agents/skills" ;;
  generic:project) base="$PWD/.agents/skills" ;;
esac

command -v unzip >/dev/null 2>&1 || die 'unzip is required.'
temp_dir=$(mktemp -d) || die 'Could not create a temporary directory.'

if [ -n "$archive" ]; then
  [ -f "$archive" ] || die "Archive not found: $archive"
  cp "$archive" "$temp_dir/package.zip"
else
  command -v curl >/dev/null 2>&1 || die 'curl is required.'
  release="https://github.com/$REPO/releases/download/v$VERSION"
  curl -fsSL --retry 2 "$release/braking-lab-portable-$VERSION.zip" -o "$temp_dir/package.zip" || die 'Could not download the release archive.'
  curl -fsSL --retry 2 "$release/SHA256SUMS" -o "$temp_dir/SHA256SUMS" || die 'Could not download release checksums.'
  expected=$(awk -v file="braking-lab-portable-$VERSION.zip" '$2 == file { print $1 }' "$temp_dir/SHA256SUMS")
  [ -n "$expected" ] || die 'The release checksum is missing.'
  if command -v shasum >/dev/null 2>&1; then
    actual=$(shasum -a 256 "$temp_dir/package.zip" | awk '{ print $1 }')
  elif command -v sha256sum >/dev/null 2>&1; then
    actual=$(sha256sum "$temp_dir/package.zip" | awk '{ print $1 }')
  else
    die 'shasum or sha256sum is required to verify the download.'
  fi
  [ "$expected" = "$actual" ] || die 'The release checksum does not match.'
fi

unzip -q "$temp_dir/package.zip" -d "$temp_dir/package" || die 'Could not unpack the release.'
for skill in $selected; do
  [ -f "$temp_dir/package/skills/$skill/SKILL.md" ] || die "Release is missing $skill."
done

mkdir -p "$base" || die "Cannot create $base"
backup="$base/.braking-lab-backup-$VERSION-$$"
for skill in $selected; do
  target="$base/$skill"
  if [ -e "$target" ] || [ -L "$target" ]; then
    [ -f "$target/.braking-lab-installed" ] || die "Existing $target was not installed by Braking Lab; leaving it untouched."
  fi
  stage="$base/.braking-lab-stage-$$-$skill"
  cp -R "$temp_dir/package/skills/$skill" "$stage" || die "Cannot stage $skill."
  printf 'source=%s\nversion=%s\n' "$REPO" "$VERSION" > "$stage/.braking-lab-installed"
  if [ -e "$target" ] || [ -L "$target" ]; then
    mkdir -p "$backup"
    mv "$target" "$backup/$skill"
  fi
  if ! mv "$stage" "$target"; then
    if [ -d "$backup/$skill" ]; then mv "$backup/$skill" "$target"; fi
    die "Cannot install $skill."
  fi
  printf 'Installed %s\n' "$skill"
done

if [ "$skip_mcp" -eq 0 ]; then
  case "$agent" in
    codex)
      if command -v codex >/dev/null 2>&1; then
        if codex mcp get braking-lab >/dev/null 2>&1; then
          printf 'Codex already has a braking-lab MCP entry; check that it points to %s.\n' "$MCP_URL"
        else
          codex mcp add braking-lab --url "$MCP_URL" || die 'Skills installed, but Codex MCP setup failed.'
        fi
        printf 'Connect your account with: codex mcp login braking-lab\n'
      else
        printf 'Codex CLI was not found. Add the HTTP MCP server %s in Codex settings.\n' "$MCP_URL"
      fi ;;
    claude-code)
      if command -v claude >/dev/null 2>&1; then
        if claude mcp get braking-lab >/dev/null 2>&1; then
          printf 'Claude already has a braking-lab MCP entry; check that it points to %s.\n' "$MCP_URL"
        else
          claude mcp add --transport http --scope user braking-lab "$MCP_URL" || die 'Skills installed, but Claude MCP setup failed.'
        fi
        printf 'Open Claude Code and run /mcp to connect your Braking Lab account.\n'
      else
        printf 'Claude CLI was not found. Add the HTTP MCP server %s in Claude Code.\n' "$MCP_URL"
      fi ;;
    cursor|generic)
      printf 'Add a Streamable HTTP MCP connection in your agent: %s\n' "$MCP_URL"
      printf 'The installer has not verified OAuth support in this client.\n' ;;
  esac
fi
printf 'Skills installed in %s\n' "$base"
printf 'Then ask your agent: What can my Braking Lab Race Engineer do?\n'
