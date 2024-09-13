from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.text.constant")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"local {name} = TextChannel.constant('{properties[0]}')\n")
    return name
