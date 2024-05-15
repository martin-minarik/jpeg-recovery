import itertools as it
from time import time
import sys

head = b"\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49\x46"
tail = b"\xff\xd9\x00\x00"

def main(filepath: str):
    print(f'Start searching for images in file "{filepath}"')
    time_start = time()
    # Load data
    with open(filepath, "rb") as input_file:
        data = input_file.read()
        data_size_mb = len(data) / (1024 * 1024)
    print(f"Size of file: {data_size_mb}MB")

    # Search for images
    for image_idx in it.count(1, step=1):
        start = data.find(head)
        end = data.find(tail)

        # Image not found in current subset
        if (start == -1) or (end == -1):
            break
        
        # Save Image
        filename = f"output-{image_idx}.jpg"
        print(f"Found {filename}")
        with open(filename, "wb") as output_file:
            output_file.write(data[start : end + 5])
        
        # Trim already searched data
        data = data[end + 5 :]

    # End
    elapsed_time = time() - time_start
    speed = data_size_mb / elapsed_time
    print(
        f"Found {image_idx-1} images in {round(elapsed_time, 3)}s, speed={round(speed, 2)} MB/s"
    )


if __name__ == "__main__":
    main(sys.argv[1])
