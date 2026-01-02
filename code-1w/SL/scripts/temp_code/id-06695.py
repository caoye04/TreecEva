def analyze_pattern(seq, limit):
    """Irrelevant auxiliary function for signal processing (dead code path)."""
    accumulator = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            accumulator += seq[i] * limit
    return accumulator

# Distractor: Unused complex transformation
def encrypt_key(data):
    return [d ^ 255 for d in data]

# Real logic begins
import math

initial_buffer = [3, 7, 12, 18, 23, 27, 31, 36, 40, 45]
offset_map = {i: val % 10 for i, val in enumerate(initial_buffer)}

# Irrelevant transformation chain
shadow_copy = initial_buffer[::2]  # slicing: every second element
expanded = [x * x for x in shadow_copy if x < 30]
scaled_noise = sum([int(math.log(n + 1, 2)) for n in expanded])  # misleading metric

# Core data structure
health_data = [
    {'id': 'A', 'vital': 88, 'stress': 4, 'recovery': 7},
    {'id': 'B', 'vital': 92, 'stress': 6, 'recovery': 5},
    {'id': 'C', 'vital': 79, 'stress': 8, 'recovery': 9},
    {'id': 'D', 'vital': 95, 'stress': 3, 'recovery': 8}
]

# Distractor variables
baseline_score = sum(d['vital'] // d['stress'] for d in health_data if d['stress'] > 0)
phantom_index = (baseline_score * 7) % 13

# Real threshold logic
threshold = 85
adjustment_factor = 0.85

# Misleading normalization (not used in final result)
normalized_vitals = [round(d['vital'] * adjustment_factor) for d in health_data]

# Key slicing operation on list of dictionaries
subset_data = health_data[1:3]  # middle two patients

# Composite diagnostic calculation
composite_scores = []
for patient in health_data:
    raw_score = patient['vital']
    stress_penalty = patient['stress'] * 2.5
    recovery_bonus = math.sqrt(patient['recovery']) * 1.5
    adjusted_score = raw_score - stress_penalty + recovery_bonus
    composite_scores.append(adjusted_score)

# Conditional filtering based on threshold
above_threshold = [score for score in composite_scores if score >= threshold]

# Bit manipulation decoy
bit_fiddle = 0
for score in composite_scores:
    bit_fiddle ^= int(score) & 0xFF

# Tuple unpacking red herring
(a, b), (c, d) = (expanded[:2], expanded[2:]), (offset_map[1], offset_map[3])
dummy_checksum = (a + b) * c - d

# Actual processing function used in final step
def process_metrics(data_list, thresh):
    scores = []
    for entry in data_list:
        base = entry['vital']
        modifier = entry['recovery'] - (entry['stress'] // 2)
        final_val = base + (modifier * 3)
        scores.append(final_val)
    filtered = [s for s in scores if s > thresh]
    return sum(filtered) // len(filtered) if filtered else 0

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold)
print(f"Result: {final_diagnostic}")