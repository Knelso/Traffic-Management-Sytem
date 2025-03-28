import cv2

def detect_cars(image_path):
    # Load pre-trained Haar Cascade model
    car_cascade = cv2.CascadeClassifier('traffic_app/ai_models/cars.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect cars
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Save the processed image
    output_path = 'traffic_app/static/images/detected_cars.jpg'
    cv2.imwrite(output_path, image)
    
    return len(cars), output_path