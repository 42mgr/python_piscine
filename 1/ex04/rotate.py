from load_image import ft_load
import matplotlib.pyplot as plot
import numpy as np


def rotate(path: str) -> int:
    image = ft_load(path)

    if image.size == 0:
        print("Error loading image. Program stops")
        return 1

    image_zoomed = image[100:500, 450:850, 0:1]
    print(f"Shape: {image_zoomed.shape}")
    print(image_zoomed)

    image_trans = np.copy(image_zoomed)

    column = 0
    row = 0

    for x in image_zoomed:
        for y in x:
            image_trans[row][column] = y
            row += 1
        row = 0
        column += 1

    try:
        plot.imshow(image_trans, cmap="grey")
        plot.show()
    except Exception as e:
        print(f"Could not display image: {e}")

    return 0


if __name__ == "__main__":
    rotate("animal.jpeg")
