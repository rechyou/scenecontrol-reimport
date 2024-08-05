from typing import TextIO
from .. import deserializer, deserialize, get_name, is_clone
from .controller_common import controller_deserialize

@deserializer(type_name="canvas")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    unit_type, worldSpace = unit_type.split(".",1)[1]
    if worldSpace == "true":
        writer.write(f"{name} = Scene.createCanvas(true)\n")
    else:
        writer.write(f"{name} = Scene.createCanvas(false)\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
