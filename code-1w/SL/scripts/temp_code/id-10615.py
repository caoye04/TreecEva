from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor array data with noise and redundant readings
def simulate_sensor_readings():
    raw_data = [18, 23, 15, 47, 22, 35, 29, 41, 33, 27]
    noise_sequence = cycle([1, -2, 0, 3])
    noisy_data = [x + next(noise_sequence) for x in raw_data]
    return noisy_data

# Irrelevant helper: processes unused metadata
def extract_metadata(tags):
    tag_count = defaultdict(int)
    for tag in tags:
        tag_count[tag] += 1
    return tag_count

# Core diagnostic computation with distractors
def run_diagnostics():
    # Primary signal processing
    sensor_readings = simulate_sensor_readings()
    filtered_readings = [x for x in sensor_readings if x > 20]
    
    # Distractor: complex but unused combinatorics
    pair_combinations = list(combinations(filtered_readings, 2))
    high_variance_pairs = [p for p in pair_combinations if abs(p[0] - p[1]) > 15]
    entropy_proxy = len(high_variance_pairs) % 7
    
    # Bit manipulation red herring
    magic_offset = 0
    for i in range(3):
        magic_offset ^= (entropy_proxy << i)
    
    # Real computation path begins
    base_values = [x // 2 for x in filtered_readings]  # Integer division
    sum_of_bases = sum(base_values)
    
    # Conditional adjustment chain
    adjustment = 0
    if sum_of_bases > 100:
        adjustment += 5
    if len(base_values) % 2 == 0:
        adjustment -= 2
    
    # Key intermediate result
    aggregate_score = sum_of_bases + adjustment
    
    # Decoy statistical analysis
    freq_map = Counter(base_values)
    mode_guess = freq_map.most_common(1)[0][1]
    outlier_flags = [k for k, v in freq_map.items() if v == 1]
    
    # Unused recursive distraction
    def analyze_outliers(data, depth=2):
        if depth == 0 or not data:
            return 999
        mid = len(data) // 2
        return analyze_outliers(data[:mid], depth-1) + analyze_outliers(data[mid:], depth-1)
    
    _ = analyze_outliers(outlier_flags)
    
    # Correction factor derived from bitwise logic
    control_flag = 0b1010
    status_code = len(outlier_flags) & 0b111
    correction_factor = (control_flag ^ status_code) * 3
    
    # Critical assignment - target execution point
    final_diagnostic = aggregate_score + correction_factor
    
    # Dead code path: never executed but looks important
    if False:
        fallback = 0
        for val in cycle(base_values):
            fallback += val
            if fallback > 1000:
                break
        final_diagnostic = fallback
    
    return final_diagnostic

# Execution entry point
result = run_diagnostics()
print(f"Result: {result}")