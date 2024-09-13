from typing import TextIO
from .. import deserializer, deserialize, get_name

@deserializer(type_name="trigger.observe")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    target,above, below, value, duration, easing = properties
    target = deserialize(writer, all_units, target)
    if easing is None:
        easing = "l"
    writer.write(f"{name} = Trigger.observe({target})\n")
    above = deserialize(writer, all_units, above)
    below = deserialize(writer, all_units, below)
    value = deserialize(writer, all_units, value)
    duration = deserialize(writer, all_units, duration)
    return name
