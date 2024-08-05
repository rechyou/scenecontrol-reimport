import json
import sys
import units
from argparse import ArgumentParser

parser = ArgumentParser("scenecontrol-reimport")
parser.add_argument("input", help="Input sc json file")
parser.add_argument("output", nargs="?", default="-")

args = parser.parse_args()

sc = json.load(open(args.input))
writer = sys.stdout
if args.output != "-":
    writer = open(args.output, "w")
writer.write("-- this is the lua source --\n")
writer.write("--        or is it?       --\n")
for i in range(len(sc)):
    if not units.is_deserialized(i):
        units.deserialize(writer, sc, i)
