import logging
import shutil
import sys


def sh_unpack(file, output, format):
    if (output / file.stem).exists():
        logging.error(f"A folder [{file.stem}] already exists in [{str(output)}]")
        sys.exit()

    logging.debug(f"Starting extract of [{str(file)}] into [{str(output)}]")
    shutil.unpack_archive(file, output / file.stem, format)
    logging.debug(f"Finished extract of [{str(file)}] into [{str(output)}]")
