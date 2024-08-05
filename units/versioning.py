from typing import TextIO
from . import deserializer, deserialize, get_name, enable_feature, FEATURE_JUDGE_MANIPULATION

@deserializer(type_name="versioning")
def func(writer:TextIO, all_units: list, unit_id: int, properties: list):
    name = ""
    version = float(properties[0])
    if version >0:
        enable_feature(FEATURE_JUDGE_MANIPULATION)
    return name
