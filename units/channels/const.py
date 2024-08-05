from typing import TextIO
from .. import deserializer, add_deserializer, deserialize, get_name

constants = {}

@deserializer(type_name="channel.const")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    value = properties[0]
    if value in constants:
        return constants[value]
    value = float(value)
    writer.write(f"{name} = Channel.constant({value:g})\n")
    constants[value] = name
    return name
