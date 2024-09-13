from typing import TextIO
from .. import deserializer, deserialize, get_name, pop_and_set_property
from .controller_common import controller_deserialize

@deserializer(type_name="context")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    laneFrom = deserialize(writer, all_units, properties.pop(0))
    laneTo = deserialize(writer, all_units, properties.pop(0))
    writer.write(f"Context.laneFrom = {laneFrom} \n")
    writer.write(f"Context.laneTo = {laneTo} \n")
    return ""
