import unittest
import os
from typing import List
import pathlib
import bpy
HERE = pathlib.Path(__file__).absolute().parent
GLTF_SAMPLE_DIR = pathlib.Path(os.getenv('GLTF_SAMPLE_MODELS'))  # type: ignore
VRM_SAMPLE_DIR = pathlib.Path(os.getenv('VRM_SAMPLES'))  # type: ignore
from lib.struct_types import Float4
from lib import formats
from lib import pyscene
from lib import bpy_helper


class VrmTests(unittest.TestCase):
    def test_vivi(self):
        path = VRM_SAMPLE_DIR / 'vroid/Vivi.vrm'
        self.assertTrue(path.exists())

        data = formats.parse_gltf(path)
        roots = pyscene.nodes_from_gltf(data)
        self.assertEqual(len(roots), 5)

        # laod
        bpy_helper.load(bpy.context, roots, data.gltf.extensions.VRM)