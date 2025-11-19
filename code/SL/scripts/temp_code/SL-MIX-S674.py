import heapq
import math
from collections import defaultdict

def process_sensor_data():
    # Simulated sensor readings (in microvolts)
    raw_readings = [1500, 2300, 950, 3400, 1800, 2750, 1200, 4100, 3200, 2100]
    
    # Apply logarithmic transformation to normalize high values
    log_scaled = [math.log10(reading) for reading in raw_readings if reading > 1000]
    
    # Initialize min-heap for tracking lowest 3 normalized values
    min_heap = []
    for value in log_scaled:
        heapq.heappush(min_heap, value)
        if len(min_heap) > 3:
            heapq.heappop(min_heap)
    
    # Calculate baseline from smallest values
    baseline = sum(min_heap) / len(min_heap)
    
    # Dictionary to track sensor anomalies
    anomaly_tracker = defaultdict(int)
    
    # Process for anomalies using ternary operator and short-circuit evaluation
    for idx, reading in enumerate(raw_readings):
        is_high_signal = reading > 3000
        is_low_signal = reading < 1000 and reading > 0
        
        # Short-circuit evaluation in anomaly condition
        if is_high_signal or (is_low_signal and reading % 2 == 0):
            # Ternary operator for anomaly severity
            severity = 2 if is_high_signal else (1 if is_low_signal else 0)
            anomaly_tracker[idx] = anomaly_tracker[idx] + severity
    
    # Calculate final anomaly score
    total_anomalies = sum(anomaly_tracker.values())
    final_anomaly_score = total_anomalies * math.exp(baseline) if total_anomalies > 0 else 0.0
    
    return final_anomaly_score

# Execute processing
final_anomaly_score = process_sensor_data()
print(f"Result: {final_anomaly_score:.6f}")