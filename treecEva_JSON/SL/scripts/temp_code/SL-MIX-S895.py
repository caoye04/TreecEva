import heapq
import math

def process_sensor_data(readings):
    # Convert readings to log scale and store with their original indices
    log_scaled = [(math.log(r + 1), i) for i, r in enumerate(readings) if r > 0]
    
    # Create a max heap using negative values
    max_heap = [(-log_val, idx) for log_val, idx in log_scaled]
    heapq.heapify(max_heap)
    
    # Transformation keys encoded as strings
    transform_keys = ["EXP", "SQRT", "LOG", "SQUARE"]
    
    modulated_output = 0
    
    # Process top 3 values from heap
    for _ in range(min(3, len(max_heap))):
        neg_log_val, idx = heapq.heappop(max_heap)
        log_val = -neg_log_val
        original_val = readings[idx]
        
        # Apply transformation based on index
        key = transform_keys[idx % len(transform_keys)]
        if key == "EXP":
            transformed = math.exp(log_val)
        elif key == "SQRT":
            transformed = math.sqrt(original_val)
        elif key == "LOG":
            transformed = math.log(original_val + 1)
        else:  # SQUARE
            transformed = original_val ** 2
        
        modulated_output += int(transformed)
    
    return modulated_output

# Sensor readings from an environmental monitoring system
sensor_readings = [10, 100, 3, 50, 7]
final_result = process_sensor_data(sensor_readings)
print(f"Result: {final_result}")