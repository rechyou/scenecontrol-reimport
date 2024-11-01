from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="channel.key")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"local {name} = Channel.keyframe()\n")
    for v in properties:
        timing,value,easing = v.split(",")
        writer.write(f".addKey({timing},{value},'{easing}')\n")
    # writer.write(f"keyframe({name},{{")
    # for v in properties:
    #     timing,value,easing = v.split(",")
    #     writer.write(f"[{timing}]={{{value},'{easing}'}},")
    # writer.write("})\n")
    return name
