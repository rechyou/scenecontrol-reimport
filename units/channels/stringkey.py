from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.string.key")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"{name} = StringChannel.create()\n")
    for v in properties:
        timing,value = v.split(",", 2)
        writer.write(f".addKey({timing},'{value}')\n")
    return name
