from typing import TextIO
from .. import deserializer, deserialize, get_name, is_clone
from .controller_common import controller_deserialize

@deserializer(type_name="hud")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    if is_clone(unit_type):
        writer.write(f"{name} = Scene.hud.copy()\n")
    else:
        writer.write(f"{name} = Scene.hud\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
