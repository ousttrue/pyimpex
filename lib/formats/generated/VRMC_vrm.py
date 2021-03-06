# this is generated by sukonbu
from typing import NamedTuple, List, Any, Optional, Dict
from enum import Enum

def is_enable(value):
    if isinstance(value, int):
        return True
    if value:
        return True
    return False


class Meta(NamedTuple):
    # The name of the model
    name: str
    # Authors of the model
    authors: List[str]
    # The version of the model
    version: Optional[str] = None
    # An information that describes the copyright of the model
    copyrightInformation: Optional[str] = None
    # An information that describes the contact information of the author
    contactInformation: Optional[str] = None
    # References / original works of the model
    references: Optional[List[str]] = None
    # Third party licenses of the model, if required. You can use line breaks
    thirdPartyLicenses: Optional[str] = None
    # The index to access the thumbnail image of the avatar model in gltf.images. The texture resolution of 1024x1024 is recommended. It must be square. Preferable resolution is 1024 x 1024. This is for the application to use as an icon.
    thumbnailImage: Optional[int] = None
    # A person who can perform with this avatars
    avatarPermission: Optional[str] = None
    # A flag that permits to use this avatar in excessively violent contents
    allowExcessivelyViolentUsage: Optional[bool] = None
    # A flag that permits to use this avatar in excessively sexual contents
    allowExcessivelySexualUsage: Optional[bool] = None
    # An option that permits to use this avatar in commercial products
    commercialUsage: Optional[str] = None
    # A flag that permits to use this avatar in political or religious contents
    allowPoliticalOrReligiousUsage: Optional[bool] = None
    # An option that forces or abandons to display the credit of this avatar
    creditNotation: Optional[str] = None
    # A flag that permits to redistribute this avatar
    allowRedistribution: Optional[bool] = None
    # An option that controls the condition to modify this avatar
    modification: Optional[str] = None
    # Describe the URL links of other license
    otherLicenseUrl: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.name): d["name"] = self.name # noqa
        if is_enable(self.version): d["version"] = self.version # noqa
        if self.authors: d["authors"] = self.authors # noqa
        if is_enable(self.copyrightInformation): d["copyrightInformation"] = self.copyrightInformation # noqa
        if is_enable(self.contactInformation): d["contactInformation"] = self.contactInformation # noqa
        if self.references: d["references"] = self.references # noqa
        if is_enable(self.thirdPartyLicenses): d["thirdPartyLicenses"] = self.thirdPartyLicenses # noqa
        if is_enable(self.thumbnailImage): d["thumbnailImage"] = self.thumbnailImage # noqa
        if is_enable(self.avatarPermission): d["avatarPermission"] = self.avatarPermission # noqa
        if is_enable(self.allowExcessivelyViolentUsage): d["allowExcessivelyViolentUsage"] = self.allowExcessivelyViolentUsage # noqa
        if is_enable(self.allowExcessivelySexualUsage): d["allowExcessivelySexualUsage"] = self.allowExcessivelySexualUsage # noqa
        if is_enable(self.commercialUsage): d["commercialUsage"] = self.commercialUsage # noqa
        if is_enable(self.allowPoliticalOrReligiousUsage): d["allowPoliticalOrReligiousUsage"] = self.allowPoliticalOrReligiousUsage # noqa
        if is_enable(self.creditNotation): d["creditNotation"] = self.creditNotation # noqa
        if is_enable(self.allowRedistribution): d["allowRedistribution"] = self.allowRedistribution # noqa
        if is_enable(self.modification): d["modification"] = self.modification # noqa
        if is_enable(self.otherLicenseUrl): d["otherLicenseUrl"] = self.otherLicenseUrl # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'Meta':
        dst = {}
        if "name" in src: dst["name"] = src["name"] # noqa copy
        if "version" in src: dst["version"] = src["version"] # noqa copy
        dst["authors"] = src.get("authors", [])
        if "copyrightInformation" in src: dst["copyrightInformation"] = src["copyrightInformation"] # noqa copy
        if "contactInformation" in src: dst["contactInformation"] = src["contactInformation"] # noqa copy
        dst["references"] = src.get("references", [])
        if "thirdPartyLicenses" in src: dst["thirdPartyLicenses"] = src["thirdPartyLicenses"] # noqa copy
        if "thumbnailImage" in src: dst["thumbnailImage"] = src["thumbnailImage"] # noqa copy
        if "avatarPermission" in src: dst["avatarPermission"] = src["avatarPermission"] # noqa copy
        if "allowExcessivelyViolentUsage" in src: dst["allowExcessivelyViolentUsage"] = src["allowExcessivelyViolentUsage"] # noqa copy
        if "allowExcessivelySexualUsage" in src: dst["allowExcessivelySexualUsage"] = src["allowExcessivelySexualUsage"] # noqa copy
        if "commercialUsage" in src: dst["commercialUsage"] = src["commercialUsage"] # noqa copy
        if "allowPoliticalOrReligiousUsage" in src: dst["allowPoliticalOrReligiousUsage"] = src["allowPoliticalOrReligiousUsage"] # noqa copy
        if "creditNotation" in src: dst["creditNotation"] = src["creditNotation"] # noqa copy
        if "allowRedistribution" in src: dst["allowRedistribution"] = src["allowRedistribution"] # noqa copy
        if "modification" in src: dst["modification"] = src["modification"] # noqa copy
        if "otherLicenseUrl" in src: dst["otherLicenseUrl"] = src["otherLicenseUrl"] # noqa copy
        return Meta(**dst)


class HumanBone(NamedTuple):
    # Represents a single glTF node tied to this humanBone.
    node: int

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.node): d["node"] = self.node # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'HumanBone':
        dst = {}
        if "node" in src: dst["node"] = src["node"] # noqa copy
        return HumanBone(**dst)


class HumanBones(NamedTuple):
    # Represents a single bone of a Humanoid.
    hips: HumanBone
    # Represents a single bone of a Humanoid.
    spine: HumanBone
    # Represents a single bone of a Humanoid.
    head: HumanBone
    # Represents a single bone of a Humanoid.
    leftUpperLeg: HumanBone
    # Represents a single bone of a Humanoid.
    leftLowerLeg: HumanBone
    # Represents a single bone of a Humanoid.
    leftFoot: HumanBone
    # Represents a single bone of a Humanoid.
    rightUpperLeg: HumanBone
    # Represents a single bone of a Humanoid.
    rightLowerLeg: HumanBone
    # Represents a single bone of a Humanoid.
    rightFoot: HumanBone
    # Represents a single bone of a Humanoid.
    leftUpperArm: HumanBone
    # Represents a single bone of a Humanoid.
    leftLowerArm: HumanBone
    # Represents a single bone of a Humanoid.
    leftHand: HumanBone
    # Represents a single bone of a Humanoid.
    rightUpperArm: HumanBone
    # Represents a single bone of a Humanoid.
    rightLowerArm: HumanBone
    # Represents a single bone of a Humanoid.
    rightHand: HumanBone
    # Represents a single bone of a Humanoid.
    chest: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    upperChest: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    neck: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftEye: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightEye: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    jaw: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftToes: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightToes: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftShoulder: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightShoulder: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftThumbProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftThumbIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftThumbDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftIndexProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftIndexIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftIndexDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftMiddleProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftMiddleIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftMiddleDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftRingProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftRingIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftRingDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftLittleProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftLittleIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    leftLittleDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightThumbProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightThumbIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightThumbDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightIndexProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightIndexIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightIndexDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightMiddleProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightMiddleIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightMiddleDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightRingProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightRingIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightRingDistal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightLittleProximal: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightLittleIntermediate: Optional[HumanBone] = None
    # Represents a single bone of a Humanoid.
    rightLittleDistal: Optional[HumanBone] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.hips): d["hips"] = self.hips.to_dict() # noqa
        if is_enable(self.spine): d["spine"] = self.spine.to_dict() # noqa
        if is_enable(self.chest): d["chest"] = self.chest.to_dict() # noqa
        if is_enable(self.upperChest): d["upperChest"] = self.upperChest.to_dict() # noqa
        if is_enable(self.neck): d["neck"] = self.neck.to_dict() # noqa
        if is_enable(self.head): d["head"] = self.head.to_dict() # noqa
        if is_enable(self.leftEye): d["leftEye"] = self.leftEye.to_dict() # noqa
        if is_enable(self.rightEye): d["rightEye"] = self.rightEye.to_dict() # noqa
        if is_enable(self.jaw): d["jaw"] = self.jaw.to_dict() # noqa
        if is_enable(self.leftUpperLeg): d["leftUpperLeg"] = self.leftUpperLeg.to_dict() # noqa
        if is_enable(self.leftLowerLeg): d["leftLowerLeg"] = self.leftLowerLeg.to_dict() # noqa
        if is_enable(self.leftFoot): d["leftFoot"] = self.leftFoot.to_dict() # noqa
        if is_enable(self.leftToes): d["leftToes"] = self.leftToes.to_dict() # noqa
        if is_enable(self.rightUpperLeg): d["rightUpperLeg"] = self.rightUpperLeg.to_dict() # noqa
        if is_enable(self.rightLowerLeg): d["rightLowerLeg"] = self.rightLowerLeg.to_dict() # noqa
        if is_enable(self.rightFoot): d["rightFoot"] = self.rightFoot.to_dict() # noqa
        if is_enable(self.rightToes): d["rightToes"] = self.rightToes.to_dict() # noqa
        if is_enable(self.leftShoulder): d["leftShoulder"] = self.leftShoulder.to_dict() # noqa
        if is_enable(self.leftUpperArm): d["leftUpperArm"] = self.leftUpperArm.to_dict() # noqa
        if is_enable(self.leftLowerArm): d["leftLowerArm"] = self.leftLowerArm.to_dict() # noqa
        if is_enable(self.leftHand): d["leftHand"] = self.leftHand.to_dict() # noqa
        if is_enable(self.rightShoulder): d["rightShoulder"] = self.rightShoulder.to_dict() # noqa
        if is_enable(self.rightUpperArm): d["rightUpperArm"] = self.rightUpperArm.to_dict() # noqa
        if is_enable(self.rightLowerArm): d["rightLowerArm"] = self.rightLowerArm.to_dict() # noqa
        if is_enable(self.rightHand): d["rightHand"] = self.rightHand.to_dict() # noqa
        if is_enable(self.leftThumbProximal): d["leftThumbProximal"] = self.leftThumbProximal.to_dict() # noqa
        if is_enable(self.leftThumbIntermediate): d["leftThumbIntermediate"] = self.leftThumbIntermediate.to_dict() # noqa
        if is_enable(self.leftThumbDistal): d["leftThumbDistal"] = self.leftThumbDistal.to_dict() # noqa
        if is_enable(self.leftIndexProximal): d["leftIndexProximal"] = self.leftIndexProximal.to_dict() # noqa
        if is_enable(self.leftIndexIntermediate): d["leftIndexIntermediate"] = self.leftIndexIntermediate.to_dict() # noqa
        if is_enable(self.leftIndexDistal): d["leftIndexDistal"] = self.leftIndexDistal.to_dict() # noqa
        if is_enable(self.leftMiddleProximal): d["leftMiddleProximal"] = self.leftMiddleProximal.to_dict() # noqa
        if is_enable(self.leftMiddleIntermediate): d["leftMiddleIntermediate"] = self.leftMiddleIntermediate.to_dict() # noqa
        if is_enable(self.leftMiddleDistal): d["leftMiddleDistal"] = self.leftMiddleDistal.to_dict() # noqa
        if is_enable(self.leftRingProximal): d["leftRingProximal"] = self.leftRingProximal.to_dict() # noqa
        if is_enable(self.leftRingIntermediate): d["leftRingIntermediate"] = self.leftRingIntermediate.to_dict() # noqa
        if is_enable(self.leftRingDistal): d["leftRingDistal"] = self.leftRingDistal.to_dict() # noqa
        if is_enable(self.leftLittleProximal): d["leftLittleProximal"] = self.leftLittleProximal.to_dict() # noqa
        if is_enable(self.leftLittleIntermediate): d["leftLittleIntermediate"] = self.leftLittleIntermediate.to_dict() # noqa
        if is_enable(self.leftLittleDistal): d["leftLittleDistal"] = self.leftLittleDistal.to_dict() # noqa
        if is_enable(self.rightThumbProximal): d["rightThumbProximal"] = self.rightThumbProximal.to_dict() # noqa
        if is_enable(self.rightThumbIntermediate): d["rightThumbIntermediate"] = self.rightThumbIntermediate.to_dict() # noqa
        if is_enable(self.rightThumbDistal): d["rightThumbDistal"] = self.rightThumbDistal.to_dict() # noqa
        if is_enable(self.rightIndexProximal): d["rightIndexProximal"] = self.rightIndexProximal.to_dict() # noqa
        if is_enable(self.rightIndexIntermediate): d["rightIndexIntermediate"] = self.rightIndexIntermediate.to_dict() # noqa
        if is_enable(self.rightIndexDistal): d["rightIndexDistal"] = self.rightIndexDistal.to_dict() # noqa
        if is_enable(self.rightMiddleProximal): d["rightMiddleProximal"] = self.rightMiddleProximal.to_dict() # noqa
        if is_enable(self.rightMiddleIntermediate): d["rightMiddleIntermediate"] = self.rightMiddleIntermediate.to_dict() # noqa
        if is_enable(self.rightMiddleDistal): d["rightMiddleDistal"] = self.rightMiddleDistal.to_dict() # noqa
        if is_enable(self.rightRingProximal): d["rightRingProximal"] = self.rightRingProximal.to_dict() # noqa
        if is_enable(self.rightRingIntermediate): d["rightRingIntermediate"] = self.rightRingIntermediate.to_dict() # noqa
        if is_enable(self.rightRingDistal): d["rightRingDistal"] = self.rightRingDistal.to_dict() # noqa
        if is_enable(self.rightLittleProximal): d["rightLittleProximal"] = self.rightLittleProximal.to_dict() # noqa
        if is_enable(self.rightLittleIntermediate): d["rightLittleIntermediate"] = self.rightLittleIntermediate.to_dict() # noqa
        if is_enable(self.rightLittleDistal): d["rightLittleDistal"] = self.rightLittleDistal.to_dict() # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'HumanBones':
        dst = {}
        if "hips" in src: dst["hips"] = HumanBone.from_dict(src["hips"]) # noqa
        if "spine" in src: dst["spine"] = HumanBone.from_dict(src["spine"]) # noqa
        if "chest" in src: dst["chest"] = HumanBone.from_dict(src["chest"]) # noqa
        if "upperChest" in src: dst["upperChest"] = HumanBone.from_dict(src["upperChest"]) # noqa
        if "neck" in src: dst["neck"] = HumanBone.from_dict(src["neck"]) # noqa
        if "head" in src: dst["head"] = HumanBone.from_dict(src["head"]) # noqa
        if "leftEye" in src: dst["leftEye"] = HumanBone.from_dict(src["leftEye"]) # noqa
        if "rightEye" in src: dst["rightEye"] = HumanBone.from_dict(src["rightEye"]) # noqa
        if "jaw" in src: dst["jaw"] = HumanBone.from_dict(src["jaw"]) # noqa
        if "leftUpperLeg" in src: dst["leftUpperLeg"] = HumanBone.from_dict(src["leftUpperLeg"]) # noqa
        if "leftLowerLeg" in src: dst["leftLowerLeg"] = HumanBone.from_dict(src["leftLowerLeg"]) # noqa
        if "leftFoot" in src: dst["leftFoot"] = HumanBone.from_dict(src["leftFoot"]) # noqa
        if "leftToes" in src: dst["leftToes"] = HumanBone.from_dict(src["leftToes"]) # noqa
        if "rightUpperLeg" in src: dst["rightUpperLeg"] = HumanBone.from_dict(src["rightUpperLeg"]) # noqa
        if "rightLowerLeg" in src: dst["rightLowerLeg"] = HumanBone.from_dict(src["rightLowerLeg"]) # noqa
        if "rightFoot" in src: dst["rightFoot"] = HumanBone.from_dict(src["rightFoot"]) # noqa
        if "rightToes" in src: dst["rightToes"] = HumanBone.from_dict(src["rightToes"]) # noqa
        if "leftShoulder" in src: dst["leftShoulder"] = HumanBone.from_dict(src["leftShoulder"]) # noqa
        if "leftUpperArm" in src: dst["leftUpperArm"] = HumanBone.from_dict(src["leftUpperArm"]) # noqa
        if "leftLowerArm" in src: dst["leftLowerArm"] = HumanBone.from_dict(src["leftLowerArm"]) # noqa
        if "leftHand" in src: dst["leftHand"] = HumanBone.from_dict(src["leftHand"]) # noqa
        if "rightShoulder" in src: dst["rightShoulder"] = HumanBone.from_dict(src["rightShoulder"]) # noqa
        if "rightUpperArm" in src: dst["rightUpperArm"] = HumanBone.from_dict(src["rightUpperArm"]) # noqa
        if "rightLowerArm" in src: dst["rightLowerArm"] = HumanBone.from_dict(src["rightLowerArm"]) # noqa
        if "rightHand" in src: dst["rightHand"] = HumanBone.from_dict(src["rightHand"]) # noqa
        if "leftThumbProximal" in src: dst["leftThumbProximal"] = HumanBone.from_dict(src["leftThumbProximal"]) # noqa
        if "leftThumbIntermediate" in src: dst["leftThumbIntermediate"] = HumanBone.from_dict(src["leftThumbIntermediate"]) # noqa
        if "leftThumbDistal" in src: dst["leftThumbDistal"] = HumanBone.from_dict(src["leftThumbDistal"]) # noqa
        if "leftIndexProximal" in src: dst["leftIndexProximal"] = HumanBone.from_dict(src["leftIndexProximal"]) # noqa
        if "leftIndexIntermediate" in src: dst["leftIndexIntermediate"] = HumanBone.from_dict(src["leftIndexIntermediate"]) # noqa
        if "leftIndexDistal" in src: dst["leftIndexDistal"] = HumanBone.from_dict(src["leftIndexDistal"]) # noqa
        if "leftMiddleProximal" in src: dst["leftMiddleProximal"] = HumanBone.from_dict(src["leftMiddleProximal"]) # noqa
        if "leftMiddleIntermediate" in src: dst["leftMiddleIntermediate"] = HumanBone.from_dict(src["leftMiddleIntermediate"]) # noqa
        if "leftMiddleDistal" in src: dst["leftMiddleDistal"] = HumanBone.from_dict(src["leftMiddleDistal"]) # noqa
        if "leftRingProximal" in src: dst["leftRingProximal"] = HumanBone.from_dict(src["leftRingProximal"]) # noqa
        if "leftRingIntermediate" in src: dst["leftRingIntermediate"] = HumanBone.from_dict(src["leftRingIntermediate"]) # noqa
        if "leftRingDistal" in src: dst["leftRingDistal"] = HumanBone.from_dict(src["leftRingDistal"]) # noqa
        if "leftLittleProximal" in src: dst["leftLittleProximal"] = HumanBone.from_dict(src["leftLittleProximal"]) # noqa
        if "leftLittleIntermediate" in src: dst["leftLittleIntermediate"] = HumanBone.from_dict(src["leftLittleIntermediate"]) # noqa
        if "leftLittleDistal" in src: dst["leftLittleDistal"] = HumanBone.from_dict(src["leftLittleDistal"]) # noqa
        if "rightThumbProximal" in src: dst["rightThumbProximal"] = HumanBone.from_dict(src["rightThumbProximal"]) # noqa
        if "rightThumbIntermediate" in src: dst["rightThumbIntermediate"] = HumanBone.from_dict(src["rightThumbIntermediate"]) # noqa
        if "rightThumbDistal" in src: dst["rightThumbDistal"] = HumanBone.from_dict(src["rightThumbDistal"]) # noqa
        if "rightIndexProximal" in src: dst["rightIndexProximal"] = HumanBone.from_dict(src["rightIndexProximal"]) # noqa
        if "rightIndexIntermediate" in src: dst["rightIndexIntermediate"] = HumanBone.from_dict(src["rightIndexIntermediate"]) # noqa
        if "rightIndexDistal" in src: dst["rightIndexDistal"] = HumanBone.from_dict(src["rightIndexDistal"]) # noqa
        if "rightMiddleProximal" in src: dst["rightMiddleProximal"] = HumanBone.from_dict(src["rightMiddleProximal"]) # noqa
        if "rightMiddleIntermediate" in src: dst["rightMiddleIntermediate"] = HumanBone.from_dict(src["rightMiddleIntermediate"]) # noqa
        if "rightMiddleDistal" in src: dst["rightMiddleDistal"] = HumanBone.from_dict(src["rightMiddleDistal"]) # noqa
        if "rightRingProximal" in src: dst["rightRingProximal"] = HumanBone.from_dict(src["rightRingProximal"]) # noqa
        if "rightRingIntermediate" in src: dst["rightRingIntermediate"] = HumanBone.from_dict(src["rightRingIntermediate"]) # noqa
        if "rightRingDistal" in src: dst["rightRingDistal"] = HumanBone.from_dict(src["rightRingDistal"]) # noqa
        if "rightLittleProximal" in src: dst["rightLittleProximal"] = HumanBone.from_dict(src["rightLittleProximal"]) # noqa
        if "rightLittleIntermediate" in src: dst["rightLittleIntermediate"] = HumanBone.from_dict(src["rightLittleIntermediate"]) # noqa
        if "rightLittleDistal" in src: dst["rightLittleDistal"] = HumanBone.from_dict(src["rightLittleDistal"]) # noqa
        return HumanBones(**dst)


class Humanoid(NamedTuple):
    # Represents a set of humanBones of a humanoid.
    humanBones: HumanBones

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.humanBones): d["humanBones"] = self.humanBones.to_dict() # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'Humanoid':
        dst = {}
        if "humanBones" in src: dst["humanBones"] = HumanBones.from_dict(src["humanBones"]) # noqa
        return Humanoid(**dst)


class MeshAnnotation(NamedTuple):
    # The index of the node that attached to target mesh.
    node: Optional[int] = None
    # How the camera interprets the mesh.
    firstPersonType: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.node): d["node"] = self.node # noqa
        if is_enable(self.firstPersonType): d["firstPersonType"] = self.firstPersonType # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'MeshAnnotation':
        dst = {}
        if "node" in src: dst["node"] = src["node"] # noqa copy
        if "firstPersonType" in src: dst["firstPersonType"] = src["firstPersonType"] # noqa copy
        return MeshAnnotation(**dst)


class FirstPerson(NamedTuple):
    # Mesh rendering annotation for cameras. 'required' :   [  'mesh' ,  'firstPersonType'  ]
    meshAnnotations: Optional[List[MeshAnnotation]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.meshAnnotations: d["meshAnnotations"] = [item.to_dict() for item in self.meshAnnotations] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'FirstPerson':
        dst = {}
        dst["meshAnnotations"] = [MeshAnnotation.from_dict(item) for item in src["meshAnnotations"]] if "meshAnnotations" in src else [] # noqa
        return FirstPerson(**dst)


class LookAtRangeMap(NamedTuple):
    # Yaw and pitch angles  ( degrees )  between the head bone forward vector and the eye gaze LookAt vector
    inputMaxValue: Optional[float] = None
    # Degree for LookAtType.bone ,  Weight for LookAtType.blendShape
    outputScale: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.inputMaxValue): d["inputMaxValue"] = self.inputMaxValue # noqa
        if is_enable(self.outputScale): d["outputScale"] = self.outputScale # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'LookAtRangeMap':
        dst = {}
        if "inputMaxValue" in src: dst["inputMaxValue"] = src["inputMaxValue"] # noqa copy
        if "outputScale" in src: dst["outputScale"] = src["outputScale"] # noqa copy
        return LookAtRangeMap(**dst)


class LookAt(NamedTuple):
    # The origin of LookAt. Position offset from the head bone
    offsetFromHeadBone: Optional[List[float]] = None
    # 
    lookAtType: Optional[str] = None
    # Horizontal inward movement. The left eye moves right. The right eye moves left.
    lookAtHorizontalInner: Optional[LookAtRangeMap] = None
    # Horizontal inward movement. The left eye moves right. The right eye moves left.
    lookAtHorizontalOuter: Optional[LookAtRangeMap] = None
    # Horizontal inward movement. The left eye moves right. The right eye moves left.
    lookAtVerticalDown: Optional[LookAtRangeMap] = None
    # Horizontal inward movement. The left eye moves right. The right eye moves left.
    lookAtVerticalUp: Optional[LookAtRangeMap] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if self.offsetFromHeadBone: d["offsetFromHeadBone"] = self.offsetFromHeadBone # noqa
        if is_enable(self.lookAtType): d["lookAtType"] = self.lookAtType # noqa
        if is_enable(self.lookAtHorizontalInner): d["lookAtHorizontalInner"] = self.lookAtHorizontalInner.to_dict() # noqa
        if is_enable(self.lookAtHorizontalOuter): d["lookAtHorizontalOuter"] = self.lookAtHorizontalOuter.to_dict() # noqa
        if is_enable(self.lookAtVerticalDown): d["lookAtVerticalDown"] = self.lookAtVerticalDown.to_dict() # noqa
        if is_enable(self.lookAtVerticalUp): d["lookAtVerticalUp"] = self.lookAtVerticalUp.to_dict() # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'LookAt':
        dst = {}
        dst["offsetFromHeadBone"] = src.get("offsetFromHeadBone", [])
        if "lookAtType" in src: dst["lookAtType"] = src["lookAtType"] # noqa copy
        if "lookAtHorizontalInner" in src: dst["lookAtHorizontalInner"] = LookAtRangeMap.from_dict(src["lookAtHorizontalInner"]) # noqa
        if "lookAtHorizontalOuter" in src: dst["lookAtHorizontalOuter"] = LookAtRangeMap.from_dict(src["lookAtHorizontalOuter"]) # noqa
        if "lookAtVerticalDown" in src: dst["lookAtVerticalDown"] = LookAtRangeMap.from_dict(src["lookAtVerticalDown"]) # noqa
        if "lookAtVerticalUp" in src: dst["lookAtVerticalUp"] = LookAtRangeMap.from_dict(src["lookAtVerticalUp"]) # noqa
        return LookAt(**dst)


class MorphTargetBind(NamedTuple):
    # The index of the node that attached to target mesh.
    node: int
    # The index of the morph target in the mesh.
    index: int
    # The weight value of target morph target.
    weight: float
    # Dictionary object with extension-specific objects.
    extensions: Optional[Dict[str, Dict[str, Any]]] = None
    # Application-specific data.
    extras: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.node): d["node"] = self.node # noqa
        if is_enable(self.index): d["index"] = self.index # noqa
        if is_enable(self.weight): d["weight"] = self.weight # noqa
        if is_enable(self.extensions): d["extensions"] = self.extensions # noqa
        if is_enable(self.extras): d["extras"] = self.extras # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'MorphTargetBind':
        dst = {}
        if "node" in src: dst["node"] = src["node"] # noqa copy
        if "index" in src: dst["index"] = src["index"] # noqa copy
        if "weight" in src: dst["weight"] = src["weight"] # noqa copy
        dst["extensions"] = src.get("extensions", {})
        dst["extras"] = src.get("extras", {})
        return MorphTargetBind(**dst)


class MaterialColorBind(NamedTuple):
    # target material
    material: int
    # 
    type: str
    # target color
    targetValue: List[float]
    # Dictionary object with extension-specific objects.
    extensions: Optional[Dict[str, Dict[str, Any]]] = None
    # Application-specific data.
    extras: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.material): d["material"] = self.material # noqa
        if is_enable(self.type): d["type"] = self.type # noqa
        if self.targetValue: d["targetValue"] = self.targetValue # noqa
        if is_enable(self.extensions): d["extensions"] = self.extensions # noqa
        if is_enable(self.extras): d["extras"] = self.extras # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'MaterialColorBind':
        dst = {}
        if "material" in src: dst["material"] = src["material"] # noqa copy
        if "type" in src: dst["type"] = src["type"] # noqa copy
        dst["targetValue"] = src.get("targetValue", [])
        dst["extensions"] = src.get("extensions", {})
        dst["extras"] = src.get("extras", {})
        return MaterialColorBind(**dst)


class TextureTransformBind(NamedTuple):
    # target material
    material: int
    # uv scaling for TEXCOORD_0
    scaling: Optional[List[float]] = None
    # uv offset for TEXCOORD_0
    offset: Optional[List[float]] = None
    # Dictionary object with extension-specific objects.
    extensions: Optional[Dict[str, Dict[str, Any]]] = None
    # Application-specific data.
    extras: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.material): d["material"] = self.material # noqa
        if self.scaling: d["scaling"] = self.scaling # noqa
        if self.offset: d["offset"] = self.offset # noqa
        if is_enable(self.extensions): d["extensions"] = self.extensions # noqa
        if is_enable(self.extras): d["extras"] = self.extras # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'TextureTransformBind':
        dst = {}
        if "material" in src: dst["material"] = src["material"] # noqa copy
        dst["scaling"] = src.get("scaling", [])
        dst["offset"] = src.get("offset", [])
        dst["extensions"] = src.get("extensions", {})
        dst["extras"] = src.get("extras", {})
        return TextureTransformBind(**dst)


class Expression(NamedTuple):
    # Functions of Expression
    preset: str
    # Use only if the preset is custom. Unique within the model
    name: Optional[str] = None
    # Specify a morph target
    morphTargetBinds: Optional[List[MorphTargetBind]] = None
    # Material color animation references
    materialColorBinds: Optional[List[MaterialColorBind]] = None
    # Texture transform animation references
    textureTransformBinds: Optional[List[TextureTransformBind]] = None
    # Interpret non-zero values as 1
    isBinary: Optional[bool] = None
    # Override values of Blink expressions when this Expression is enabled
    overrideBlink: Optional[str] = None
    # Override values of LookAt expressions when this Expression is enabled
    overrideLookAt: Optional[str] = None
    # Override values of Mouth expressions when this Expression is enabled
    overrideMouth: Optional[str] = None
    # Dictionary object with extension-specific objects.
    extensions: Optional[Dict[str, Dict[str, Any]]] = None
    # Application-specific data.
    extras: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.name): d["name"] = self.name # noqa
        if is_enable(self.preset): d["preset"] = self.preset # noqa
        if self.morphTargetBinds: d["morphTargetBinds"] = [item.to_dict() for item in self.morphTargetBinds] # noqa
        if self.materialColorBinds: d["materialColorBinds"] = [item.to_dict() for item in self.materialColorBinds] # noqa
        if self.textureTransformBinds: d["textureTransformBinds"] = [item.to_dict() for item in self.textureTransformBinds] # noqa
        if is_enable(self.isBinary): d["isBinary"] = self.isBinary # noqa
        if is_enable(self.overrideBlink): d["overrideBlink"] = self.overrideBlink # noqa
        if is_enable(self.overrideLookAt): d["overrideLookAt"] = self.overrideLookAt # noqa
        if is_enable(self.overrideMouth): d["overrideMouth"] = self.overrideMouth # noqa
        if is_enable(self.extensions): d["extensions"] = self.extensions # noqa
        if is_enable(self.extras): d["extras"] = self.extras # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'Expression':
        dst = {}
        if "name" in src: dst["name"] = src["name"] # noqa copy
        if "preset" in src: dst["preset"] = src["preset"] # noqa copy
        dst["morphTargetBinds"] = [MorphTargetBind.from_dict(item) for item in src["morphTargetBinds"]] if "morphTargetBinds" in src else [] # noqa
        dst["materialColorBinds"] = [MaterialColorBind.from_dict(item) for item in src["materialColorBinds"]] if "materialColorBinds" in src else [] # noqa
        dst["textureTransformBinds"] = [TextureTransformBind.from_dict(item) for item in src["textureTransformBinds"]] if "textureTransformBinds" in src else [] # noqa
        if "isBinary" in src: dst["isBinary"] = src["isBinary"] # noqa copy
        if "overrideBlink" in src: dst["overrideBlink"] = src["overrideBlink"] # noqa copy
        if "overrideLookAt" in src: dst["overrideLookAt"] = src["overrideLookAt"] # noqa copy
        if "overrideMouth" in src: dst["overrideMouth"] = src["overrideMouth"] # noqa copy
        dst["extensions"] = src.get("extensions", {})
        dst["extras"] = src.get("extras", {})
        return Expression(**dst)


class VRMCVrm(NamedTuple):
    # 
    specVersion: Optional[str] = None
    # 
    meta: Optional[Meta] = None
    # Correspondence between nodes and human bones
    humanoid: Optional[Humanoid] = None
    # First-person perspective settings
    firstPerson: Optional[FirstPerson] = None
    # Eye gaze control
    lookAt: Optional[LookAt] = None
    # Definitions of expressions
    expressions: Optional[List[Expression]] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {}
        if is_enable(self.specVersion): d["specVersion"] = self.specVersion # noqa
        if is_enable(self.meta): d["meta"] = self.meta.to_dict() # noqa
        if is_enable(self.humanoid): d["humanoid"] = self.humanoid.to_dict() # noqa
        if is_enable(self.firstPerson): d["firstPerson"] = self.firstPerson.to_dict() # noqa
        if is_enable(self.lookAt): d["lookAt"] = self.lookAt.to_dict() # noqa
        if self.expressions: d["expressions"] = [item.to_dict() for item in self.expressions] # noqa
        return d

    @staticmethod
    def from_dict(src: dict) -> 'VRMCVrm':
        dst = {}
        if "specVersion" in src: dst["specVersion"] = src["specVersion"] # noqa copy
        if "meta" in src: dst["meta"] = Meta.from_dict(src["meta"]) # noqa
        if "humanoid" in src: dst["humanoid"] = Humanoid.from_dict(src["humanoid"]) # noqa
        if "firstPerson" in src: dst["firstPerson"] = FirstPerson.from_dict(src["firstPerson"]) # noqa
        if "lookAt" in src: dst["lookAt"] = LookAt.from_dict(src["lookAt"]) # noqa
        dst["expressions"] = [Expression.from_dict(item) for item in src["expressions"]] if "expressions" in src else [] # noqa
        return VRMCVrm(**dst)


if __name__ == '__main__':
    pass
