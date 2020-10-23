# PDF Maker

PDF Maker takes cbr, cbz, and cba files and converts them into pdfs.

### Requirements

Python 3.6+

Standard modules:
* os
* pathlib

Other modules:
* pyunpack
* reportlab

### Setup

Create one text files, `folders.txt` in the same location as `main.py`.
Delete any `.keep` files.

### Usage

In `folders.txt`, have the folders containing all files to be made into pdfs on the first line and the folder for pdfs to be outputted to on the second line. 

```
Path to input directory
Path to output directory
```

Then run `main.py`.