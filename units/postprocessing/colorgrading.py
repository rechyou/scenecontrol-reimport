from typing import TextIO
from .. import deserializer, deserialize, get_name, pop_and_set_property, pop_and_call_raw
from .postprocessing_common import enable_effect_array

@deserializer(type_name="colorGrading")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = get_name(unit_id)
    writer.write(f"{name} = PostProcessing.colorGrading\n")
    enabled = properties.pop(0)
    enableEffects = enable_effect_array(
        ["temperature",
        "tint",
        "colorfilter",
        "hueshift",
        "saturation",
        "brightness",
        "constrast",
        "mixerredoutredin",
        "mixerredoutbluein",
        "mixerredoutgreenin",
        "mixergreenoutredin",
        "mixergreenoutbluein",
        "mixergreenoutgreenin",
        "mixerblueoutredin",
        "mixerblueoutbluein",
        "mixerblueoutgreenin",
        "lift",
        "gamma",
        "gain"]
        , properties)
    writer.write(f"{name}.enableEffects({enableEffects})")
    pop_and_set_property(writer, all_units, properties, unit_id, "temperature")
    pop_and_set_property(writer, all_units, properties, unit_id, "tint")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorR")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorG")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorB")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorA")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorH")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorS")
    pop_and_set_property(writer, all_units, properties, unit_id, "colorV")
    pop_and_set_property(writer, all_units, properties, unit_id, "contrast")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerRedOutRedIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerRedOutBlueIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerRedOutGreenIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerGreenOutRedIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerGreenOutBlueIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerGreenOutGreenIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerBlueOutRedIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerBlueOutBlueIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "mixerBlueOutGreenIn")
    pop_and_set_property(writer, all_units, properties, unit_id, "liftX")
    pop_and_set_property(writer, all_units, properties, unit_id, "liftY")
    pop_and_set_property(writer, all_units, properties, unit_id, "liftZ")
    pop_and_set_property(writer, all_units, properties, unit_id, "liftW")
    pop_and_set_property(writer, all_units, properties, unit_id, "gammaX")
    pop_and_set_property(writer, all_units, properties, unit_id, "gammaY")
    pop_and_set_property(writer, all_units, properties, unit_id, "gammaZ")
    pop_and_set_property(writer, all_units, properties, unit_id, "gammaW")
    pop_and_set_property(writer, all_units, properties, unit_id, "gainX")
    pop_and_set_property(writer, all_units, properties, unit_id, "gainY")
    pop_and_set_property(writer, all_units, properties, unit_id, "gainZ")
    pop_and_set_property(writer, all_units, properties, unit_id, "gainW")
    return name
