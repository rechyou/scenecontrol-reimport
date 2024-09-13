from typing import TextIO
import pkgutil
import sys
import string
import random
from import_submodules import import_submodules


UNIT_DESERIALIZERS = {}

deserialized = {}

features = []

FEATURE_JUDGE_MANIPULATION = "JUDGE_MANIPULATION"

def get_name(index):
    random.seed(index)
    new_id = hex(random.randint(0, 2**32)).lstrip('0x').rjust(8, "0").upper()
    return f"_x{index}"


def deserializer(type_name):
    def wrap(func):
        UNIT_DESERIALIZERS[type_name] = func
    return wrap

def add_deserializer(type_name, func):
    sys.stderr.write(f"new deserializer: {type_name}\n")
    UNIT_DESERIALIZERS[type_name] = func

def is_deserialized(unit_id):
    return unit_id in deserialized

def deserialize(writer:TextIO, all_units: list, unit_id: int):
    if unit_id is None:
        return "nil"
    properties = all_units[unit_id]["Properties"]
    if unit_id in deserialized:
        return deserialized[unit_id]
    # deserialized[unit_id] = True
    unit_type = all_units[unit_id]["Type"]
    unit_type = unit_type.removeprefix("$")
    unit_type_sub = unit_type.split(".")[0]
    if unit_type in UNIT_DESERIALIZERS:
        name = UNIT_DESERIALIZERS[unit_type](writer, all_units, unit_id, properties)
        deserialized[unit_id] = name
        return name
    if unit_type_sub in UNIT_DESERIALIZERS:
        name = UNIT_DESERIALIZERS[unit_type_sub](writer, all_units, unit_id, properties)
        deserialized[unit_id] = name
        return name
    else:
        name = get_name(unit_id)
        sys.stderr.write(f"WARNING: Unknown unit type: {unit_type} of ID {unit_id}\n")
        writer.write(f"{name} = nil -- UNKNOWN UNIT TYPE: {unit_type} of ID {unit_id}\n")
        deserialized[unit_id] = name
        return name

def enable_feature(feature: str):
    global features
    sys.stderr.write(f"Feature enabled: {feature}\n")
    features.append(feature)

def has_feature(feature:str):
    return feature in features

def is_clone(unit_type: str):
    return unit_type.startswith("$")

def pop_and_set_property(writer:TextIO, all_units: list, properties: list, parent_id: int, property_name: str):
    unit = deserialize(writer, all_units, properties.pop(0))
    parent_name = get_name(parent_id)
    writer.write(f"{parent_name}.{property_name} = {unit}\n")

def pop_and_set_property_raw(writer:TextIO, all_units: list, properties: list, parent_id: int, property_name: str):
    unit = properties.pop(0)
    if type(unit) == bool:
        unit = "true" if unit else "false"
    parent_name = get_name(parent_id)
    writer.write(f"{parent_name}.{property_name} = {unit}\n")


def pop_and_call_raw(writer:TextIO, all_units: list, properties: list, parent_id: int, method: str):
    unit = properties.pop(0)
    if type(unit) == bool:
        unit = "true" if unit else "false"
    parent_name = get_name(parent_id)
    writer.write(f"{parent_name}.{method}({unit})\n")

import_submodules("units.channels")
import_submodules("units.triggers")
import_submodules("units.controllers")
import_submodules("units.postprocessing")
import_submodules("units")
