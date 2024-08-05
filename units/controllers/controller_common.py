from typing import TextIO
from .. import deserializer, deserialize, get_name, is_clone, has_feature, FEATURE_JUDGE_MANIPULATION

position = ["beatline","camera","canvas","image","sprite","text","tg"]
color = ["image","sprite","text","tg"]
layer = ["sprite","canvas"]
text= ["text"]
notegroup = ["tg"]
camera = ["camera"]
rect = ["image","text","canvas"]
texture = ["sprite"]
track = ["track"]

cast_unit_mapping = {
    "track": "sprite",
    "critline0": "sprite",
    "critline1": "sprite",
    "critline2": "sprite",
    "critline3": "sprite",
    "critline4": "sprite",
    "critline5": "sprite",
    "edgeextraL": "sprite",
    "edgeextraR": "sprite",
    "extraL": "sprite",
    "extraR": "sprite",
    "divline01": "sprite",
    "divline12": "sprite",
    "divline23": "sprite",
    "divline34": "sprite",
    "divline45": "sprite",
    "combo": "text",
    "scoreTitle": "text",
    "score": "text",
    "predictedGrade": "text",
    "predictedGradeBg": "image",
    "jacketBg": "image",
    "jacket": "image",
    "title": "text",
    "composer": "text",
    "diff": "text",
    "diffBg": "image",
    "hud": "canvas",
    "info": "image",
    "pause": "image",
    "bg": "image",
    "videobg": "sprite",
    "singlelinel": "sprite",
    "singleliner": "sprite",
    "skyinputline": "sprite",
    "skyinputlabel": "sprite",
    "darken": "sprite",
    "worldcanvas": "canvas",
    "screencanvas": "canvas",
    "cameracanvas": "canvas",
}

def cast_unit(unit_type: str):
    if unit_type in cast_unit_mapping:
        return cast_unit_mapping[unit_type]
    else:
        return unit_type

def create_internal(key):
    def wrap(writer:TextIO, all_units: list, unit_id: int, properties: list):
        name = get_name(unit_id)
        unit_type = all_units[unit_id]["Type"]
        if is_clone(unit_type):
            writer.write(f"{name} = {key}.copy()\n")
        else:
            writer.write(f"{name} = {key}\n")
        controller_deserialize(writer, all_units, unit_type, unit_id, properties)
        return name
    return wrap

def controller_deserialize(writer:TextIO, all_units: list, unit_type: str, unit_id: int, properties: list):
    properties = properties.copy()
    name = get_name(unit_id)
    customParent = properties.pop(0)
    if customParent is not None:
        customParent = get_name(customParent)
        writer.write(f"{name}.setParent({customParent})\n")
    active = deserialize(writer, all_units, properties.pop(0))
    alt_unit_type = cast_unit(unit_type)
    if unit_type in position or alt_unit_type in position:
        enable = properties.pop(0)
        translationX = deserialize(writer, all_units, properties.pop(0))
        translationY = deserialize(writer, all_units, properties.pop(0))
        translationZ = deserialize(writer, all_units, properties.pop(0))
        rotationX = deserialize(writer, all_units, properties.pop(0))
        rotationY = deserialize(writer, all_units, properties.pop(0))
        rotationZ = deserialize(writer, all_units, properties.pop(0))
        scaleX = deserialize(writer, all_units, properties.pop(0))
        scaleY = deserialize(writer, all_units, properties.pop(0))
        scaleZ = deserialize(writer, all_units, properties.pop(0))
        if enable:
            writer.write(f"{name}.translationX = {translationX}\n")
            writer.write(f"{name}.translationY = {translationY}\n")
            writer.write(f"{name}.translationZ = {translationZ}\n")
            writer.write(f"{name}.rotationX = {rotationX}\n")
            writer.write(f"{name}.rotationY = {rotationY}\n")
            writer.write(f"{name}.rotationZ = {rotationZ}\n")
            writer.write(f"{name}.scaleX = {scaleX}\n")
            writer.write(f"{name}.scaleY = {scaleY}\n")
            writer.write(f"{name}.scaleZ = {scaleZ}\n")
    if unit_type in color or alt_unit_type in color:
        enable = properties.pop(0)
        colorR = deserialize(writer, all_units, properties.pop(0))
        colorG = deserialize(writer, all_units, properties.pop(0))
        colorB = deserialize(writer, all_units, properties.pop(0))
        colorA = deserialize(writer, all_units, properties.pop(0))
        colorH = deserialize(writer, all_units, properties.pop(0))
        colorS = deserialize(writer, all_units, properties.pop(0))
        colorV = deserialize(writer, all_units, properties.pop(0))
        if enable:
            writer.write(f"{name}.colorR = {colorR}\n")
            writer.write(f"{name}.colorG = {colorG}\n")
            writer.write(f"{name}.colorB = {colorB}\n")
            writer.write(f"{name}.colorA = {colorA}\n")
            writer.write(f"{name}.colorH = {colorH}\n")
            writer.write(f"{name}.colorS = {colorS}\n")
            writer.write(f"{name}.colorV = {colorV}\n")
    if unit_type in layer or alt_unit_type in layer:
        enable = properties.pop(0)
        layers = deserialize(writer, all_units, properties.pop(0))
        sort = deserialize(writer, all_units, properties.pop(0))
        alpha = deserialize(writer, all_units, properties.pop(0))
        if enable:
            writer.write(f"{name}.layer = {layers}\n")
            writer.write(f"{name}.sort = {sort}\n")
            writer.write(f"{name}.alpha = {alpha}\n")
    if unit_type in text or alt_unit_type in text:
        enable = properties.pop(0)
        fontSize = deserialize(writer, all_units, properties.pop(0))
        lineSpacing = deserialize(writer, all_units, properties.pop(0))
        txt = deserialize(writer, all_units, properties.pop(0))
        customFont = properties.pop(0)
        if enable:
            writer.write(f"{name}.applyCustomFont('{customFont}')\n")
        #     writer.write(f"{name}.layer = {layer}\n")
        #     writer.write(f"{name}.sort = {sort}\n")
        #     writer.write(f"{name}.alpha = {alpha}\n")
    if unit_type in notegroup or alt_unit_type in notegroup:
        enable = properties.pop(0)
        angleX = deserialize(writer, all_units, properties.pop(0))
        angleY = deserialize(writer, all_units, properties.pop(0))
        rotationIndividualX = deserialize(writer, all_units, properties.pop(0))
        rotationIndividualY = deserialize(writer, all_units, properties.pop(0))
        rotationIndividualZ = deserialize(writer, all_units, properties.pop(0))
        scaleIndividualX = deserialize(writer, all_units, properties.pop(0))
        scaleIndividualY = deserialize(writer, all_units, properties.pop(0))
        scaleIndividualZ = deserialize(writer, all_units, properties.pop(0))
        judgeSizeX = None
        judgeSizeY = None
        judgeOffsetX = None
        judgeOffsetY = None
        judgeOffsetZ = None
        if has_feature(FEATURE_JUDGE_MANIPULATION):
            judgeSizeX = deserialize(writer, all_units, properties.pop(0))
            judgeSizeY = deserialize(writer, all_units, properties.pop(0))
            judgeOffsetX = deserialize(writer, all_units, properties.pop(0))
            judgeOffsetY = deserialize(writer, all_units, properties.pop(0))
            judgeOffsetZ = deserialize(writer, all_units, properties.pop(0))
        if enable:
            writer.write(f"{name}.angleX = {angleX}\n")
            writer.write(f"{name}.angleY = {angleY}\n")
            writer.write(f"{name}.rotationIndividualX = {rotationIndividualX}\n")
            writer.write(f"{name}.rotationIndividualY = {rotationIndividualY}\n")
            writer.write(f"{name}.rotationIndividualZ = {angleY}\n")
            writer.write(f"{name}.scaleIndividualX = {scaleIndividualX}\n")
            writer.write(f"{name}.scaleIndividualY = {scaleIndividualY}\n")
            writer.write(f"{name}.scaleIndividualZ = {scaleIndividualZ}\n")
            if has_feature(FEATURE_JUDGE_MANIPULATION):
                writer.write(f"{name}.judgeSizeX = {judgeSizeX}\n")
                writer.write(f"{name}.judgeSizeY = {judgeSizeY}\n")
                writer.write(f"{name}.judgeOffsetX = {judgeOffsetX}\n")
                writer.write(f"{name}.judgeOffsetY = {judgeOffsetY}\n")
                writer.write(f"{name}.judgeOffsetZ = {judgeOffsetZ}\n")
    if unit_type in rect or alt_unit_type in rect:
        enable = properties.pop(0)
        rectW = deserialize(writer, all_units, properties.pop(0))
        rectH = deserialize(writer, all_units, properties.pop(0))
        anchorMinX = deserialize(writer, all_units, properties.pop(0))
        anchorMinY = deserialize(writer, all_units, properties.pop(0))
        anchorMaxX = deserialize(writer, all_units, properties.pop(0))
        anchorMaxY = deserialize(writer, all_units, properties.pop(0))
        pivotX = deserialize(writer, all_units, properties.pop(0))
        pivotY = deserialize(writer, all_units, properties.pop(0))
        if enable:
            writer.write(f"{name}.rectW = {rectW}\n")
            writer.write(f"{name}.rectH = {rectH}\n")
            writer.write(f"{name}.anchorMinX = {anchorMinX}\n")
            writer.write(f"{name}.anchorMinY = {anchorMinY}\n")
            writer.write(f"{name}.anchorMaxX = {anchorMaxX}\n")
            writer.write(f"{name}.anchorMaxY = {anchorMaxY}\n")
            writer.write(f"{name}.pivotX = {pivotX}\n")
            writer.write(f"{name}.pivotY = {pivotY}\n")
    if unit_type in texture or alt_unit_type in texture:
        enable = properties.pop(0)
        textureOffsetX = deserialize(writer, all_units, properties.pop(0))
        textureOffsetY = deserialize(writer, all_units, properties.pop(0))
        textureScaleX = deserialize(writer, all_units, properties.pop(0))
        textureScaleY = deserialize(writer, all_units, properties.pop(0))
        writer.write(f"{name}.textureOffsetX = {textureOffsetX}\n")
        writer.write(f"{name}.textureOffsetY = {textureOffsetY}\n")
        writer.write(f"{name}.textureScaleX = {textureScaleX}\n")
        writer.write(f"{name}.textureScaleY = {textureScaleY}\n")
    if unit_type in track or alt_unit_type in track:
        enable = properties.pop(0)
        edgeLAlpha = deserialize(writer, all_units, properties.pop(0))
        edgeRAlpha = deserialize(writer, all_units, properties.pop(0))
        lane1Alpha = deserialize(writer, all_units, properties.pop(0))
        lane2Alpha = deserialize(writer, all_units, properties.pop(0))
        lane3Alpha = deserialize(writer, all_units, properties.pop(0))
        lane4Alpha = deserialize(writer, all_units, properties.pop(0))
        customSkin = writer, all_units, properties.pop(0)
        if enable:
            writer.write(f"{name}.edgeLAlpha = {edgeLAlpha}\n")
            writer.write(f"{name}.edgeRAlpha = {edgeRAlpha}\n")
            writer.write(f"{name}.lane1Alpha = {lane1Alpha}\n")
            writer.write(f"{name}.lane2Alpha = {lane2Alpha}\n")
            writer.write(f"{name}.lane3Alpha = {lane3Alpha}\n")
            writer.write(f"{name}.lane4Alpha = {lane4Alpha}\n")
            writer.write(f"{name}.setTrackSprite('{customSkin}')\n")
        

