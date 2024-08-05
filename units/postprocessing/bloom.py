from typing import TextIO
from .. import deserializer, deserialize, get_name, pop_and_set_property
from .postprocessing_common import enable_effect_array

@deserializer(type_name="bloom")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"{name} = PostProcessing.bloom\n")
    enabled = properties.pop(0)
    enableEffects = enable_effect_array(
        ["intensity",
        "threshold",
        "softknee",
        "clamp",
        "diffusion",
        "anamorphicratio",
        "color"]
        , properties)
    writer.write(f"{name}.enableEffects({enableEffects})")
    pop_and_set_property(writer, all_units, properties, unit_id, "intensity")
    pop_and_set_property(writer, all_units, properties, unit_id, "threshold")
    pop_and_set_property(writer, all_units, properties, unit_id, "softKnee")
    pop_and_set_property(writer, all_units, properties, unit_id, "clamp")
    pop_and_set_property(writer, all_units, properties, unit_id, "diffusion")
    pop_and_set_property(writer, all_units, properties, unit_id, "anamorphicRatio")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorR")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorG")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorB")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorA")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorH")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorS")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorV")
    return name
