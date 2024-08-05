from typing import TextIO
from .. import deserializer, deserialize, get_name
from .controller_common import controller_deserialize

@deserializer(type_name="sprite")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    unit_type, params = unit_type.split(".",1)
    path, blendMode, renderLayer, pivotX, pivotY = params.split(",")
    writer.write(f"{name} = Scene.createSprite('{path}','{blendMode}','{renderLayer}',xy({pivotX},{pivotY}))\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
