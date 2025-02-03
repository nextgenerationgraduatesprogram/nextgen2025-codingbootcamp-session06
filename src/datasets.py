import cv2
from pathlib import Path

from typing import *
from numpy import ndarray


class FashionMnist:
    def __init__(self, root: str, regex: Optional[str] = None) -> None:
        super(FashionMnist, self).__init__()
        self.root = Path(root).absolute().resolve()
        self.regex = "*" if regex is None else regex

        # validate the dataset exists
        assert self.root.exists, f"provided root doesn't exist"

    def __iter__(self) -> Tuple[Any, str]:
        # define an iterable for the samples in the dataset
        samples = Path(self.root).glob(self.regex)

        # iterate over the samples in our dataset
        for sample in samples:
            # construct the filepaths of the data
            img_filepath : Path = sample.joinpath("img.png")
            lbl_filepath : Path = sample.joinpath("label.txt")

            # read the data
            img : ndarray = self.read_image(img_filepath)
            lbl : int = self.read_label(lbl_filepath)

            # yield the data
            yield img, lbl

    def read_image(self, path: str) -> ndarray:
        img : ndarray = cv2.imread(path)
        return img

    def read_label(self, path: str) -> int:
        with open(path, "r") as file:
            data : int = int(file.read())
        return data