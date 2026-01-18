from load_image import ft_load
import matplotlib.pyplot as plot


def zoom(path: str) -> int:
    image = ft_load(path)

    if image.size == 0:
        print("Error loading image. Program stops")
        return 1

    print(f"The image shape is: {image.shape}")

    image_zoomed = image[100:500, 450:850, 0:1]
    print(f"Shape after zooming: {image_zoomed.shape}")
    print(image_zoomed)

    try:
        plot.imshow(image_zoomed, cmap="grey")
        plot.show()
    except Exception as e:
        print(f"Could not display zoomed image: {e}")

    return 0


if __name__ == "__main__":
    zoom("animal.jpeg")
