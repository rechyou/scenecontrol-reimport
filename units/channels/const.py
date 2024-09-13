from typing import TextIO
from .. import deserializer, add_deserializer, deserialize, get_name

constants = {}

@deserializer(type_name="channel.const")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    global constants
    name = get_name(unit_id)
    value = properties[0]
    valueKey = str(value)
    if valueKey in constants:
        # writer.write(f"{name} = {constants[valueKey]} -- constant rewrite\n")
        return constants[valueKey]
    value = float(value)
    writer.write(f"local {name} = Channel.constant({value:g})\n")
    constants[valueKey] = name
    return name
