import logging
import pathlib
import sys

from helpers import files
from helpers import parser

# Variables
FILE_TYPES = [".cba", ".cbr", ".cbz", ".zip"]

args = parser.main()

if args.info:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
else:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


image_path = pathlib.Path(args.path)
output_path = pathlib.Path(args.output)
temp_path = pathlib.Path(args.temp)


if not image_path.exists():
    logging.error(f"[{args.path}] does not exist")
    sys.exit()

if not output_path.exists():
    logging.info(f"The output folder [{args.output}] does not exist, creating folder")
    output_path.mkdir(parents=True)

if not temp_path.exists():
    logging.info(f"The temp folder [{args.temp}] does not exist, creating folder")
    temp_path.mkdir(parents=True)


if image_path.is_dir():
    pass
elif image_path.suffix in [".zip", ".cbz"]:
    files.sh_unpack(image_path, temp_path, "zip")
elif image_path.suffix in [".tar", ".cbt"]:
    files.sh_unpack(image_path, temp_path, "tar")
