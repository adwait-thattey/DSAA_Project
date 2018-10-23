import cv2


def convert_to_edges(incoming_image, lower_threshold=100, upper_threshold=200):
    edge_image = cv2.Canny(incoming_image, threshold1=100, threshold2=200)

    return edge_image


def count_white_pixels(incoming_edge_image):
    return cv2.countNonZero(incoming_edge_image)


def get_ratio(img):
    edge_image = convert_to_edges(img)
    w_px = count_white_pixels(edge_image)

    img_ht, img_width = img.shape[:2]
    tot_px = img_ht * img_width

    ratio = tot_px/w_px

    return ratio