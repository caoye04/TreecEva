import itertools

# System health monitoring simulation with redacted processing paths
def collect_telemetry():
    raw_samples = [18, 22, 19, 25, 21, 17, 24]
    offset = 3
    adjusted = [x + offset for x in raw_samples]
    return adjusted

def generate_sequence(n):
    # Irrelevant Fibonacci-like sequence generator (dead path)
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def filter_outliers(data, threshold=20):
    # Misleading filter that isn't actually used later
    return [x for x in data if x <= threshold]

def rolling_average(values, window=3):
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages

def compress_data(stream):
    # Unused compression heuristic
    return [stream[i] for i in range(0, len(stream), 2)]

def accumulate_diagnostics(logs):
    # Complex but partially irrelevant accumulation
    base_score = 0
    penalty = 0
    for entry in logs:
        if entry > 22:
            base_score += entry * 0.5
        elif entry < 19:
            penalty += 1
    return base_score - (penalty * 1.5)

def validate_timing_integrity(timestamps):
    # Decoy validation function never called
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    return all(d > 0 for d in diffs)

def extract_metadata(config_blob):
    # Dead code path simulating config parsing
    metadata = {}
    for line in config_blob.split('\n'):
        if '=' in line:
            k, v = line.strip().split('=', 1)
            metadata[k] = v
    return metadata

def main_processing_pipeline():
    # Real signal in a noisy context
    sensor_readings = collect_telemetry()  # [21, 25, 22, 28, 24, 20, 27]

    # Distractor: unused filtering and transformation
    clean_data = filter_outliers(sensor_readings, threshold=23)
    compressed = compress_data(sensor_readings)

    # Relevant: compute rolling behavior
    moving_avg = rolling_average(sensor_readings, window=3)  # [22.0, 25.0, 23.333..., 24.0, 23.666...]

    # Simulated timing log with meaningful values
    timing_log = [12, 15, 14, 18, 16]
    timing_log = [t * 1.1 for t in timing_log]  # Apply scaling: [13.2, 16.5, 15.4, 19.8, 17.6]
    timing_log = [round(t, 1) for t in timing_log]

    # Diagnostic flags with decoy logic
    status_flags = {k: False for k in ['f1', 'f2', 'f3', 'f4']}
    temp_burst = [25, 22, 28]
    flag_scores = list(map(lambda x: x ** 0.5, temp_burst))  # [5.0, ~4.69, ~5.29]

    # Unused advanced analysis
    combinations = list(itertools.combinations([1, 2, 3, 4], 2))
    permutations = list(itertools.permutations(['a', 'b'], 2))

    # Real diagnostic computation chain
    avg_magnitude = sum(moving_avg) / len(moving_avg)  # ~23.6
    adjustment_factor = len(combinations) * 0.2  # 6 * 0.2 = 1.2

    # Critical intermediate (misleading)
    preliminary_index = avg_magnitude - adjustment_factor  # ~22.4

    # Another distraction
    metadata_str = "version=2.1\ndebug=false\noptimized=true"
    cfg = extract_metadata(metadata_str)

    # Real dependency: diagnostics built from multiple sources
    diagnostics = {
        'base': accumulate_diagnostics(sensor_readings),
        'peaks': len([x for x in sensor_readings if x >= 25]),
        'stability': preliminary_index,
        'noise_floor': sum(1 for x in flag_scores if x > 4.5)  # 3
    }

    # Key statement - this is where the answer comes from
    final_diagnostic = aggregate_metrics(timing_log, diagnostics)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

def aggregate_metrics(times, metrics):
    # Core metric integration with subtle arithmetic
    time_component = sum(t for t in times if t > 15)  # 16.5 + 15.4 + 19.8 + 17.6 = 69.3
    base_component = metrics['base']  # (25*0.5 + 28*0.5 + 27*0.5) - (2 * 1.5) = (12.5+14+13.5) - 3 = 37
    peak_bonus = metrics['peaks'] * 2.5  # 3 * 2.5 = 7.5
    stability_penalty = 10 - metrics['stability']  # 10 - 22.4 = -12.4
    noise_weight = metrics['noise_floor'] * 1.1  # 3 * 1.1 = 3.3

    # Final deterministic calculation
    result = time_component + base_component + peak_bonus + stability_penalty + noise_weight
    # 69.3 + 37 + 7.5 - 12.4 + 3.3 = 104.7
    return round(result, 6)

# Orchestration
if __name__ == '__main__':
    final_diagnostic = main_processing_pipeline()
