from typing import TextIO
from .. import deserializer, deserialize, get_name, pop_and_set_property, pop_and_call_raw
from .postprocessing_common import enable_effect_array

@deserializer(type_name="chromaticAberration")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"{name} = PostProcessing.chromaticAberration\n")
    enabled = properties.pop(0)
    enableEffects = enable_effect_array(["intensity"], properties)
    writer.write(f"{name}.enableEffects({enableEffects})")
    pop_and_set_property(writer, all_units, properties, unit_id, "intensity")
    pop_and_call_raw(writer, all_units, properties, unit_id, "setFastMode")
    return name
