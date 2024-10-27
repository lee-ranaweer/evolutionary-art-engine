from display import display

def main():
    base_image_path = "images/original.jpg"
    suffixes = [
        "copy",
        "contrasted",
        "grayscaled",
        "disturbed",
        "single gray pixel",
        "single white pixel",
        "vehicle"
    ]

    for suffix in suffixes:
        img2_path = f"images/{suffix}.jpg"
        display(base_image_path, img2_path)

if __name__ == "__main__":
    main()