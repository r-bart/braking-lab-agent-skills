#!/usr/bin/env python3
"""Build a distinct, private staging test ZIP. Never submit it to public review."""
from copy import deepcopy
import argparse
from hashlib import sha256
import json
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

import build_archive

STAGING_MCP = 'https://mcp-staging.brakinglab.com/mcp'
STABLE_VERSION = r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)'

def build(installed_plugin: Path | None = None, version: str | None = None) -> Path:
    release_version = build_archive.VERSION if version is None else version
    if not re.fullmatch(STABLE_VERSION, release_version):
        raise ValueError('Staging version must be a strict stable semantic version')
    build_archive.verify_submission(build_archive.MANIFEST, build_archive.ROOT)
    manifest=deepcopy(build_archive.MANIFEST)
    manifest['name']='braking-lab-ray-paddock-staging'
    extension=manifest['extensions']['com.openai']
    extension.pop('publication', None)
    extension.pop('review', None)
    manifest['version'] = release_version
    connection_name = 'mcp.json'
    connection = {'mcpServers':{'braking-lab':{'type':'streamable-http','url':STAGING_MCP}}}
    flavor = 'staging'
    legacy_overlay = None
    if installed_plugin is not None:
        # Private binding is supplied locally; it never enters public source/artifacts.
        for name in ['plugin.json', '.app.json']:
            if (installed_plugin/name).is_symlink():
                raise ValueError('Symlink in private staging input')
        installed = json.loads((installed_plugin/'plugin.json').read_text())
        if installed.get('name') != manifest['name']:
            raise ValueError('Existing plugin is not the staging pilot')
        if installed.get('extensions', {}).get('com.openai', {}).get('apps') != './.app.json':
            raise ValueError('Existing staging connection is not an app mapping')
        manifest = deepcopy(installed)
        current_version = installed.get('version')
        if not isinstance(current_version, str) or not re.fullmatch(STABLE_VERSION, current_version):
            raise ValueError('Installed staging version must be a strict stable semantic version')
        if tuple(map(int, release_version.split('.'))) <= tuple(map(int, current_version.split('.'))):
            raise ValueError('Private update version must exceed the installed version')
        manifest['version'] = release_version
        extension = manifest['extensions']['com.openai']
        extension['onboardingSkill'] = './skills/race-engineer/SKILL.md'
        connection = json.loads((installed_plugin/'.app.json').read_text())
        apps = connection.get('apps', {})
        if set(connection) != {'apps'} or set(apps) != {'braking-lab'}:
            raise ValueError('Unexpected private staging mapping')
        app = apps['braking-lab']
        if set(app) != {'id', 'required'} or not isinstance(app['id'], str) or not app['id'].startswith('asdk_app_') or app['required'] is not True:
            raise ValueError('Invalid private staging mapping')
        connection_name = '.app.json'
        extension.pop('mcp', None)
        extension['apps'] = './.app.json'
        overlay_path = installed_plugin/'.codex-plugin/plugin.json'
        if overlay_path.exists():
            if overlay_path.is_symlink() or overlay_path.parent.is_symlink():
                raise ValueError('Symlink in private staging input')
            legacy_overlay = json.loads(overlay_path.read_text())
            if legacy_overlay.get('name') != manifest['name'] or legacy_overlay.get('apps') != './.app.json':
                raise ValueError('Unexpected staging legacy overlay')
            legacy_overlay['version'] = release_version
        flavor = 'staging-chatgpt'
    manifest['description'] = 'Ray, your Braking Lab race engineer: owned telemetry, race preparation, coaching, setups, strategy, track notes and training in staging.'
    interface = extension['interface']
    interface['displayName'] = 'Braking Lab - Race Engineer · Staging'
    interface['shortDescription'] = 'Your race engineer · staging'
    interface['longDescription'] = 'Ray is your Braking Lab race engineer. Review captured telemetry, compare laps and owned setup versions, prepare races, read coaching reports, work on strategy, keep track notes and turn braking evidence into practice. The UI shows your evidence; the conversation stays in ChatGPT. Uses your connected Braking Lab staging account. Available features follow your existing membership and data. Saves affect staging. Capture and physical pedal practice run separately in Braking Lab.'
    for key in ['logo', 'composerIcon']:
        interface[key] = build_archive.MANIFEST['extensions']['com.openai']['interface'][key]
    interface['supportURL'] = build_archive.MANIFEST['extensions']['com.openai']['interface']['supportURL']
    interface['websiteURL'] = build_archive.MANIFEST['extensions']['com.openai']['interface']['websiteURL']
    if legacy_overlay is not None:
        legacy_overlay['interface'] = deepcopy(interface)
        legacy_overlay['description'] = manifest['description']
    build_archive.OUTPUT_DIR.mkdir(exist_ok=True)
    output=build_archive.OUTPUT_DIR/f'braking-lab-{flavor}-{release_version}.zip'
    with ZipFile(output, 'w', compression=ZIP_DEFLATED) as archive:
        for path in build_archive.SKILL_FILES:
            build_archive.add_file(archive,path)
        for name in sorted({extension['interface'][key] for key in ['logo','composerIcon']}):
            build_archive.add_file(archive,build_archive.ROOT/name)
        generated = [('plugin.json',manifest),(connection_name,connection)]
        if legacy_overlay is not None: generated.append(('.codex-plugin/plugin.json', legacy_overlay))
        for name,value in generated:
            info=ZipInfo(name,(2000,1,1,0,0,0)); info.compress_type=ZIP_DEFLATED
            info.create_system=3; info.external_attr=0o100644 << 16
            archive.writestr(info,json.dumps(value,indent=2,ensure_ascii=False)+'\n')
    with ZipFile(output) as archive:
        names=archive.namelist()
        assert len(names)==len(set(names))
        assert sum(n in names for n in ['mcp.json', '.mcp.json', '.app.json']) == 1
        assert len([n for n in names if n.endswith('/SKILL.md')])==10
        if installed_plugin is None:
            assert json.loads(archive.read('mcp.json'))['mcpServers']['braking-lab']['url']==STAGING_MCP
        for name in names:
            if name.endswith('.json') and installed_plugin is None: build_archive.no_private_bindings(json.loads(archive.read(name)))
    (build_archive.OUTPUT_DIR/f'SHA256SUMS.{flavor}').write_text(f'{sha256(output.read_bytes()).hexdigest()}  {output.name}\n')
    print(f'Built PRIVATE staging candidate: {output}')
    return output

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--installed-plugin', type=Path, help='Local existing private staging plugin; preserve its connection without publishing the binding')
    parser.add_argument('--version', help='Greater stable semantic version for an existing private plugin update')
    args = parser.parse_args()
    build(args.installed_plugin, args.version)
