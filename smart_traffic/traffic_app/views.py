
from django.shortcuts import render
from .ai_models.car_detection import detect_cars
from .ai_models.traffic_signal_logic import control_traffic_signal

def index(request):
    if request.method == 'POST' and request.FILES['traffic_image']:
        # Save uploaded image
        image = request.FILES['traffic_image']
        image_path = f'traffic_app/static/images/{image.name}'
        with open(image_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)
        
        # Detect cars
        car_count, detected_image_path = detect_cars(image_path)
        
        # Control traffic signal
        lane1_cars = car_count
        lane2_cars = 5  # Simulated for now
        signal_status, recommendation = control_traffic_signal(lane1_cars, lane2_cars)
        
        context = {
            'car_count': car_count,
            'detected_image': detected_image_path,
            'signal_status': signal_status,
            'recommendation': recommendation,
        }
        return render(request, 'index.html', context)
    
    return render(request, 'index.html')

# Create your views here.
