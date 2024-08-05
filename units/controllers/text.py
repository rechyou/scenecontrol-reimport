from typing import TextIO
from .. import deserializer, deserialize, get_name, is_clone
from .controller_common import controller_deserialize

@deserializer(type_name="text")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    unit_type, args = unit_type.split(".",1)[1]
    args = createText.split(",")
    writer.write(f"{name} = Scene.createText('{args[0]}',{args[1]},{args[2]},'{args[3]}','{args[4]}')\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
