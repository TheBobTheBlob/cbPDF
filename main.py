import logging
import pathlib
import sys

from modules import files, parser

# from fpdf import FPDF


# Variables
# FILE_TYPES = [".cba", ".cbr", ".cbz", ".zip"]


args = parser.main()


# Sets debug level based on --info argument
if args.info:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
else:
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


input_path = pathlib.Path(args.path)
output_path = pathlib.Path(args.output)
temp_path = pathlib.Path(args.temp)


if not input_path.exists():
    logging.error(f"The input folder [{args.path}] does not exist")
    sys.exit()

if not output_path.exists():
    logging.info(f"The output folder [{args.output}] does not exist, creating folder")
    output_path.mkdir(parents=True)

if not temp_path.exists():
    logging.info(f"The temp folder [{args.temp}] does not exist, creating folder")
    temp_path.mkdir(parents=True)


if input_path.is_dir():
    pass
elif input_path.suffix in [".zip", ".cbz"]:
    files.sh_unpack(input_path, temp_path, "zip")
elif input_path.suffix in [".tar", ".cbt"]:
    files.sh_unpack(input_path, temp_path, "tar")

# files = [file for file in pathlib.Path(args.Path).rglob("*")]
# pdf = FPDF()
# for i in range(0, len(files) - 1):
#     pdf.add_page()
#     pdf.image(files[i])

# pdf.output("result.pdf")
