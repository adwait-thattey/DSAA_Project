import check_section


def crop_section(img_arr, x1, y1, x2, y2):
    section = img_arr[y1:y2, x1:x2]
    return section


def read_image(img):
    return check_section.cv2.imread(img, check_section.cv2.IMREAD_GRAYSCALE)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise AttributeError("Please pass the name of image as input")

    img_path = sys.argv[1]

    img = read_image(img_path)

    # img_sec = crop_section(img, 480, 150, 700, 450)

    print(check_section.get_ratio(img))
