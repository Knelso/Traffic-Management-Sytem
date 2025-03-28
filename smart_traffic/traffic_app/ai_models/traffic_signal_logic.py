def control_traffic_signal(car_count_lane1, car_count_lane2):
    if car_count_lane1 > car_count_lane2:
        return "Lane 1: Green, Lane 2: Red", "Redirect cars to Lane 2"
    else:
        return "Lane 1: Red, Lane 2: Green", "Redirect cars to Lane 1"