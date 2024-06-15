"""Convert colors to selected ones"""

import sys

from PIL import Image
from loguru import logger

logger = logger.opt(colors=True)

pixel = tuple[int, int, int]


def get_closest_pixel(pool: list[pixel], given: pixel) -> pixel:
    """Pick the closest matching pixel to a given one,
    from the pool"""
    logger.trace("Given pixel <m>{}</>, pool <w>{}</>, finding closest..",
                 given, pool)

    return (0, 0, 0)


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


if __name__ == "__main__":
    logger.info("Starting the script..")

    output_path = None

    try:
        image_path = sys.argv[1]
    except IndexError:
        logger.error("Please specify image path, i.e. `py main.py image.png`")
        sys.exit(1)

    args = {
        "image_path": image_path,
        "pool": [1, 2]
    }
    if output_path:
        args.update({"output_path": output_path})
    
    main(args)
