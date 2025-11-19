import heapq
import math

def process_sensor_data(raw_readings):
    # Normalize readings using floating point operations
    normalized = [math.sqrt(abs(x)) for x in raw_readings if x != 0]
    
    # Apply modular transformation
    mod_transformed = [(int(val * 10) % 17) for val in normalized]
    
    # Build max heap from transformed values
    max_heap = [-x for x in mod_transformed]
    heapq.heapify(max_heap)
    
    # Extract top 3 elements and compute aggregate
    top_elements = []
    for _ in range(min(3, len(max_heap))):
        top_elements.append(-heapq.heappop(max_heap))
    
    # Calculate signal strength using array operations
    signal_matrix = [[top_elements[i] * (i + 1) for i in range(len(top_elements))]]
    aggregated_strength = sum(signal_matrix[0])
    
    # Final modulation with floating point precision
    modulated_signal_strength = (aggregated_strength * 2.5) % 9.7
    
    return modulated_signal_strength

# Sensor readings from environmental monitoring system
sensor_readings = [16, -25, 0, 49, -64, 9, -4, 36]
result = process_sensor_data(sensor_readings)
print(f"Result: {result}")