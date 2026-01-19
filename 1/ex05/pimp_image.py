from numpy.typing import NDArray
from load_image import ft_load
import matplotlib.pyplot as plot
import numpy as np


def ft_red(array: NDArray) -> NDArray:
    """
    function to apply red filter
    """
    if array is None or array.size == 0 or array.ndim != 3:
        return array

    copy = array.copy()
    copy[:, :, 1] = 0
    copy[:, :, 2] = 0
    return copy


def ft_green(array: NDArray) -> NDArray:
    """
    function to apply green filter
    """
    if array is None or array.size == 0 or array.ndim != 3:
        return array

    copy = array.copy()
    copy[:, :, 0] = 0
    copy[:, :, 2] = 0
    return copy


def ft_blue(array: NDArray) -> NDArray:
    """
    function to apply blue filter
    """
    if array is None or array.size == 0 or array.ndim != 3:
        return array

    copy = array.copy()
    copy[:, :, 1] = 0
    copy[:, :, 0] = 0
    return copy


def ft_grey(array: NDArray) -> NDArray:
    """
    function to change colors to gray
    """
    if array.ndim == 2:
        return array

    copy = np.dot(array[..., :3], [0.2989, 0.5870, 0.114])
    return copy


def ft_invert(array: NDArray) -> NDArray:
    """
    function to apply color invert
    """
    copy = 255 - array
    return copy


def pimp_color(function, path: str) -> int:
    """
    loads the file from the specified path
    applies filter from provided function to image
    displays modified image
    """
    image = ft_load(path)
    if image.size == 0:
        print("Error loading file.")
        return 1

    if function is not None:
        edited = function(image)
    else:
        edited = image

    try:
        print(edited)
        if edited.ndim == 2:
            plot.imshow(edited, cmap="gray")
        else:
            plot.imshow(edited)
        plot.show()
    except Exception as e:
        print(f"Could not display image: {e}")

    return 0


def main(path: str) -> int:
    """
    a main which cycles through the functions that had to be programmed
    """
    try:
        print("ORIGINAL")
        pimp_color(None, path)
        print("RED")
        pimp_color(ft_red, path)
        print("GREEN")
        pimp_color(ft_green, path)
        print("BLUE")
        pimp_color(ft_blue, path)
        print("GREY")
        pimp_color(ft_grey, path)
        print("INVERT")
        pimp_color(ft_invert, path)
    except Exception as e:
        print("Error:", e)
        return 1

    return 0


if __name__ == "__main__":
    main("landscape.jpg")
    main("animal.jpeg")
    main("cover_icon.png")
