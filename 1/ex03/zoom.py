from load_image import ft_load
import matplotlib.pyplot as plot


def zoom(path: str) -> int:
    image = ft_load(path)

    if image.size == 0:
        print("Error loading image. Program stops")
        return 1

    print(f"The shape of image is: {image.shape}")
    print(image)

    image_zoomed = image[100:500, 450:850, 0:1]
    print(
        f"New shape after slicing: {image_zoomed.shape} or "
        f"({image_zoomed.shape[0]}, {image_zoomed.shape[1]})"
    )
    print(image_zoomed)

    try:
        plot.imshow(image_zoomed, cmap="grey")
        plot.show()
    except Exception as e:
        print(f"Could not display zoomed image: {e}")

    return 0


if __name__ == "__main__":
    zoom("animal.jpeg")
