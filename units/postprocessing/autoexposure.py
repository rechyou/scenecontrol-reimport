from typing import TextIO
from .. import deserializer, deserialize, get_name, pop_and_set_property, pop_and_call_raw
from .postprocessing_common import enable_effect_array

@deserializer(type_name="autoExposure")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"{name} = PostProcessing.autoExposure\n")
    enabled = properties.pop(0)
    enableEffects = enable_effect_array(
        ["filtering",
        "minluminance",
        "maxluminance",
        "keyvalue",
        "speedup",
        "speeddown"], properties)
    writer.write(f"{name}.enableEffects({enableEffects})")
    pop_and_set_property(writer, all_units, properties, unit_id, "filteringFrom")
    pop_and_set_property(writer, all_units, properties, unit_id, "filteringTo")
    pop_and_set_property(writer, all_units, properties, unit_id, "minLuminance")
    pop_and_set_property(writer, all_units, properties, unit_id, "maxLuminance")
    pop_and_set_property(writer, all_units, properties, unit_id, "keyValue")
    pop_and_set_property(writer, all_units, properties, unit_id, "speedUp")
    pop_and_set_property(writer, all_units, properties, unit_id, "speedDown")
    pop_and_call_raw(writer, all_units, properties, unit_id, "setEyeAdaption")
    return name
