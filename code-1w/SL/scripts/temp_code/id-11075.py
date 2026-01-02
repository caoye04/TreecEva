import itertools
import math

def analyze_turbine_health(sensor_readings, threshold_map):
    # Irrelevant helper: computes entropy (not used in final result)
    def compute_entropy(data):
        total = sum(data)
        return sum(- (x / total) * math.log2(x / total) for x in data if x > 0)

    # Distractor: complex transformation not contributing to answer
    normalized = [max(0, x - threshold_map['noise_floor']) for x in sensor_readings]
    filtered = list(itertools.filterfalse(lambda x: x < threshold_map['min_signal'], normalized))
    
    # Dead code path: never executed due to condition
    if len(filtered) > 1000:
        smoothed = [sum(filtered[i:i+5]) / 5 for i in range(len(filtered) - 4)]
    else:
        smoothed = filtered  # This runs, but value gets overridden later

    # Misleading intermediate: looks important but unused
    peak_magnitude = max(smoothed) if smoothed else 0
    decay_rate = math.exp(-0.1 * len(smoothed))

    # Actual relevant logic buried here
    raw_energy = sum(x ** 2 for x in sensor_readings if x > 0)
    cycle_count = len([x for x in sensor_readings if x % 100 == 0 and x > 0])
    return raw_energy // (cycle_count + 1)  # Avoids division by zero


def validate_calibration(sequence):
    # Decoy function with heavy computation but no impact
    permutations = itertools.permutations(sequence[:4])
    valid_perms = 0
    for p in permutations:
        if sum(p) % 2 == 0 and p[0] > p[-1]:
            valid_perms += 1
    return valid_perms * 17  # Red herring result


def generate_benchmark(signal_length, base_freq):
    # Generates synthetic signal (partially relevant)
    t = range(signal_length)
    benchmark_wave = [int(50 * math.sin(base_freq * 2 * math.pi * i / 100)) for i in t]
    
    # Adds interference components
    noise_layer = [i % 13 for i in t]
    corrupted = [a + b for a, b in zip(benchmark_wave, noise_layer)]
    
    # Only this portion contributes to final output
    clean_energy = sum(x for x in benchmark_wave if x > 0)
    return clean_energy


def aggregate_metrics(data_package, calib_seq):
    # Key distractors
    audit_trace = []
    debug_mode = False
    
    # Unused complex unpacking
    (*primary_channels, secondary, tertiary) = data_package['channels']
    config_meta = {**data_package['config'], 'version': '3.7'}

    # Spurious transformation chain
    temp_snapshot = [
        (idx, val, math.atan(val / (idx + 1))) 
        for idx, val in enumerate(data_package['readings'])
        if val % 2 == 0
    ]
    
    # Fake dependency on validation (result ignored)
    _ = validate_calibration(calib_seq)
    
    # Real computation hidden among distractions
    base_health = analyze_turbine_health(data_package['readings'], data_package['thresholds'])
    benchmark_score = generate_benchmark(200, 0.25)
    
    # Critical logic step 1: combinatorial adjustment
    combinations = list(itertools.combinations(calib_seq[1:6], 3))
    combo_adjust = len(combinations) // 2
    
    # Critical logic step 2: integer division and rounding behavior
    intermediate = (base_health + benchmark_score) // 10
    
    # Critical logic step 3: final combination
    final_diagnostic = intermediate - combo_adjust
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution setup
if __name__ == "__main__":
    turbine_data = {
        'readings': [150, 200, 100, 350, 400, 50, 250, 300, 450, 500],
        'channels': [1, 2, 3, 4, 5],
        'thresholds': {'min_signal': 75, 'noise_floor': 25},
        'config': {'gain': 1.5}
    }
    calibration_sequence = [8, 6, 4, 2, 10, 12, 14]
    
    # Trigger execution
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)