from PIL import Image, UnidentifiedImageError
import numpy as np
from numpy.typing import NDArray


def ft_load(path: str) -> NDArray:
    try:
        with Image.open(path) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")
            image_array = np.array(img)
            print(f"The shape of the image is: {image_array.shape}")

            return image_array
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        print("Error: File not found or cannot be opened")
        return np.array([])
    except UnidentifiedImageError:
        print("Error: unidentified image error")
        return np.array([])
    except Exception as e:
        print(f"An unexpected error happened: {e}")
        return np.array([])


if __name__ == "__main__":
    image = ft_load("landscape.jpg")
    image = ft_load("error")
