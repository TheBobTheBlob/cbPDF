import json
import logging
import pathlib
import shutil
import sys


def sh_unpack(file, output, format):
    if (output / file.stem).exists():
        logging.error(f"A folder [{file.stem}] already exists in [{str(output)}]")
        sys.exit()

    logging.debug(f"Starting extract of [{str(file)}] into [{str(output)}]")
    shutil.unpack_archive(file, output / file.stem, format)
    logging.debug(f"Finished extract of [{str(file)}] into [{str(output)}]")


def image_locations(folder):
    for path in pathlib.rglob(folder):
        print(path)


# def config(source="config.json"):
#     with open(source) as file:
