import array
from typing import (Any, List, Dict, Optional, NamedTuple)
import bpy, mathutils
from scene_translator.formats.buffertypes import (Vector2, Vector3, BoneWeight,
                                                  IVector4, Vector4)
from .submesh_mesh import Submesh, SubmeshMesh


class FaceVertex(NamedTuple):
    position_index: int
    normal: Optional[Vector3]
    uv: Optional[Vector2]

    def __hash__(self):
        return hash(self.position_index)

    def __eq__(self, other: 'FaceVertex') -> bool:
        if other is None or not isinstance(other, FaceVertex):
            return False
        if self.position_index != other.position_index:
            return False
        if self.normal != other.normal:
            return False
        if self.uv != other.uv:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)


class Triangle(NamedTuple):
    material_index: int
    i0: int
    i1: int
    i2: int


class FaceMesh:
    def __init__(self, name: str, vertices: List[bpy.types.MeshVertex],
                 materials: List[bpy.types.Material],
                 vertex_groups: List[bpy.types.VertexGroup],
                 bone_names: List[str]) -> None:
        self.name = name
        self.positions: Any = (Vector3 * len(vertices))()
        self.normals: Any = (Vector3 * len(vertices))()
        for i, v in enumerate(vertices):
            self.positions[i] = Vector3.from_Vector(v.co)
            self.normals[i] = Vector3.from_Vector(v.normal)

        self.materials: List[bpy.types.Material] = materials

        # faces
        self.face_vertices: List[FaceVertex] = []
        self.face_vertex_index_map: Dict[FaceVertex, int] = {}
        self.triangles: List[Triangle] = []

        self.vertex_group_names = [g.name for g in vertex_groups]
        self.bone_names = bone_names
        self.bone_weights = (BoneWeight * len(vertices))()
        for i, v in enumerate(vertices):
            for ve in v.groups:
                vg_name = self.vertex_group_names[ve.group]
                if vg_name in self.bone_names:
                    self.bone_weights[i].push(ve.group, ve.weight)

        self.morph_map: Dict[str, Any] = {}

    def __str__(self) -> str:
        return f'<{self.name}: {len(self.face_vertex_index_map)}vertices>'

    def add_triangle(self, face: bpy.types.MeshLoopTriangle,
                     uv_texture_layer: Optional[bpy.types.MeshUVLoopLayer]):

        assert len(face.vertices) == 3
        i0 = self._get_or_add_face_vertex(
            face.vertices[0], uv_texture_layer.data[face.loops[0]].uv
            if uv_texture_layer else None,
            None if face.use_smooth else face.normal)

        i1 = self._get_or_add_face_vertex(
            face.vertices[1], uv_texture_layer.data[face.loops[1]].uv
            if uv_texture_layer else None,
            None if face.use_smooth else face.normal)

        i2 = self._get_or_add_face_vertex(
            face.vertices[2], uv_texture_layer.data[face.loops[2]].uv
            if uv_texture_layer else None,
            None if face.use_smooth else face.normal)

        self.triangles.append(Triangle(face.material_index, i0, i1, i2))

    def _get_or_add_face_vertex(self, vertex_index: int, uv: mathutils.Vector,
                                normal: Optional[mathutils.Vector]) -> int:
        # 同一頂点を考慮する
        face = FaceVertex(vertex_index,
                          Vector3.from_Vector(normal) if normal else None,
                          Vector2.from_faceUV(uv) if uv else None)
        index = self.face_vertex_index_map.get(face, None)
        if index != None:
            return index

        index = len(self.face_vertices)
        self.face_vertices.append(face)
        self.face_vertex_index_map[face] = index
        return index

    def add_morph(self, name: str, vertices: List[bpy.types.MeshVertex]):
        print('add_morph', name)
        assert (len(vertices) == len(self.positions))
        positions = (Vector3 * len(vertices))()
        for i, v in enumerate(vertices):
            delta = Vector3.from_Vector(v.co) - self.positions[i]
            positions[i] = delta
        self.morph_map[name] = positions

    def freeze(self, skin_bone_names: List[str]) -> SubmeshMesh:
        '''
        blenderの面毎にmaterialを持つ形式から、
        同じmaterialをsubmeshにまとめた形式に変換する
        '''

        # 三角形をsubmeshに分配する
        dst = SubmeshMesh(self.name)
        for triangle in self.triangles:
            submesh = dst.get_or_create_submesh(triangle.material_index, self.materials)
            submesh.indices += array.array(
                'I', (triangle.i0, triangle.i1, triangle.i2))

        keys = sorted(dst.submesh_map.keys())
        total_vertex_count = 0
        for key in keys:
            submesh = dst.submesh_map[key]
            total_vertex_count += len(submesh.indices)
        dst.vertex_count = total_vertex_count

        # attributes
        positions = (Vector3 * total_vertex_count)()
        normals = (Vector3 * total_vertex_count)()
        uvs = (Vector2 * total_vertex_count)() if any(
            f.uv for f in self.face_vertices) else None
        joints = (IVector4 * total_vertex_count)()
        weights = (Vector4 * total_vertex_count)()
        has_bone_weights = skin_bone_names and len(skin_bone_names) > 0
        if has_bone_weights:
            group_index_to_joint_index = {
                i: skin_bone_names.index(vertex_group)
                for i, vertex_group in enumerate(self.vertex_group_names)
                if vertex_group in skin_bone_names
            }

        morph_map = {}
        for k, morph in self.morph_map.items():
            morph_positions = (Vector3 * total_vertex_count)()
            morph_map[k] = morph_positions

        # each submesh
        i = 0
        for key in keys:
            submesh = dst.submesh_map[key]

            for index in submesh.indices:
                face = self.face_vertices[index]
                positions[i] = self.positions[face.position_index]
                if face.normal:
                    normals[i] = face.normal
                else:
                    normals[i] = self.normals[face.position_index]
                uvs[i] = face.uv

                if has_bone_weights:
                    bone_weight = self.bone_weights[face.position_index]
                    joints[i], weights[i] = bone_weight.to_joints_with_weights(
                        group_index_to_joint_index)

                for k, morph in self.morph_map.items():
                    morph_positions = morph_map[k]
                    morph_positions[i] = morph[face.position_index]
                i += 1

        # sort
        dst.submeshes = [dst.submesh_map[key] for key in keys]
        dst.positions = memoryview(positions)
        dst.normals = memoryview(normals)
        dst.texcoord = memoryview(uvs) if uvs else None
        dst.joints = memoryview(joints) if has_bone_weights else None
        dst.weights = memoryview(weights) if has_bone_weights else None
        dst.morph_map = {k: memoryview(v) for k, v in morph_map.items()}

        return dst