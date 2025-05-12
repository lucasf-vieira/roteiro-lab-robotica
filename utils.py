import cv2


def flip_and_show_image(image_name, image):
    image = cv2.flip(image, 1)
    cv2.imshow(image_name, image)
    return cv2.waitKey(1)
