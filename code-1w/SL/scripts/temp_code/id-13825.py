from collections import defaultdict, Counter
import math

def collect_sensor_data():
    # Simulated sensor readings (some relevant, some red herrings)
    raw_data = [127, 255, 64, 192, 32, 168, 96, 144]
    return raw_data

def filter_noise(data):
    # Real preprocessing: isolate high-magnitude signals
    filtered = [x for x in data if x > 100]
    normalization_factor = 1.5  # Distractor: not actually used
    enhanced = [x * 0.9 for x in filtered]  # Minor adjustment
    return enhanced

def extract_patterns(signal_list):
    pattern_map = defaultdict(int)
    temp_counter = 0
    for val in signal_list:
        if val & 128:  # Checks if high bit is set (bit manipulation)
            pattern_map['high_bit_set'] += 1
        if val % 2 == 0:
            pattern_map['even'] += 1
    # Irrelevant transformation
    squared_sums = sum(x**2 for x in signal_list)  # Dead-end computation
    return pattern_map

def derive_metrics(patterns):
    # Only 'high_bit_set' is used later; 'even' is a distractor
    base_score = patterns['high_bit_set'] * 100
    penalty = patterns.get('even', 0) * 5  # Misleading: looks important
    adjusted = base_score - penalty
    if adjusted < 50:
        adjusted = 50
    return adjusted

def simulate_failure_modes(metrics_value):
    # Decoy function: appears related but unused
    modes = ['overheat', 'sync_loss', 'noise_spike']
    log_entry = f"Simulating {len(modes)} failure modes with seed {metrics_value}"
    simulation_result = [math.sin(metrics_value + i) for i in range(3)]
    return simulation_result

def validate_consistency(data):
    # Unused validation logic (dead code path)
    if len(data) < 4:
        return False
    sorted_data = sorted(data)
    return all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))

def generate_diagnostics(score):
    # Complex-looking but ultimately irrelevant diagnostic string generation
    diagnosis_code = ''
    temp_val = score
    while temp_val > 0:
        diagnosis_code += chr(65 + (temp_val % 26))
        temp_val //= 26
    # Returns unused metadata
    return {'code': diagnosis_code, 'score': score, 'version': '2.1'}

def analyze_readings(signals):
    # Core logic begins here
    patterns = extract_patterns(signals)
    metric = derive_metrics(patterns)
    
    # Red herring: multiple assignments and unused vars
    primary_diag, secondary_diag, tertiary_diag = metric, metric * 0.85, metric * 0.7
    temp_data = []
    for i in range(3):
        temp_data.append(math.log(primary_diag + i))  # Computation with no effect
    
    # Conditional branches with misleading comparisons
    if primary_diag > 200:
        adjustment = 10
    elif primary_diag > 100:
        adjustment = 5
    else:
        adjustment = 0
    
    final_adjusted = primary_diag + adjustment
    
    # Another decoy operation
    histogram = Counter(signals)
    total_pairs = sum(1 for k, v in histogram.items() if v >= 2)
    
    # Final computation using only one path
    scaling_factor = 1.2
    final_diagnostic = int((final_adjusted * scaling_factor) + 0.5)  # Rounded integer
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    raw_signals = collect_sensor_data()
    processed_signals = filter_noise(raw_signals)
    final_diagnostic = analyze_readings(processed_signals)