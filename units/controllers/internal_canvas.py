from typing import TextIO
from .. import deserializer, deserialize, get_name, is_clone
from .controller_common import controller_deserialize

@deserializer(type_name="worldcanvas")
def worldcanvas(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    if is_clone(unit_type):
        writer.write(f"local {name} = Scene.worldCanvas.copy()\n")
    else:
        writer.write(f"local {name} = Scene.worldCanvas\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name

@deserializer(type_name="screencanvas")
def screencanvas(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    if is_clone(unit_type):
        writer.write(f"local {name} = Scene.screenCanvas.copy()\n")
    else:
        writer.write(f"local {name} = Scene.screenCanvas\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name

@deserializer(type_name="cameracanvas")
def cameracanvas(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    unit_type = all_units[unit_id]["Type"]
    if is_clone(unit_type):
        writer.write(f"local {name} = Scene.cameraCanvas.copy()\n")
    else:
        writer.write(f"local {name} = Scene.cameraCanvas\n")
    controller_deserialize(writer, all_units, unit_type, unit_id, properties)
    return name
