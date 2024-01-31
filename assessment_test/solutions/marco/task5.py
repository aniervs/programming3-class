import argparse
import re
import os

parser = argparse.ArgumentParser("task5.py")
parser.add_argument("directory")
parser.add_argument("-e", "--extension")
parser.add_argument("-n", "--name")
parser.add_argument("-s", "--size")
args = parser.parse_args()

for (dirpath, dirnames, filenames) in os.walk(args.directory):
    for filename in filenames:
        if args.extension != None:
            extension = filename.split(".")[-1]
            if extension != args.extension.strip("."):
                continue
        if args.name != None:
            name = filename.split(".")[0]
            if not re.match(args.name, name):
                continue
        file_path = dirpath.strip("/") + "/" + filename
        file_stats = os.stat(file_path)
        if args.size:
            if args.size[0] == "+":
                min_size = int(args.size[1:])
                if file_stats.st_size < min_size:
                    continue
            elif args.size[0] == "-":
                max_size = int(args.size[1:])
                if file_stats.st_size > max_size:
                    continue
        print(file_path)
