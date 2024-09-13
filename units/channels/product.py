from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.product")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    for i in range(len(properties)):
        v = properties[i]
        properties[i] = deserialize(writer, all_units, v)
    args = "*".join(properties)
    writer.write(f"local {name} = {args}\n")
    return name
