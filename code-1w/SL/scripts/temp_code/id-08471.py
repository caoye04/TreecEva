from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and redundant readings
def generate_noisy_data():
    base_values = [3.5, 4.2, 2.8, 5.1, 3.9]
    noise_offsets = [0.1, -0.2, 0.3, -0.1, 0.0]
    readings = defaultdict(float)
    
    for i, val in enumerate(base_values):
        readings[f'sensor_{i+1}_raw'] = val
        readings[f'sensor_{i+1}_adj'] = val + noise_offsets[i]
        readings[f'sensor_{i+1}_valid'] = True

    # Irrelevant derived stats
    avg_raw = sum(readings[f'sensor_{i+1}_raw'] for i in range(5)) / 5
    readings['average_raw'] = avg_raw
    readings['deviation_flag'] = False

    return readings

def analyze_readings(data):
    anomalies = 0
    adjusted_sum = 0.0
    
    for i in range(5):
        raw = data[f'sensor_{i+1}_raw']
        adj = data[f'sensor_{i+1}_adj']
        diff = abs(adj - raw)
        
        if diff > 0.25:
            anomalies += 1
        
        # Only raw values contribute to final calculation
        adjusted_sum += raw * (1 + 0.1 * (i % 2))  # alternating scaling
    
    # Dead code: this block is never executed due to fixed condition
    if anomalies > 10:
        backup_mode = True
        adjusted_sum *= 0.9

    return adjusted_sum, anomalies

def compute_weighted_average(values, weights):
    # Unused helper function - red herring
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def compute_final_score(data, weights):
    # Extract raw sensor values
    raw_values = [data[f'sensor_{i+1}_raw'] for i in range(5)]
    
    # Compute transformed values using non-linear adjustment
    transformed = []
    for i, v in enumerate(raw_values):
        temp = v ** 2 if i % 2 == 0 else v ** 0.5
        transformed.append(round(temp, 3))
    
    # Use only first three transformed values for score
    partial_sum = sum(transformed[:3])
    
    # Secondary processing path with distractor logic
    pair_sums = []
    for a, b in combinations(transformed, 2):
        pair_sums.append(a + b)
    
    top_pairs = sorted(pair_sums, reverse=True)[:3]
    bonus_component = sum(top_pairs) * 0.05  # Minor influence but not used
    
    # Final score depends only on partial_sum and fixed offset
    score = int(partial_sum + 7.25)
    
    # Spurious assignment - looks important but unused
    data['diagnostic_code'] = 'OK'
    data['last_calibrated'] = '2023-12-01'
    
    return score

# Main execution
sensor_data = generate_noisy_data()
weights = [0.2, 0.15, 0.3, 0.25, 0.1]  # Unused in actual logic

intermediate_total, detected_anomalies = analyze_readings(sensor_data)

# Key computation step
final_score = compute_final_score(sensor_data, weights)

print(f"Result: {final_score}")