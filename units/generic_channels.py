from typing import TextIO
from . import add_deserializer, deserializer, deserialize, get_name

def generic_constructor(constructor: str):
    def wrap(writer:TextIO, all_units: list, unit_id: int, properties: list):
        name = get_name(unit_id)
        for i in range(len(properties)):
            v = properties[i]
            properties[i] = deserialize(writer, all_units, v)
        args = ",".join(properties)
        writer.write(f"local {name} = {constructor}({args})\n")
        return name
    return wrap


def generic_constructor_noref(constructor: str):
    def wrap(writer:TextIO, all_units: list, unit_id: int, properties: list):
        name = get_name(unit_id)
        args = ",".join([str(x) for x in properties])
        writer.write(f"local {name} = {constructor}({args})\n")
        return name
    return wrap

def generic_constructor_remap(constructor: str, mapping: dict):
    def wrap(writer:TextIO, all_units: list, unit_id: int, properties: list):
        name = get_name(unit_id)
        for i in range(len(properties)):
            v = properties[i]
            
            properties[i] = deserialize(writer, all_units, v)
        new_props = [None] * len(properties)
        for i,j in mapping.items():
            new_props[j] = properties[i]
        args = ",".join(new_props)
        writer.write(f"local {name} = {constructor}({args})\n")
        return name
    return wrap

def simple_ref(ref: str):
    def wrap(writer:TextIO, all_units: list, unit_id: int, properties: list):
        name = get_name(unit_id)
        writer.write(f"local {name} = {ref}\n")
        return name
    return wrap


add_deserializer("channel.clamp",generic_constructor("Channel.clamp"))
add_deserializer("channel.condition",generic_constructor("Channel.condition"))
add_deserializer("channel.exp",generic_constructor("Channel.exp"))
add_deserializer("channel.fft",generic_constructor("Channel.FFT"))
add_deserializer("channel.max",generic_constructor("Channel.max"))
add_deserializer("channel.min",generic_constructor("Channel.min"))
add_deserializer("channel.cos",generic_constructor_remap("Channel.cos", {0:0, 2:1, 3:2, 1:3}))
add_deserializer("channel.sine",generic_constructor_remap("Channel.sine", {0:0, 2:1, 3:2, 1:3}))
# add_deserializer("channel.random",generic_constructor("Channel.random"))
add_deserializer("channel.noise",generic_constructor_remap("Channel.noise", {0:1 ,1:2 ,2:3 ,3:4 ,4:0}))

add_deserializer("channel.context.droprate", simple_ref("Context.dropRate"))
add_deserializer("channel.context.globaloffset", simple_ref("Context.globalOffset"))
add_deserializer("channel.context.currentscore", simple_ref("Context.currentScore"))
add_deserializer("channel.context.currentcombo", simple_ref("Context.currentCombo"))
add_deserializer("channel.context.currenttiming", simple_ref("Context.currentTiming"))
add_deserializer("channel.context.screenwidth", simple_ref("Context.screenWidth"))
add_deserializer("channel.context.screenheight", simple_ref("Context.screenHeight"))
add_deserializer("channel.context.is16by9", simple_ref("Context.is16By9"))
add_deserializer("channel.context.bpm", generic_constructor_noref("Context.bpm"))
add_deserializer("channel.context.divisor", generic_constructor_noref("Context.divisor"))
add_deserializer("channel.context.floorposition", generic_constructor_noref("Context.floorPosition"))

add_deserializer("channel.trigger.accumulate", generic_constructor("TriggerChannel.accumulate"))
add_deserializer("channel.trigger.loop", generic_constructor("TriggerChannel.loop"))
add_deserializer("channel.trigger.stack", generic_constructor("TriggerChannel.stack"))
add_deserializer("channel.trigger.set", generic_constructor("TriggerChannel.setTo"))
