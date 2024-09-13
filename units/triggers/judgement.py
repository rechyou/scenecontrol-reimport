from typing import TextIO
from .. import deserializer, deserialize, get_name

mapping = [
    "Max",
    "PerfectEarly",
    "PerfectLate",
    "GoodEarly",
    "GoodLate",
    "MissEarly",
    "MissLate"
]

@deserializer(type_name="trigger.judgement")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    
    value, duration, easing = properties[7], properties[8], properties[9]
    value = deserialize(writer, all_units, value)
    duration = deserialize(writer, all_units, duration)
    if easing is None:
        easing = "l"

    writer.write(f"{name} = Trigger.judgement()\n")
    for i in range(len(mapping)):
        if properties[i]:
            writer.write(f".on{mapping[i]}()\n")
    writer.write(f".dispatch({value},{duration},'{easing}')\n")
    return name
