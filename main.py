import argparse
import pathlib
import sys

# Variables
FILE_TYPES = [".cba", ".cbr", ".cbz", ".zip"]
TEMP_FOLDER = "Temp"

# argparse code
parser = argparse.ArgumentParser(
    prog="cbPDF",
    description="Convert a folder or compressed archive containing images into a PDF",
)

parser.add_argument("Path", metavar="path", type=str, help="path to images")

args = parser.parse_args()


# pathlib code

if not pathlib.Path(args.Path).exists():
    print("The path you entered does not exist.")
    sys.exit()


files = [file for file in pathlib.Path(args.Path).rglob("*")]
