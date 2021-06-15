import logging
import pathlib
import sys

from helpers import parser

# Variables
FILE_TYPES = [".cba", ".cbr", ".cbz", ".zip"]

args = parser.main()

if args.info:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
else:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


if not pathlib.Path(args.path).exists():
    logging.error(f"{args.path} does not exist")
    sys.exit()

if not pathlib.Path(args.output).exists():
    logging.warning(f"{args.output} does not exist, creating folder")
    pathlib.Path(args.output).mkdir(parents=True)

if not pathlib.Path(args.temp).exists():
    logging.warning(f"{args.temp} does not exist, creating folder")
    pathlib.Path(args.temp).mkdir(parents=True)
