from typing import TextIO
from .. import deserializer, deserialize, get_name
from .controller_common import controller_deserialize

@deserializer(type_name="tg")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    tgIndex = unit_type.split(".")[1]
    tgIndex = int(tgIndex)
    writer.write(f"{name} = Scene.getNoteGroup({tgIndex})\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
