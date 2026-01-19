import sys
from PIL import Image, UnidentifiedImageError
import numpy as np
from numpy.typing import NDArray


def ft_load(path: str) -> NDArray:
    try:
        # 'with' keyword - resource management: automatically handling setup
        # and cleanup, ensuring files or connections close safely
        # even if errors occur
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


def main():
    args = sys.argv[1:]

    try:
        match args:
            case [arg]:
                image = ft_load(arg)
                print(image)
            case _:
                raise ValueError("please provide image (jpg, jpeg, png, etc)")
    except ValueError as e:
        print("ValueError:", e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
