from typing import Any, List, Optional, Dict, Sequence
import array
from ..struct_types import PlanarBuffer


class Material:
    '''
    unlit
    '''
    def __init__(self, name: str):
        self.name = name


class PBRMaterial(Material):
    '''
    PBR
    '''
    def __init__(self, name: str):
        super().__init__(name)


class Submesh:
    def __init__(self, offset: int, vertex_count: int,
                 material: Material) -> None:
        self.material = material
        self.offset = offset
        self.vertex_count = vertex_count


class SubmeshMesh:
    def __init__(self, name: str, vertex_count: int, has_bone_weight: bool):
        self.name = name
        self.attributes = PlanarBuffer.create(vertex_count, has_bone_weight)
        # morph
        self.morph_map: Dict[str, memoryview] = {}
        # indices
        self.indices = array.array('I')
        self.submeshes: List[Submesh] = []

    def __str__(self) -> str:
        return f'<SubmeshMesh: {self.attributes.get_vertex_count()}verts>'
