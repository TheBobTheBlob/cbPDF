iimport osimport pathlib

import pyunpack
import reportlab
import PyPDF4

# Variables
file_types = [".cba", ".cbr", ".cbz"]
temp_file = "unpacked"


# Gets folders from folders.txt and converts them into Path objects
with open("folders.txt") as file:
    lines = file.readlines()
    input_dir = pathlib.Path(lines[0].strip())
    output_dir = pathlib.Path(lines[1].strip())


# Gets all archives and adds their path to a list
print(f"Getting archives from {os.fspath(input_dir)}")
archives = []
for file in input_dir.glob("*"):
    if file.is_file() and file.suffix in file_types:
        archives.append(file)
print(f"Found {len(archives)} archives\n")


os.mkdir(temp_file)

finished = 1
for file in archives:
    print(f"{finished}/{len(archives)} Extracting {file.name}")
    pyunpack.Archive(file).extractall(temp_file)
    finished += 1

