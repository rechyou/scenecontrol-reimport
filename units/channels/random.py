from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.random")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    p = properties
    p[0] = str(p[0])
    p[1] = deserialize(writer, all_units, p[1])
    p[2] = deserialize(writer, all_units, p[2])
    args = ",".join(properties)
    writer.write(f"local {name} = Channel.random({args})\n")
    return name
