from itertools import compress, count

def filter_anomalies(stream):
    # Identify positions where readings exceed dynamic threshold
    moving_avg = [sum(stream[i-2:i+1]) / 3 if i >= 2 else sum(stream[:i+1]) / (i+1) for i in range(len(stream))]
    thresholds = [avg * 1.5 for avg in moving_avg]
    anomalies_mask = [abs(value) > thresholds[i] for i, value in enumerate(stream)]
    
    # Misleading computation: entropy-like metric (not used in final result)
    zero_count = sum(1 for x in stream if x == 0)
    entropy_approx = zero_count / len(stream) if len(stream) else 0
    
    # Return filtered values using mask
    filtered = list(compress(stream, [not anomaly for anomaly in anomalies_mask]))
    return filtered if filtered else [0]

def process_readings(data):
    # Apply transformation pipeline
    squared = [x ** 2 for x in data]
    shifted = [val - 10 for val in squared]
    
    # Dead code path: this block is logically unreachable due to prior filtering
    if any(x < -100 for x in shifted):
        fallback = sum(abs(y) for y in shifted) // len(shifted)
        return fallback + 5000  # Distractor logic
    
    # Relevant computation: sum positive odd values
    positive_odds = [v for v in shifted if v > 0 and v % 2 == 1]
    aggregate = sum(positive_odds)
    
    # Extra state tracking (only some used)
    stats_tracker = {
        'count': len(positive_odds),
        'total_shift': sum(shifted),
        'raw_sum': sum(data)
    }
    
    # Final diagnostic based on aggregated transformed data
    adjustment_factor = 3
    final_diagnostic = aggregate * adjustment_factor - stats_tracker['count']
    return final_diagnostic

# Simulated sensor data stream
sensor_ids = ['S1', 'S2', 'S3']
sensor_stream = [-5, 3, 12, -1, 0, 8, 15, -3, 2, 9, 20]

# Auxiliary unused processing (distractor)
index_gen = count(start=1)
indexed_data = [(next(index_gen), val) for val in sensor_stream]
valid_tags = list(compress(sensor_ids, [val > 0 for val in sensor_stream[:3]]))

# Core execution chain
filtered_data = filter_anomalies(sensor_stream)
final_diagnostic = process_readings(filtered_data)
print(f"Result: {final_diagnostic}")