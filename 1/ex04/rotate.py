import sys
from load_image import ft_load
import matplotlib.pyplot as plot
import numpy as np


def rotate(path: str) -> int:
    """
    opens an image from path as array
    zooms in a square
    transposes it (looks like a rotation, but is a mirroring on the diagonal
    prints results and shows image
    """

    image = ft_load(path)

    if image.size == 0:
        print("Error loading image. Program stops")
        return 1

    image_zoomed = image[100:500, 450:850, 0:1]

    print(
        f"The shape of the image is: {image_zoomed.shape} or "
        f"({image_zoomed.shape[0]}, {image_zoomed.shape[1]})"
    )
    print(image_zoomed)

    height, width, channel = image_zoomed.shape
    new_image = np.zeros((width, height), dtype=image_zoomed.dtype)
    for y in range(height):
        for x in range(width):
            new_image[x][y] = image_zoomed[y][x][0]
    print(
        f"New shape after Transpose: "
        f"({new_image.shape[0]}, {image_zoomed.shape[1]})"
    )
    print(new_image)

    try:
        plot.imshow(new_image, cmap="grey")
        plot.show()
    except Exception as e:
        print(f"Could not display image: {e}")

    return 0


def main():
    try:
        rotate("animal.jpeg")
    except Exception as e:
        print("Error:", e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
