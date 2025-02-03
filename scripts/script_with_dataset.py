import sys
from pathlib import Path


if __name__ == "__main__":
    # make sure we can use src
    p = str(Path("..").resolve().absolute())
    if p not in sys.path: sys.path.append(p)

    # define where we want the data to go
    root = Path("..").resolve().absolute()
    data_dir = root.joinpath("data")

    # download the dataset
    from src.utils import download_fashion_mnist
    dataset_dir = download_fashion_mnist(data_dir)

    # # create an interface for the dataset
    from src.datasets import FashionMnist
    dataset = FashionMnist(dataset_dir)
    
    # do something to the dataset... e.g. train a model, analyze the data, pre-process the data, etc.
    for idx, (img, lbl) in enumerate(dataset):
        print(f"{idx} has label {lbl} with img of shape {img.shape}")
