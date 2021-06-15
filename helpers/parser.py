import argparse


ARGUMENTS = {
    "resize": {
        "--original": {
            "const": "original",
            "default": "original",
            "help": "images keep their original resolution (default)",
        },
        "--mode": {
            "const": "mode",
            "help": "resized to the most popular resolution",
        },
        "--smallest": {
            "const": "smallest",
            "help": "resized to the resolution of the smallest image",
        },
        "--largest": {
            "const": "largest",
            "help": "resized to the resolution of the largest image",
        },
        "--a4": {
            "const": "a4",
            "help": "resized to fit in an a4 sheet of paper",
        },
    },
    "order": {
        "--numerical": {
            "const": "numerical",
            "default": "numerical",
            "help": "ordered mathematically (default)",
        },
        "--alphabetical": {
            "const": "alphabetical",
            "help": "ordered alphabetically",
        },
        "--creation": {
            "const": "creation",
            "help": "ordered by date of creation",
        },
        "--accessed": {
            "const": "accessed",
            "help": "ordered by date of last access",
        },
    },
    "diretion": {
        "--ascending": {
            "const": "ascending",
            "default": "ascending",
            "help": "sorted from lowest to highest (default)",
        },
        "--descending": {
            "const": "descending",
            "help": "sorted from highest to lowest",
        },
    },
}


def main():
    parser = argparse.ArgumentParser(
        prog="cbPDF",
        description="Convert a folder or compressed archive containing images into a PDF",
        epilog="For a more thorough explanation with examples go to docs/help.md",
    )

    parser.add_argument("path", type=str, help="path to images")
    parser.add_argument(
        "-o",
        "--output",
        default="Output",
        help="path to output folder",
    )
    parser.add_argument(
        "-t",
        "--temp",
        default="Temp",
        help="path to temp folder",
    )
    parser.add_argument(
        "-i",
        "--info",
        action="store_true",
        help="show additional information when running",
    )

    # Arguments for resizing an image
    # variable is "resize", defaults to "original"
    resize_wrapper = parser.add_argument_group(
        "resize images", "how images should be resized when added to a pdf"
    )
    resize_group = resize_wrapper.add_mutually_exclusive_group()

    for arg, kwargs in ARGUMENTS["resize"].items():
        resize_group.add_argument(arg, action="store_const", dest="resize", **kwargs)

    # Arguments for ordering images
    # variable is "order", defaults to "numerical"
    order_wrapper = parser.add_argument_group(
        "image order", "how images are ordered when added to a pdf"
    )
    order_group = order_wrapper.add_mutually_exclusive_group()
    for arg, kwargs in ARGUMENTS["order"].items():
        order_group.add_argument(arg, action="store_const", dest="order", **kwargs)

    # variable is "direction", defaults to "ascending"
    direction_group = order_wrapper.add_mutually_exclusive_group()
    for arg, kwargs in ARGUMENTS["diretion"].items():
        direction_group.add_argument(
            arg, action="store_const", dest="direction", **kwargs
        )

    return parser.parse_args()
