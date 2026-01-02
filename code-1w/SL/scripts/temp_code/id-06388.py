from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 3.5, 'type': 'A', 'seq': 1, 'meta': 'X'},
    {'id': 2, 'val': -2.1, 'type': 'B', 'seq': 2, 'meta': 'Y'},
    {'id': 3, 'val': 4.8, 'type': 'A', 'seq': 3, 'meta': 'X'},
    {'id': 4, 'val': 0.0, 'type': 'C', 'seq': 4, 'meta': 'Z'},
    {'id': 5, 'val': 6.2, 'type': 'B', 'seq': 5, 'meta': 'X'},
    {'id': 6, 'val': -1.3, 'type': 'A', 'seq': 6, 'meta': 'Y'},
    {'id': 7, 'val': 5.9, 'type': 'C', 'seq': 7, 'meta': 'X'},
    {'id': 8, 'val': 2.7, 'type': 'A', 'seq': 8, 'meta': 'Z'}
]

# Irrelevant baseline constants for distraction
equilibrium_baseline = 1.414
noise_floor = 0.05
calibration_offset = -0.77
scaling_factor = 2.5
normalization_constant = 9.81

# Distractor function: looks important but unused
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Another decoy function with misleading name
def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    trend = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    return trend

# Real processing begins here
valid_types = {'A', 'B', 'C'}
filtered_data = []
temp_vals = []

for entry in data_stream:
    raw_val = entry['val']
    # Apply fake correction that's not actually used later
    corrected = raw_val + calibration_offset if raw_val > 0 else raw_val - calibration_offset
    temp_vals.append(abs(raw_val))
    
    # Actual filtering logic
    if entry['type'] in valid_types and entry['id'] % 2 == 1:
        filtered_data.append(entry)

# Unused statistical summary (distractor)
avg_temp = sum(temp_vals) / len(temp_vals) if temp_vals else 0
std_dev_temp = (sum((x - avg_temp) ** 2 for x in temp_vals) / len(temp_vals)) ** 0.5 if temp_vals else 0

# Build threshold map using only type 'A' entries from filtered_data
threshold_map = defaultdict(float)
type_counts = Counter()

for entry in filtered_data:
    t = entry['type']
    type_counts[t] += 1
    if t == 'A':
        threshold_map[t] += abs(entry['val']) * 0.5
    elif t == 'B':
        threshold_map[t] += entry['val'] ** 2 * 0.1
    else:
        threshold_map[t] += math.log(abs(entry['val']) + 1) * 0.3

# Normalize thresholds by count (only matters for 'A')
for k in threshold_map:
    if type_counts[k] > 0:
        threshold_map[k] /= type_counts[k]

# More red herring variables
signal_strength = sum(threshold_map.values()) * scaling_factor
consistency_score = len([v for v in temp_vals if v > avg_temp]) / len(temp_vals) if temp_vals else 0

# Core logic disguised among distractions
def process_signals(data, thresholds):
    result = 0.0
    cumulative_shift = 0
    
    for item in data:
        val = item['val']
        typ = item['type']
        
        # Multi-step conditional processing
        if typ == 'A':
            if val > 0:
                result += math.sqrt(val) * thresholds[typ]
            else:
                result -= abs(val) ** 0.3
        elif typ == 'B':
            intermediate = val * thresholds[typ]
            if intermediate > 1.0:
                result += math.log(intermediate + 1)
            else:
                result += intermediate ** 2
        elif typ == 'C':
            base_contrib = abs(val) * 0.5
            if item['seq'] % 3 == 0:
                base_contrib *= 1.5
            result += base_contrib * thresholds[typ]
            
        # Hidden accumulator affecting final result
        cumulative_shift += int(abs(val)) % 3
    
    # Final transformation
    result = (result * 100) // 1  # Floor to nearest integer as float
    result += cumulative_shift
    
    return result

# Dead code path - never executed but looks plausible
if __name__ == "__fake_main__":
    debug_mode = True
    validation_check = analyze_pattern([d['val'] for d in data_stream])
    print("Debug:", validation_check)

# Critical execution point
final_output = process_signals(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_output}")