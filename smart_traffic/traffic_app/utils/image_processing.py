import cv2

def preprocess_image(image_path):
    # Load and resize the image
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (500, 300))
    return resized_image