import sys
import argparse
from pathlib import Path


if __name__ == "__main__":
    # define an argument parser
    parser = argparse.ArgumentParser(
        description="Downloads and processes the FashionMNIST dataset.",
        epilog="Please contact sam.cantrill@data61.csiro.au for further help."
    )
    parser.add_argument("--root",
        required=True,
        type=str,
        help="Root directory to store the dataset into."
    )
    parser.add_argument("--regex",
        required=False,
        type=str,
        default="*",
        help="Regular expression to use for matching samples in the dataset."
    )

    # parse the system arguments
    args, unknown_args = parser.parse_known_args(sys.argv)


    print(f"Arguments: {args}")
    print(f"Unhandled Arguments: {unknown_args}")
