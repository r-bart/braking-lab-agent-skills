"""Verify reproducible public artifacts and package boundary failures."""
from io import BytesIO
from copy import deepcopy
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from zipfile import ZipFile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_archive
import build_staging

class ArchiveTest(unittest.TestCase):
    def test_each_provider_is_reproducible_and_has_one_connection(self):
        with TemporaryDirectory() as temp, patch.object(build_archive, 'OUTPUT_DIR', Path(temp)):
            for flavor, connection in [('portable', 'mcp.json'), ('claude', '.mcp.json')]:
                with self.subTest(flavor=flavor):
                    output=build_archive.build(flavor)
                    before=output.read_bytes()
                    self.assertEqual(before, build_archive.build(flavor).read_bytes())
                    with ZipFile(BytesIO(before)) as archive:
                        names=archive.namelist()
                        self.assertIn(connection, names)
                        self.assertEqual(sum(n in names for n in ['mcp.json','.mcp.json']), 1)
                        self.assertEqual(sum(n.endswith('/SKILL.md') for n in names), 10)
                        self.assertNotIn('.app.json', names)
                        self.assertFalse(any(n.startswith(('docs/', 'tests/', 'hooks/')) for n in names))
    def test_staging_artifact_is_distinct_and_never_points_at_production(self):
        with TemporaryDirectory() as temp, patch.object(build_archive, 'OUTPUT_DIR', Path(temp)):
            output=build_staging.build()
            before=output.read_bytes()
            self.assertEqual(before, build_staging.build().read_bytes())
            import json
            with ZipFile(output) as archive:
                manifest=json.loads(archive.read('plugin.json'))
                self.assertEqual(manifest['name'], 'braking-lab-ray-paddock-staging')
                self.assertNotIn('publication',manifest['extensions']['com.openai'])
                self.assertNotIn('review',manifest['extensions']['com.openai'])
                self.assertEqual(json.loads(archive.read('mcp.json'))['mcpServers']['braking-lab']['url'], build_staging.STAGING_MCP)
            self.assertEqual(build_archive.MANIFEST['name'],'braking-lab-race-engineer')

    def test_symlinked_input_is_rejected_even_if_target_is_inside_root(self):
        with TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'real').write_text('fixture')
            (root/'linked').symlink_to(root/'real')
            with patch.object(build_archive,'ROOT',root), ZipFile(BytesIO(), 'w') as archive:
                with self.assertRaisesRegex(ValueError,'Symlink'):
                    build_archive.add_file(archive, root/'linked')

    def test_private_chatgpt_update_preserves_only_existing_staging_binding(self):
        import json
        with TemporaryDirectory() as temp, patch.object(build_archive, 'OUTPUT_DIR', Path(temp)/'out'):
            root=Path(temp)
            interface=deepcopy(build_archive.MANIFEST['extensions']['com.openai']['interface'])
            (root/'plugin.json').write_text(json.dumps({'name':'braking-lab-ray-paddock-staging','extensions':{'com.openai':{'apps':'./.app.json', 'interface':interface}}}))
            binding={'apps':{'braking-lab':{'id':'asdk_app_fixture_only', 'required':True}}}
            (root/'.app.json').write_text(json.dumps(binding))
            output=build_staging.build(root)
            before=output.read_bytes()
            self.assertEqual(before, build_staging.build(root).read_bytes())
            with ZipFile(output) as archive:
                self.assertEqual(json.loads(archive.read('.app.json')), binding)
                self.assertNotIn('mcp.json',archive.namelist())
                self.assertNotIn('.mcp.json',archive.namelist())
                self.assertEqual(json.loads(archive.read('plugin.json'))['version'],'1.0.0')
            with ZipFile(build_archive.build('portable')) as archive:
                self.assertNotIn('.app.json',archive.namelist())
                self.assertFalse(any(b'asdk_app_fixture_only' in archive.read(n) for n in archive.namelist()))
            (root/'plugin.json').write_text(json.dumps({'name':'production-plugin'}))
            with self.assertRaisesRegex(ValueError,'not the staging pilot'):
                build_staging.build(root)
    def test_external_input_is_rejected(self):
        with TemporaryDirectory() as temp, ZipFile(BytesIO(), 'w') as archive:
            with self.assertRaisesRegex(ValueError,'escapes'):
                build_archive.add_file(archive, Path(temp)/'outside')
    def test_unknown_provider_is_rejected_before_creating_an_archive(self):
        with self.assertRaisesRegex(ValueError,'Unknown package flavor'):
            build_archive.build('private-pilot')
