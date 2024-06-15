"""Convert colors to selected ones"""

import sys

import numpy as np
from PIL import Image
from loguru import logger

logger = logger.opt(colors=True)

pixel = tuple[int, int, int]


def get_closest_pixel(pool: list[pixel], given: pixel) -> pixel:
    """Pick the closest matching pixel to a given one,
    from the pool"""
    logger.trace("Given pixel <m>{}</>, pool <w>{}</>, finding closest..",
                 given, pool)

    # https://stackoverflow.com/questions/54242194/\
    # find-the-closest-color-to-a-color-from-given-list-of-colors
    colors = np.array(pool)
    color = np.array(given)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))

    choice = list(index_of_smallest[0])[0]
    return pool[choice]


def main(args: dict) -> None:
    """Process the image with all the given settings"""
    logger.info("Got settings: <w>{}</>", args)

    image = Image.open(args["image_path"]).convert("RGB")
    width, height = image.size

    # [TODO: maybe PIL already has a way to transform
    #  colors based on function?]
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            modified_pixel = get_closest_pixel(args["pool"], pixel)
            image.putpixel((x, y), modified_pixel)

    image.save(args.get("output_path", "output.png"))


def get_pool(pool_file: str) -> list[pixel]:
    """Get list of colors (for the pool) from a file"""
    logger.debug("Getting color pool from pool file")

    with open(pool_file, "r", encoding="UTF-8") as file:
        raw_colors = file.read().splitlines()

    return [tuple(map(int, x.split())) for x in raw_colors]


if __name__ == "__main__":
    logger.info("Starting the script..")

    output_path = None

    try:
        image_path = sys.argv[1]
        pool_path = sys.argv[2]
    except IndexError:
        logger.error("Please specify image and pool paths")
        sys.exit(1)

    pool = get_pool(pool_path)
    args = {
        "image_path": image_path,
        "pool": pool
    }
    if output_path:
        args.update({"output_path": output_path})
    
    main(args)
