# this is generated by sukonbu
from typing import NamedTuple, List, Any, Optional, Dict
from enum import Enum

def is_enable(value):
    if isinstance(value, int):
        return True
    if value:
        return True
    return False


class vrmMeta(NamedTuple):
    # Title of VRM model
    title: Optional[str] = None
    # Version of VRM model
    version: Optional[str] = None
    # Author of VRM model
    author: Optional[str] = None
    # Contact Information of VRM model author
    contactInformation: Optional[str] = None
    # Reference of VRM model
    reference: Optional[str] = None
    # Thumbnail of VRM model
    texture: Optional[int] = None
    # A person who can perform with this avatar
    allowedUserName: Optional[str] = None
    # Permission to perform violent acts with this avatar
    violentUssageName: Optional[str] = None
    # Permission to perform sexual acts with this avatar
    sexualUssageName: Optional[str] = None
    # For commercial use
    commercialUssageName: Optional[str] = None
    # If there are any conditions not mentioned above, put the URL link of the license document here.
    otherPermissionUrl: Optional[str] = None
    # License type
    licenseName: Optional[str] = None
    # If �gOther�h is selected, put the URL link of the license document here.
    otherLicenseUrl: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.title): d["title"] = self.title # noqa
        if is_enable(self.version): d["version"] = self.version # noqa
        if is_enable(self.author): d["author"] = self.author # noqa
        if is_enable(self.contactInformation): d["contactInformation"] = self.contactInformation # noqa
        if is_enable(self.reference): d["reference"] = self.reference # noqa
        if is_enable(self.texture): d["texture"] = self.texture # noqa
        if is_enable(self.allowedUserName): d["allowedUserName"] = self.allowedUserName # noqa
        if is_enable(self.violentUssageName): d["violentUssageName"] = self.violentUssageName # noqa
        if is_enable(self.sexualUssageName): d["sexualUssageName"] = self.sexualUssageName # noqa
        if is_enable(self.commercialUssageName): d["commercialUssageName"] = self.commercialUssageName # noqa
        if is_enable(self.otherPermissionUrl): d["otherPermissionUrl"] = self.otherPermissionUrl # noqa
        if is_enable(self.licenseName): d["licenseName"] = self.licenseName # noqa
        if is_enable(self.otherLicenseUrl): d["otherLicenseUrl"] = self.otherLicenseUrl # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmMeta':
        dst = {}
        if "title" in src: dst["title"] = src["title"] # noqa copy
        if "version" in src: dst["version"] = src["version"] # noqa copy
        if "author" in src: dst["author"] = src["author"] # noqa copy
        if "contactInformation" in src: dst["contactInformation"] = src["contactInformation"] # noqa copy
        if "reference" in src: dst["reference"] = src["reference"] # noqa copy
        if "texture" in src: dst["texture"] = src["texture"] # noqa copy
        if "allowedUserName" in src: dst["allowedUserName"] = src["allowedUserName"] # noqa copy
        if "violentUssageName" in src: dst["violentUssageName"] = src["violentUssageName"] # noqa copy
        if "sexualUssageName" in src: dst["sexualUssageName"] = src["sexualUssageName"] # noqa copy
        if "commercialUssageName" in src: dst["commercialUssageName"] = src["commercialUssageName"] # noqa copy
        if "otherPermissionUrl" in src: dst["otherPermissionUrl"] = src["otherPermissionUrl"] # noqa copy
        if "licenseName" in src: dst["licenseName"] = src["licenseName"] # noqa copy
        if "otherLicenseUrl" in src: dst["otherLicenseUrl"] = src["otherLicenseUrl"] # noqa copy
        return vrmMeta(**dst)


class humanoidHumanBonesItemMin(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'humanoidHumanBonesItemMin':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return humanoidHumanBonesItemMin(**dst)


class humanoidHumanBonesItemMax(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'humanoidHumanBonesItemMax':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return humanoidHumanBonesItemMax(**dst)


class humanoidHumanBonesItemCenter(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'humanoidHumanBonesItemCenter':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return humanoidHumanBonesItemCenter(**dst)


class vrmHumanoidBone(NamedTuple):
    # Human bone name.
    bone: Optional[str] = None
    # Reference node index
    node: Optional[int] = None
    # Unity's HumanLimit.useDefaultValues
    useDefaultValues: Optional[bool] = None
    # Unity's HumanLimit.min
    min: Optional[humanoidHumanBonesItemMin] = None
    # Unity's HumanLimit.max
    max: Optional[humanoidHumanBonesItemMax] = None
    # Unity's HumanLimit.center
    center: Optional[humanoidHumanBonesItemCenter] = None
    # Unity's HumanLimit.axisLength
    axisLength: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.bone): d["bone"] = self.bone # noqa
        if is_enable(self.node): d["node"] = self.node # noqa
        if is_enable(self.useDefaultValues): d["useDefaultValues"] = self.useDefaultValues # noqa
        if is_enable(self.min): d["min"] = self.min.to_dict() # noqa
        if is_enable(self.max): d["max"] = self.max.to_dict() # noqa
        if is_enable(self.center): d["center"] = self.center.to_dict() # noqa
        if is_enable(self.axisLength): d["axisLength"] = self.axisLength # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmHumanoidBone':
        dst = {}
        if "bone" in src: dst["bone"] = src["bone"] # noqa copy
        if "node" in src: dst["node"] = src["node"] # noqa copy
        if "useDefaultValues" in src: dst["useDefaultValues"] = src["useDefaultValues"] # noqa copy
        if "min" in src: dst["min"] = humanoidHumanBonesItemMin.from_dict(src["min"]) # noqa
        if "max" in src: dst["max"] = humanoidHumanBonesItemMax.from_dict(src["max"]) # noqa
        if "center" in src: dst["center"] = humanoidHumanBonesItemCenter.from_dict(src["center"]) # noqa
        if "axisLength" in src: dst["axisLength"] = src["axisLength"] # noqa copy
        return vrmHumanoidBone(**dst)


class vrmHumanoid(NamedTuple):
    # 
    humanBones: Optional[List[vrmHumanoidBone]] = None
    # Unity's HumanDescription.armStretch
    armStretch: Optional[float] = None
    # Unity's HumanDescription.legStretch
    legStretch: Optional[float] = None
    # Unity's HumanDescription.upperArmTwist
    upperArmTwist: Optional[float] = None
    # Unity's HumanDescription.lowerArmTwist
    lowerArmTwist: Optional[float] = None
    # Unity's HumanDescription.upperLegTwist
    upperLegTwist: Optional[float] = None
    # Unity's HumanDescription.lowerLegTwist
    lowerLegTwist: Optional[float] = None
    # Unity's HumanDescription.feetSpacing
    feetSpacing: Optional[float] = None
    # Unity's HumanDescription.hasTranslationDoF
    hasTranslationDoF: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.humanBones: d["humanBones"] = [item.to_dict() for item in self.humanBones] # noqa
        if is_enable(self.armStretch): d["armStretch"] = self.armStretch # noqa
        if is_enable(self.legStretch): d["legStretch"] = self.legStretch # noqa
        if is_enable(self.upperArmTwist): d["upperArmTwist"] = self.upperArmTwist # noqa
        if is_enable(self.lowerArmTwist): d["lowerArmTwist"] = self.lowerArmTwist # noqa
        if is_enable(self.upperLegTwist): d["upperLegTwist"] = self.upperLegTwist # noqa
        if is_enable(self.lowerLegTwist): d["lowerLegTwist"] = self.lowerLegTwist # noqa
        if is_enable(self.feetSpacing): d["feetSpacing"] = self.feetSpacing # noqa
        if is_enable(self.hasTranslationDoF): d["hasTranslationDoF"] = self.hasTranslationDoF # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmHumanoid':
        dst = {}
        dst["humanBones"] = [vrmHumanoidBone.from_dict(item) for item in src["humanBones"]] if "humanBones" in src else [] # noqa
        if "armStretch" in src: dst["armStretch"] = src["armStretch"] # noqa copy
        if "legStretch" in src: dst["legStretch"] = src["legStretch"] # noqa copy
        if "upperArmTwist" in src: dst["upperArmTwist"] = src["upperArmTwist"] # noqa copy
        if "lowerArmTwist" in src: dst["lowerArmTwist"] = src["lowerArmTwist"] # noqa copy
        if "upperLegTwist" in src: dst["upperLegTwist"] = src["upperLegTwist"] # noqa copy
        if "lowerLegTwist" in src: dst["lowerLegTwist"] = src["lowerLegTwist"] # noqa copy
        if "feetSpacing" in src: dst["feetSpacing"] = src["feetSpacing"] # noqa copy
        if "hasTranslationDoF" in src: dst["hasTranslationDoF"] = src["hasTranslationDoF"] # noqa copy
        return vrmHumanoid(**dst)


class firstPersonFirstPersonBoneOffset(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'firstPersonFirstPersonBoneOffset':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return firstPersonFirstPersonBoneOffset(**dst)


class vrmFirstpersonMeshannotation(NamedTuple):
    # 
    mesh: Optional[int] = None
    # 
    firstPersonFlag: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.mesh): d["mesh"] = self.mesh # noqa
        if is_enable(self.firstPersonFlag): d["firstPersonFlag"] = self.firstPersonFlag # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmFirstpersonMeshannotation':
        dst = {}
        if "mesh" in src: dst["mesh"] = src["mesh"] # noqa copy
        if "firstPersonFlag" in src: dst["firstPersonFlag"] = src["firstPersonFlag"] # noqa copy
        return vrmFirstpersonMeshannotation(**dst)


class vrmFirstpersonDegreemap(NamedTuple):
    # None linear mapping params. time, value, inTangent, outTangent
    curve: Optional[List[float]] = None
    # Look at input clamp range degree.
    xRange: Optional[float] = None
    # Look at map range degree from xRange.
    yRange: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.curve: d["curve"] = self.curve # noqa
        if is_enable(self.xRange): d["xRange"] = self.xRange # noqa
        if is_enable(self.yRange): d["yRange"] = self.yRange # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmFirstpersonDegreemap':
        dst = {}
        dst["curve"] = src.get("curve", [])
        if "xRange" in src: dst["xRange"] = src["xRange"] # noqa copy
        if "yRange" in src: dst["yRange"] = src["yRange"] # noqa copy
        return vrmFirstpersonDegreemap(**dst)


class vrmFirstperson(NamedTuple):
    # The bone whose rendering should be turned off in first-person view. Usually Head is specified.
    firstPersonBone: Optional[int] = None
    # The target position of the VR headset in first-person view. It is assumed that an offset from the head bone to the VR headset is added.
    firstPersonBoneOffset: Optional[firstPersonFirstPersonBoneOffset] = None
    # Switch display / undisplay for each mesh in first-person view or the others.
    meshAnnotations: Optional[List[vrmFirstpersonMeshannotation]] = None
    # Eye controller mode.
    lookAtTypeName: Optional[str] = None
    # Eye controller setting.
    lookAtHorizontalInner: Optional[vrmFirstpersonDegreemap] = None
    # Eye controller setting.
    lookAtHorizontalOuter: Optional[vrmFirstpersonDegreemap] = None
    # Eye controller setting.
    lookAtVerticalDown: Optional[vrmFirstpersonDegreemap] = None
    # Eye controller setting.
    lookAtVerticalUp: Optional[vrmFirstpersonDegreemap] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.firstPersonBone): d["firstPersonBone"] = self.firstPersonBone # noqa
        if is_enable(self.firstPersonBoneOffset): d["firstPersonBoneOffset"] = self.firstPersonBoneOffset.to_dict() # noqa
        if self.meshAnnotations: d["meshAnnotations"] = [item.to_dict() for item in self.meshAnnotations] # noqa
        if is_enable(self.lookAtTypeName): d["lookAtTypeName"] = self.lookAtTypeName # noqa
        if is_enable(self.lookAtHorizontalInner): d["lookAtHorizontalInner"] = self.lookAtHorizontalInner.to_dict() # noqa
        if is_enable(self.lookAtHorizontalOuter): d["lookAtHorizontalOuter"] = self.lookAtHorizontalOuter.to_dict() # noqa
        if is_enable(self.lookAtVerticalDown): d["lookAtVerticalDown"] = self.lookAtVerticalDown.to_dict() # noqa
        if is_enable(self.lookAtVerticalUp): d["lookAtVerticalUp"] = self.lookAtVerticalUp.to_dict() # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmFirstperson':
        dst = {}
        if "firstPersonBone" in src: dst["firstPersonBone"] = src["firstPersonBone"] # noqa copy
        if "firstPersonBoneOffset" in src: dst["firstPersonBoneOffset"] = firstPersonFirstPersonBoneOffset.from_dict(src["firstPersonBoneOffset"]) # noqa
        dst["meshAnnotations"] = [vrmFirstpersonMeshannotation.from_dict(item) for item in src["meshAnnotations"]] if "meshAnnotations" in src else [] # noqa
        if "lookAtTypeName" in src: dst["lookAtTypeName"] = src["lookAtTypeName"] # noqa copy
        if "lookAtHorizontalInner" in src: dst["lookAtHorizontalInner"] = vrmFirstpersonDegreemap.from_dict(src["lookAtHorizontalInner"]) # noqa
        if "lookAtHorizontalOuter" in src: dst["lookAtHorizontalOuter"] = vrmFirstpersonDegreemap.from_dict(src["lookAtHorizontalOuter"]) # noqa
        if "lookAtVerticalDown" in src: dst["lookAtVerticalDown"] = vrmFirstpersonDegreemap.from_dict(src["lookAtVerticalDown"]) # noqa
        if "lookAtVerticalUp" in src: dst["lookAtVerticalUp"] = vrmFirstpersonDegreemap.from_dict(src["lookAtVerticalUp"]) # noqa
        return vrmFirstperson(**dst)


class vrmBlendshapeBind(NamedTuple):
    # 
    mesh: Optional[int] = None
    # 
    index: Optional[int] = None
    # SkinnedMeshRenderer.SetBlendShapeWeight
    weight: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.mesh): d["mesh"] = self.mesh # noqa
        if is_enable(self.index): d["index"] = self.index # noqa
        if is_enable(self.weight): d["weight"] = self.weight # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmBlendshapeBind':
        dst = {}
        if "mesh" in src: dst["mesh"] = src["mesh"] # noqa copy
        if "index" in src: dst["index"] = src["index"] # noqa copy
        if "weight" in src: dst["weight"] = src["weight"] # noqa copy
        return vrmBlendshapeBind(**dst)


class vrmBlendshapeMaterialbind(NamedTuple):
    # 
    materialName: Optional[str] = None
    # 
    propertyName: Optional[str] = None
    # 
    targetValue: Optional[List[float]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.materialName): d["materialName"] = self.materialName # noqa
        if is_enable(self.propertyName): d["propertyName"] = self.propertyName # noqa
        if self.targetValue: d["targetValue"] = self.targetValue # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmBlendshapeMaterialbind':
        dst = {}
        if "materialName" in src: dst["materialName"] = src["materialName"] # noqa copy
        if "propertyName" in src: dst["propertyName"] = src["propertyName"] # noqa copy
        dst["targetValue"] = src.get("targetValue", [])
        return vrmBlendshapeMaterialbind(**dst)


class vrmBlendshapeGroup(NamedTuple):
    # Expression name
    name: Optional[str] = None
    # Predefined Expression name
    presetName: Optional[str] = None
    # Low level blendshape references.
    binds: Optional[List[vrmBlendshapeBind]] = None
    # Material animation references.
    materialValues: Optional[List[vrmBlendshapeMaterialbind]] = None
    # 0 or 1. Do not allow an intermediate value. Value should rounded
    isBinary: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.name): d["name"] = self.name # noqa
        if is_enable(self.presetName): d["presetName"] = self.presetName # noqa
        if self.binds: d["binds"] = [item.to_dict() for item in self.binds] # noqa
        if self.materialValues: d["materialValues"] = [item.to_dict() for item in self.materialValues] # noqa
        if is_enable(self.isBinary): d["isBinary"] = self.isBinary # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmBlendshapeGroup':
        dst = {}
        if "name" in src: dst["name"] = src["name"] # noqa copy
        if "presetName" in src: dst["presetName"] = src["presetName"] # noqa copy
        dst["binds"] = [vrmBlendshapeBind.from_dict(item) for item in src["binds"]] if "binds" in src else [] # noqa
        dst["materialValues"] = [vrmBlendshapeMaterialbind.from_dict(item) for item in src["materialValues"]] if "materialValues" in src else [] # noqa
        if "isBinary" in src: dst["isBinary"] = src["isBinary"] # noqa copy
        return vrmBlendshapeGroup(**dst)


class vrmBlendshape(NamedTuple):
    # 
    blendShapeGroups: Optional[List[vrmBlendshapeGroup]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.blendShapeGroups: d["blendShapeGroups"] = [item.to_dict() for item in self.blendShapeGroups] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmBlendshape':
        dst = {}
        dst["blendShapeGroups"] = [vrmBlendshapeGroup.from_dict(item) for item in src["blendShapeGroups"]] if "blendShapeGroups" in src else [] # noqa
        return vrmBlendshape(**dst)


class secondaryAnimationBoneGroupsItemGravityDir(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'secondaryAnimationBoneGroupsItemGravityDir':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return secondaryAnimationBoneGroupsItemGravityDir(**dst)


class vrmSecondaryanimationSpring(NamedTuple):
    # Annotation comment
    comment: Optional[str] = None
    # The resilience of the swaying object (the power of returning to the initial pose).
    stiffiness: Optional[float] = None
    # The strength of gravity.
    gravityPower: Optional[float] = None
    # The direction of gravity. Set (0, -1, 0) for simulating the gravity. Set (1, 0, 0) for simulating the wind.
    gravityDir: Optional[secondaryAnimationBoneGroupsItemGravityDir] = None
    # The resistance (deceleration) of automatic animation.
    dragForce: Optional[float] = None
    # The reference point of a swaying object can be set at any location except the origin. When implementing UI moving with warp, the parent node to move with warp can be specified if you don't want to make the object swaying with warp movement.
    center: Optional[int] = None
    # The radius of the sphere used for the collision detection with colliders.
    hitRadius: Optional[float] = None
    # Specify the node index of the root bone of the swaying object.
    bones: Optional[List[int]] = None
    # Specify the index of the collider group for collisions with swaying objects.
    colliderGroups: Optional[List[int]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.comment): d["comment"] = self.comment # noqa
        if is_enable(self.stiffiness): d["stiffiness"] = self.stiffiness # noqa
        if is_enable(self.gravityPower): d["gravityPower"] = self.gravityPower # noqa
        if is_enable(self.gravityDir): d["gravityDir"] = self.gravityDir.to_dict() # noqa
        if is_enable(self.dragForce): d["dragForce"] = self.dragForce # noqa
        if is_enable(self.center): d["center"] = self.center # noqa
        if is_enable(self.hitRadius): d["hitRadius"] = self.hitRadius # noqa
        if self.bones: d["bones"] = self.bones # noqa
        if self.colliderGroups: d["colliderGroups"] = self.colliderGroups # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmSecondaryanimationSpring':
        dst = {}
        if "comment" in src: dst["comment"] = src["comment"] # noqa copy
        if "stiffiness" in src: dst["stiffiness"] = src["stiffiness"] # noqa copy
        if "gravityPower" in src: dst["gravityPower"] = src["gravityPower"] # noqa copy
        if "gravityDir" in src: dst["gravityDir"] = secondaryAnimationBoneGroupsItemGravityDir.from_dict(src["gravityDir"]) # noqa
        if "dragForce" in src: dst["dragForce"] = src["dragForce"] # noqa copy
        if "center" in src: dst["center"] = src["center"] # noqa copy
        if "hitRadius" in src: dst["hitRadius"] = src["hitRadius"] # noqa copy
        dst["bones"] = src.get("bones", [])
        dst["colliderGroups"] = src.get("colliderGroups", [])
        return vrmSecondaryanimationSpring(**dst)


class secondaryAnimationColliderGroupsItemCollidersItemOffset(NamedTuple):
    # 
    x: Optional[float] = None
    # 
    y: Optional[float] = None
    # 
    z: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.x): d["x"] = self.x # noqa
        if is_enable(self.y): d["y"] = self.y # noqa
        if is_enable(self.z): d["z"] = self.z # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'secondaryAnimationColliderGroupsItemCollidersItemOffset':
        dst = {}
        if "x" in src: dst["x"] = src["x"] # noqa copy
        if "y" in src: dst["y"] = src["y"] # noqa copy
        if "z" in src: dst["z"] = src["z"] # noqa copy
        return secondaryAnimationColliderGroupsItemCollidersItemOffset(**dst)


class secondaryAnimationColliderGroupsItemCollidersItem(NamedTuple):
    # The local coordinate from the node of the collider group in *left-handed* Y-up coordinate.
    offset: Optional[secondaryAnimationColliderGroupsItemCollidersItemOffset] = None
    # The radius of the collider.
    radius: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.offset): d["offset"] = self.offset.to_dict() # noqa
        if is_enable(self.radius): d["radius"] = self.radius # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'secondaryAnimationColliderGroupsItemCollidersItem':
        dst = {}
        if "offset" in src: dst["offset"] = secondaryAnimationColliderGroupsItemCollidersItemOffset.from_dict(src["offset"]) # noqa
        if "radius" in src: dst["radius"] = src["radius"] # noqa copy
        return secondaryAnimationColliderGroupsItemCollidersItem(**dst)


class vrmSecondaryanimationCollidergroup(NamedTuple):
    # The node of the collider group for setting up collision detections.
    node: Optional[int] = None
    # 
    colliders: Optional[List[secondaryAnimationColliderGroupsItemCollidersItem]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.node): d["node"] = self.node # noqa
        if self.colliders: d["colliders"] = [item.to_dict() for item in self.colliders] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmSecondaryanimationCollidergroup':
        dst = {}
        if "node" in src: dst["node"] = src["node"] # noqa copy
        dst["colliders"] = [secondaryAnimationColliderGroupsItemCollidersItem.from_dict(item) for item in src["colliders"]] if "colliders" in src else [] # noqa
        return vrmSecondaryanimationCollidergroup(**dst)


class vrmSecondaryanimation(NamedTuple):
    # 
    boneGroups: Optional[List[vrmSecondaryanimationSpring]] = None
    # 
    colliderGroups: Optional[List[vrmSecondaryanimationCollidergroup]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.boneGroups: d["boneGroups"] = [item.to_dict() for item in self.boneGroups] # noqa
        if self.colliderGroups: d["colliderGroups"] = [item.to_dict() for item in self.colliderGroups] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmSecondaryanimation':
        dst = {}
        dst["boneGroups"] = [vrmSecondaryanimationSpring.from_dict(item) for item in src["boneGroups"]] if "boneGroups" in src else [] # noqa
        dst["colliderGroups"] = [vrmSecondaryanimationCollidergroup.from_dict(item) for item in src["colliderGroups"]] if "colliderGroups" in src else [] # noqa
        return vrmSecondaryanimation(**dst)


class vrmMaterial(NamedTuple):
    # 
    name: Optional[str] = None
    # This contains shader name.  VRM/MToon, VRM/UnlitTransparentZWrite, and VRM_USE_GLTFSHADER (and legacy materials as Standard, UniGLTF/UniUnlit, VRM/UnlitTexture, VRM/UnlitCutout, VRM/UnlitTransparent) . If VRM_USE_GLTFSHADER is specified, use same index of gltf's material settings
    shader: Optional[str] = None
    # 
    renderQueue: Optional[int] = None
    # 
    floatProperties: Optional[Dict[str, float]] = None
    # 
    vectorProperties: Optional[Dict[str, List[float]]] = None
    # 
    textureProperties: Optional[Dict[str, int]] = None
    # 
    keywordMap: Optional[Dict[str, bool]] = None
    # 
    tagMap: Optional[Dict[str, str]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.name): d["name"] = self.name # noqa
        if is_enable(self.shader): d["shader"] = self.shader # noqa
        if is_enable(self.renderQueue): d["renderQueue"] = self.renderQueue # noqa
        if is_enable(self.floatProperties): d["floatProperties"] = self.floatProperties # noqa
        if is_enable(self.vectorProperties): d["vectorProperties"] = self.vectorProperties # noqa
        if is_enable(self.textureProperties): d["textureProperties"] = self.textureProperties # noqa
        if is_enable(self.keywordMap): d["keywordMap"] = self.keywordMap # noqa
        if is_enable(self.tagMap): d["tagMap"] = self.tagMap # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrmMaterial':
        dst = {}
        if "name" in src: dst["name"] = src["name"] # noqa copy
        if "shader" in src: dst["shader"] = src["shader"] # noqa copy
        if "renderQueue" in src: dst["renderQueue"] = src["renderQueue"] # noqa copy
        dst["floatProperties"] = src.get("floatProperties", {})
        dst["vectorProperties"] = src.get("vectorProperties", {})
        dst["textureProperties"] = src.get("textureProperties", {})
        dst["keywordMap"] = src.get("keywordMap", {})
        dst["tagMap"] = src.get("tagMap", {})
        return vrmMaterial(**dst)


class vrm(NamedTuple):
    # Version of exporter that vrm created. UniVRM-0.46
    exporterVersion: Optional[str] = None
    # Version of VRM specification. 0.0
    specVersion: Optional[str] = None
    # 
    meta: Optional[vrmMeta] = None
    # 
    humanoid: Optional[vrmHumanoid] = None
    # 
    firstPerson: Optional[vrmFirstperson] = None
    # BlendShapeAvatar of UniVRM
    blendShapeMaster: Optional[vrmBlendshape] = None
    # The setting of automatic animation of string-like objects such as tails and hairs.
    secondaryAnimation: Optional[vrmSecondaryanimation] = None
    # 
    materialProperties: Optional[List[vrmMaterial]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.exporterVersion): d["exporterVersion"] = self.exporterVersion # noqa
        if is_enable(self.specVersion): d["specVersion"] = self.specVersion # noqa
        if is_enable(self.meta): d["meta"] = self.meta.to_dict() # noqa
        if is_enable(self.humanoid): d["humanoid"] = self.humanoid.to_dict() # noqa
        if is_enable(self.firstPerson): d["firstPerson"] = self.firstPerson.to_dict() # noqa
        if is_enable(self.blendShapeMaster): d["blendShapeMaster"] = self.blendShapeMaster.to_dict() # noqa
        if is_enable(self.secondaryAnimation): d["secondaryAnimation"] = self.secondaryAnimation.to_dict() # noqa
        if self.materialProperties: d["materialProperties"] = [item.to_dict() for item in self.materialProperties] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'vrm':
        dst = {}
        if "exporterVersion" in src: dst["exporterVersion"] = src["exporterVersion"] # noqa copy
        if "specVersion" in src: dst["specVersion"] = src["specVersion"] # noqa copy
        if "meta" in src: dst["meta"] = vrmMeta.from_dict(src["meta"]) # noqa
        if "humanoid" in src: dst["humanoid"] = vrmHumanoid.from_dict(src["humanoid"]) # noqa
        if "firstPerson" in src: dst["firstPerson"] = vrmFirstperson.from_dict(src["firstPerson"]) # noqa
        if "blendShapeMaster" in src: dst["blendShapeMaster"] = vrmBlendshape.from_dict(src["blendShapeMaster"]) # noqa
        if "secondaryAnimation" in src: dst["secondaryAnimation"] = vrmSecondaryanimation.from_dict(src["secondaryAnimation"]) # noqa
        dst["materialProperties"] = [vrmMaterial.from_dict(item) for item in src["materialProperties"]] if "materialProperties" in src else [] # noqa
        return vrm(**dst)


if __name__ == '__main__':
    pass
