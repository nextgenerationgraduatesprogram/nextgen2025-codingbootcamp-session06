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

    # make sure we can use src
    p = str(Path("..").resolve().absolute())
    if p not in sys.path: sys.path.append(p)

    # download the dataset
    from src.utils import download_fashion_mnist
    dataset_dir = download_fashion_mnist(Path(args.root))

    # # create an interface for the dataset
    from src.datasets import FashionMnist
    dataset = FashionMnist(dataset_dir, args.regex)
    
    # do something to the dataset... e.g. train a model, analyze the data, pre-process the data, etc.
    for idx, (img, lbl) in enumerate(dataset):
        print(f"sample {idx} has label {lbl} with img of shape {img.shape}")

