from itertools import combinations
from functools import reduce

# Simulate sensor data processing with diagnostic logic
def analyze_readings(readings):
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    adjusted_scores = [x * 0.9 + baseline * 0.1 for x in readings]
    
    # Irrelevant transformation (distractor)
    normalized = [max(0, min(100, (x - baseline) * 10)) for x in readings]
    
    return adjusted_scores, variance

# Misleading auxiliary function that computes unused stats
def compute_rolling_average(data, window=3):
    rolling = []
    for i in range(len(data) - window + 1):
        rolling.append(sum(data[i:i+window]) / window)
    return rolling

# Core aggregation logic
def aggregate_metrics(trends, thresholds):
    trend_values = list(trends.values())
    flat_trends = [item for sublist in trend_values for item in sublist]
    
    # Key computation: weighted harmonic mean if above threshold, else skip
    valid_entries = []
    for key, values in trends.items():
        thresh = thresholds.get(key, 10)
        valid_entries.extend([v for v in values if v > thresh])
    
    if not valid_entries:
        return 0
    
    # Use lambda and reduce for harmonic mean
    harmonic_func = lambda acc, x: acc + (1 / x)
    inverse_sum = reduce(harmonic_func, valid_entries, 0)
    harmonic_mean = len(valid_entries) / inverse_sum
    
    # Secondary metric: count of high-magnitude fluctuations (distractor)
    magnitude_spikes = sum(1 for v in flat_trends if abs(v) > 25)
    spike_ratio = magnitude_spikes / len(flat_trends) if flat_trends else 0
    
    # Final diagnostic based only on harmonic mean
    final_score = int(harmonic_mean * 100)
    
    return final_score

# Main execution
if __name__ == "__main__":
    # Simulated multi-sensor input (temperature, pressure, flow_rate)
    sensor_input = {
        'temp': [15.2, 18.7, 22.1, 24.3, 26.8],
        'pressure': [8.5, 9.1, 10.3, 12.4, 14.2, 16.0],
        'flow_rate': [5.0, 7.2, 6.8, 8.1, 9.3]
    }

    # Thresholds for filtering significant readings
    threshold_map = {
        'temp': 20.0,
        'pressure': 10.0,
        'flow_rate': 7.0
    }

    # Preprocess each sensor stream
    processed_data = {}
    for k, v in sensor_input.items():
        adjusted, var = analyze_readings(v)
        processed_data[k] = adjusted
    
    # Generate irrelevant combinatorial analysis (distractor)
    temp_pairs = list(combinations(sensor_input['temp'], 2))
    high_diff_pairs = [pair for pair in temp_pairs if abs(pair[0] - pair[1]) > 5]
    
    # Rolling stats on original data (dead path)
    pressure_rolling = compute_rolling_average(sensor_input['pressure'])
    
    # Core assignment
    trend_data = processed_data
    final_diagnostic = aggregate_metrics(trend_data, threshold_map)
    
    # Print result
    print(f"Result: {final_diagnostic}")