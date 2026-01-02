def analyze_pattern(sequence, threshold):
    count = 0
    for i in range(len(sequence)):
        if sequence[i] > threshold:
            count += 1
            temp_result = (i * 2) + sequence[i]  # red herring
    return count

# Irrelevant helper function (decoy)
def compute_entropy(data):
    import math
    freq_map = {}
    total = len(data)
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0.0
    for v in freq_map.values():
        p = v / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused but plausible-looking transformation
def transform_sequence(seq):
    return [x ** 0.5 for x in seq if x > 0]

# Core logic disguised among distractions
def filter_outliers(values, limit=100):
    filtered = []
    for v in values:
        if v < limit:
            filtered.append(v)
    return filtered

# Distractor: complex but unused data structure
class DataBuffer:
    def __init__(self, size):
        self.buffer = [0] * size
        self.index = 0

    def add(self, val):
        self.buffer[self.index] = val % 256
        self.index = (self.index + 1) % len(self.buffer)

# Real processing begins here
def evaluate_performance(metrics, base):
    # Step 1: extract relevant metrics
    primary = [m for m in metrics if m > 0]
    
    # Step 2: apply decay factor based on position (real logic)
    weighted = [primary[i] * (0.9 ** i) for i in range(len(primary))]
    
    # Step 3: calculate moving average over 3 elements
    avg_window = []
    for i in range(len(weighted) - 2):
        avg_window.append(sum(weighted[i:i+3]) / 3)
    
    # Step 4: find peak deviation from baseline
    deviations = [abs(w - base) for w in weighted]
    peak_dev = max(deviations) if deviations else 0
    
    # Step 5: use set operations to identify unique magnitude levels
    mag_levels = {int(abs(w)): w for w in weighted}
    unique_magnitudes = set(mag_levels.keys())
    
    # Step 6: slice top 4 by value
    sorted_weights = sorted(weighted, reverse=True)
    top_four_sum = sum(sorted_weights[:4]) if len(sorted_weights) >= 4 else sum(sorted_weights)
    
    # Step 7: apply correction using dictionary lookup
    corrections = {k: v * 0.85 for k, v in enumerate(sorted_weights)}
    corrected_total = sum(corrections.values()) if corrections else 0
    
    # Step 8: final score computation (this is the actual answer path)
    balance_factor = len(unique_magnitudes) / (len(weighted) or 1)
    stability = sum(1 for d in deviations if d < base) / len(deviations) if deviations else 0
    final_score = int(top_four_sum * stability + corrected_total * balance_factor)
    
    # Dead code branch - never executed
    if False:
        debug_log = {'final': final_score, 'dev': peak_dev}
        print(debug_log)
    
    return final_score

# Simulated input data
raw_signal = [-5, 10, 15, 20, 25, 30, 12, -8, 14, 18, 22]
baseline_ref = 17.5

# Unused variables and operations (distractions)
entropy_value = compute_entropy([1,2,2,3,3,3,4,4,4,4])
buffer_pool = [DataBuffer(8), DataBuffer(16)]
transformed_raw = transform_sequence(raw_signal)
outlier_filtered = filter_outliers(raw_signal, 50)

# Redundant list slicing
subset_a = raw_signal[2:8:2]
subset_b = raw_signal[::-1]

# Key execution point
metric_data = [x * 1.1 for x in raw_signal if x > 5]
sparse_mask = {i for i, x in enumerate(metric_data) if i % 2 == 0}  # set operation
baseline_adjusted = baseline_ref * 0.95

# Critical statement
final_score = evaluate_performance(metric_data, baseline_adjusted)

# Output result
print(f"Result: {final_score}")