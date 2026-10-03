# Canonical Braking Lab icon

`icon.svg` is an unchanged copy of the v5 sticker isotype in the monorepo's
`apps/app/public/favicon.svg`, with viewBox `18 18 163 163`. Its geometry and
colors are shared with the SPA and landing; no alternate logo was designed.

The manifests reference `icon.png`, a transparent 512 Ã— 512 raster rendered
from that SVG with Sharp 0.34.5, density 192, resize 512 Ã— 512, PNG compression
level 9 and adaptive filtering disabled. Two consecutive renders produced
identical bytes. The provider archives include the referenced PNG.

- SVG SHA-256 (LF-normalized): `aeb6eac66694b3c349a392f09d3b98d13c13ca08ec8a5e9499fb2df348cbf7f1`
- PNG SHA-256: `8033f6144244ef53bb5ed68ed09014cbe56163bbee0a30540afd4b4353fbc5c9`

Updating the icon does not change the production MCP connection or any private
App binding. Private staging packages are built separately and are excluded
from this public source.
