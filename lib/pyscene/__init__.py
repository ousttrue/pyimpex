from .. import formats
from .facemesh import FaceMesh
from .submesh_mesh import SubmeshMesh, Submesh, Vertex
from .node import Node, Skin
from .material import UnlitMaterial, PBRMaterial, MToonMaterial, Texture, BlendMode, TextureUsage
from .from_gltf import nodes_from_gltf, load
from .modifier import before_import
from .vrm_loader import Vrm, VrmExpression, VrmExpressionPreset
from .index_map import IndexMap


def reload():
    print(f'reload {__file__}')
    from . import facemesh, submesh_mesh, node, material, from_gltf, modifier, vrm_loader
    import importlib
    for m in [
            facemesh, submesh_mesh, node, material, from_gltf, modifier,
            vrm_loader
    ]:
        importlib.reload(m)