from collections import deque

def process_sensor_data(readings):
    window = deque(maxlen=5)
    peak_stack = []
    peak_count = 0
    
    for reading in readings:
        window.append(reading)
        
        if len(window) == 5:
            window_avg = sum(window) / len(window)
            
            # Check if current reading is a significant peak
            is_peak = reading > 2 * window_avg and reading == max(window)
            
            # Apply logical filtering for noise reduction
            not_noise = reading % 3 != 0 or (reading & 7) == 0
            
            if is_peak and not_noise:
                peak_stack.append(reading)
                peak_count += 1
    
    return peak_count

# Sensor readings from an environmental monitoring system
sensor_readings = [12, 45, 23, 67, 34, 89, 56, 78, 91, 25, 64, 87, 42, 58, 73]

peak_count = process_sensor_data(sensor_readings)
print(f"Result: {peak_count}")