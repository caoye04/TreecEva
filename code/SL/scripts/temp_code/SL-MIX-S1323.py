from collections import defaultdict
import math

def analyze_wildlife_activity(sensor_log):
    # Process raw sensor data using dictionary comprehension
    hourly_activations = defaultdict(int)
    for timestamp, intensity in sensor_log:
        hour = timestamp // 100  # Extract hour from HHMM format
        hourly_activations[hour] += intensity if intensity > 0 else 0
    
    # Apply greedy selection for peak activity window (3 consecutive hours)
    max_activity = 0
    peak_activity_count = 0
    
    hours_list = sorted(hourly_activations.keys())
    for i in range(len(hours_list) - 2):
        # Short-circuit evaluation to ensure consecutive hours
        if (hours_list[i+1] == hours_list[i] + 1 and 
            hours_list[i+2] == hours_list[i] + 2):
            window_total = sum(hourly_activations[h] for h in hours_list[i:i+3])
            # Logical operations to update peak
            if window_total > max_activity and window_total >= 15:
                max_activity = window_total
                peak_activity_count += 1  # Count valid peak windows
    
    return peak_activity_count

# Lambda function for data transformation
transform_reading = lambda x: (x[0], round(math.sqrt(x[1]) * 2) if x[1] > 0 else 0)

# Context manager for processing pipeline
class SensorPipeline:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.processed_data = []
    
    def __enter__(self):
        # Apply transformation to all readings
        self.processed_data = [transform_reading(reading) for reading in self.raw_data]
        return self.processed_data
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Raw sensor data: (timestamp in HHMM, activation_intensity)
raw_sensor_readings = [
    (905, 16), (915, 25), (930, 9),
    (1002, 36), (1020, 49), (1045, 64),
    (1110, 1), (1130, 4), (1150, 16),
    (1420, 25), (1435, 36), (1450, 9)
]

# Execute analysis using context manager
with SensorPipeline(raw_sensor_readings) as processed_readings:
    peak_activity_count = analyze_wildlife_activity(processed_readings)

print(f"Result: {peak_activity_count}")