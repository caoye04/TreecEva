from collections import defaultdict, Counter
import math

# Irrelevant setup: Sensor simulation (distractor)
sensor_nodes = [f'node_{i}' for i in range(12)]
node_status = {node: 'active' for node in sensor_nodes}
calibration_offset = sum([hash(n) % 100 for n in sensor_nodes]) // 12

# Decoy function: Unused but plausible
def compute_resonance(freq, phase):
    return (freq * phase) % 77 + 3

# Real logic begins: Pattern analyzer with red herrings
def generate_sequence(length, seed=10):
    seq = []
    x = seed
    for i in range(length):
        if i % 5 == 0:
            x = (x * 1.618) % 1000
        elif i % 3 == 0:
            x = (x ** 0.5) * 10
        else:
            x = (x + 7) * 1.1
        seq.append(int(x) % 97)
    return seq

# Misleading transformation chain
def transform_signal(data):
    temp_result = []
    shift_val = len(data) // 4
    for idx, val in enumerate(data):
        shifted = (val << 2) ^ 255
        if shifted > 200:
            shifted = shifted // 3
        temp_result.append(shifted + idx % 10)
    # Dead path: never used
    processed_log = [math.log(x + 1) for x in temp_result if x > 0]
    return temp_result  # Only this matters

# Core analysis with distractors
def evaluate_stability(measurements):
    count_map = Counter(measurements)
    mode_val = count_map.most_common(1)[0][1]
    entropy = 0.0
    total = len(measurements)
    for count in count_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    
    # Red herring computation
    dummy_score = sum([k * v for k, v in count_map.items()]) % 88
    
    # Relevant only if threshold met
    if entropy > 4.5:
        return mode_val * 2
    else:
        return mode_val + 10

# Another decoy: looks important, unused
class DataNormalizer:
    def __init__(self, cap=100):
        self.cap = cap
        self.history = []

    def normalize(self, x):
        return min(x, self.cap) / self.cap

# Main processing pipeline
def analyze_pattern(raw_series, config_thresholds):
    # Step 1: Filter using threshold (actual use)
    filtered = [x for x in raw_series if x > config_thresholds['base']]
    
    # Step 2: Frequency counting with defaultdict (relevant)
    freq_table = defaultdict(int)
    for val in filtered:
        freq_table[val] += 1
    
    # Step 3: Transform using lambda in map (real usage)
    transformed = list(map(lambda x: (x * 3) ^ 42, filtered))
    
    # Step 4: Conditional logic with nested expressions
    if len(transformed) > 15:
        pivot = sum(transformed) // len(transformed)
        left = [x for x in transformed if x <= pivot]
        right = [x for x in transformed if x > pivot]
        if len(left) == 0:
            branch_metric = pivot
        else:
            # Deep nesting with actual logic
            max_gap = 0
            sorted_left = sorted(left)
            for i in range(1, len(sorted_left)):
                gap = sorted_left[i] - sorted_left[i-1]
                if gap > max_gap:
                    max_gap = gap
            branch_metric = max_gap * len(right) if len(right) > 0 else max_gap + 5
    else:
        branch_metric = len(transformed) * 11
    
    # Step 5: Spurious intermediate that looks like final result
    pseudo_diagnostic = (branch_metric + len(freq_table)) % 1000
    
    # Step 6: Actual key computation (non-obvious)
    unique_high_vals = {k for k, v in freq_table.items() if v >= 3 and k > 50}
    bonus = len(unique_high_vals) * 13
    
    # Final result built from multiple concepts
    final_value = branch_metric + bonus
    
    # Dead code block: looks like it updates something important
    diagnostic_log = []
    for k in sorted(freq_table.keys()):
        if freq_table[k] % 2 == 0:
            diagnostic_log.append(f"even_count:{k}")
    
    return final_value

# Irrelevant global tracking
global_counter = 0
log_entries = []
for i in range(5):
    log_entries.append(f"init_pass_{i}")
    global_counter += 1

# Generate real data input
raw_data = generate_sequence(25, seed=13)
processed_signal = transform_signal(raw_data)
stability_rating = evaluate_stability(processed_signal)

# Configuration with misleading keys
default_thresholds = {
    'base': 20,
    'peak': 85,
    'decay': 0.9,
    'dummy_flag': True,
    'mode_bias': None
}

# Collect data (only this matters)
collected_data = [x + stability_rating for x in processed_signal]

# Key execution point
final_diagnostic = analyze_pattern(collected_data, default_thresholds)

print(f"Result: {final_diagnostic}")