from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.saw")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    p = properties
    p[0], p[1], p[2], p[3], p[4] = p[4], p[0], p[2], p[3], p[1]
    p[0] = f"'{p[0]}'"
    for i in range(len(properties)):
        if i == 0: continue
        v = properties[i]
        properties[i] = deserialize(writer, all_units, v)
    args = ",".join(properties)
    writer.write(f"{name} = Channel.saw({args})\n")
    return name
