from itertools import combinations, cycle

# Simulate a data stream from sensor readings with noise filtering
def preprocess_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]  # Normalize to 0-1 range
    smoothed = []
    window = []
    for val in normalized:
        window.append(val)
        if len(window) > 3:
            window.pop(0)
        smoothed.append(sum(window) / len(window))
    return smoothed

# Analyze patterns in the data using sliding windows and combinatorial pairs
def detect_anomaly_patterns(values):
    anomalies = 0
    for i in range(len(values) - 4):
        segment = values[i:i+5]
        avg = sum(segment) / len(segment)
        variance = sum((x - avg) ** 2 for x in segment) / len(segment)
        if variance > 0.1:
            # Check all pairs in this segment for high divergence
            for a, b in combinations(segment, 2):
                if abs(a - b) > 0.5:
                    anomalies += 1
    return anomalies

# Misleading helper: computes unrelated statistical moment (not used in final score)
def compute_kurtosis_like(values):
    if len(values) == 0:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    if variance == 0:
        return 0.0
    kurtosis = sum((x - mean_val) ** 4 for x in values) / (len(values) * variance ** 2)
    return kurtosis

# Core scoring logic combining multiple factors
def calculate_final_score(data_stream):
    preprocessed = preprocess_sensor_data(data_stream)
    
    # Distractor: unused intermediate calculation
    cyclic_iter = cycle([1, 2, 3])
    pseudo_enriched = [a + next(cyclic_iter) for a in preprocessed[:10]]
    
    # Actual signal strength metric
    signal_energy = sum(x * x for x in preprocessed)
    
    # Pattern complexity measure
    pattern_richness = detect_anomaly_patterns(preprocessed)
    
    # Dummy state tracking with no impact
    state_log = []
    for i, val in enumerate(preprocessed):
        if val > 0.7:
            state_log.append((i, 'HIGH'))
        elif val < 0.3:
            state_log.append((i, 'LOW'))
    
    # Weighted combination forming the final score
    base_score = signal_energy * 100
    adjustment = pattern_richness * 5
    final_score = int(base_score - adjustment)  # Integer output for stability
    
    # Red herring: modifying unrelated list
    temp_grid = [[0]*5 for _ in range(5)]
    for r in range(5):
        for c in range(5):
            temp_grid[r][c] = r * c + 2
    
    return final_score

# Main execution
if __name__ == '__main__':
    raw_sensor_data = [5, 15, 25, 95, 105, 45, 60, 88, 92, 30, 20, 12, 99, 50]
    final_score = calculate_final_score(raw_sensor_data)
    print(f"Target result: {final_score}")