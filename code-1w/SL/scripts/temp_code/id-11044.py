import math

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 23.5, 'temp': 22.1, 'active': True, 'seq': 0},
    {'id': 2, 'val': 19.8, 'temp': 23.0, 'active': False, 'seq': 1},
    {'id': 3, 'val': 20.1, 'temp': 22.5, 'active': True, 'seq': 2},
    {'id': 4, 'val': 25.3, 'temp': 24.3, 'active': True, 'seq': 3},
    {'id': 5, 'val': 18.7, 'temp': 21.9, 'active': True, 'seq': 4}
]

# Irrelevant statistical counters (distractors)
mean_temp = 0.0
variance_temp = 0.0
temp_values = [d['temp'] for d in data_stream]
if len(temp_values) > 0:
    mean_temp = sum(temp_values) / len(temp_values)
    variance_temp = sum((t - mean_temp) ** 2 for t in temp_values) / len(temp_values)

# Noise threshold calculation (unused red herring)
noise_floor = math.log(len(data_stream) + 1) * 0.5

# Misleading transformation: bit manipulation on IDs (dead end)
id_bit_analysis = 0
for d in data_stream:
    id_bit_analysis ^= d['id'] << 1
    id_bit_analysis |= (d['id'] & 1)

# Auxiliary function that appears important but is never called
def analyze_redundancy(data):
    """Dead function: looks relevant but unused"""
    return sum(d['val'] * d['seq'] for d in data if d['active']) % 7

# Secondary processing: filtering and indexing using enumerate and zip (core + distractor mix)
filtered_data = [d for d in data_stream if d['active']]
indexed_vals = [(i, d['val']) for i, d in enumerate(filtered_data)]

# Complex weight assignment with irrelevant combinatorics
n_active = len(filtered_data)
combinatoric_weight = 1
for i in range(1, min(n_active + 1, 5)):
    combinatoric_weight *= (n_active - i + 1) // i if i > 1 else n_active

# Decoy normalization factor (never applied)
max_val = max(d['val'] for d in data_stream)
min_val = min(d['val'] for d in data_stream)
normalization_factor = 1.0 / (max_val - min_val + 1e-8) if max_val != min_val else 1.0

# Real signal extraction: weighted harmonic mean of active values with position weights
position_weights = [math.sin(i * math.pi / (len(indexed_vals) + 1)) for i, _ in indexed_vals]
weighted_vals = []
for idx, val in indexed_vals:
    weight = position_weights[idx] * (0.5 + idx * 0.1)
    weighted_vals.append(weight / val if val != 0 else 0)

harmonic_intermediate = len(weighted_vals) / sum(weighted_vals) if sum(weighted_vals) > 0 else 0

# Secondary decoy: string-based encoding of sequence (irrelevant)
seq_codes = ''.join(str(d['seq']) for d in data_stream)
encoded_seq = ''.join(chr(ord(c) + 1) for c in seq_codes)  # Obfuscation with no use

# Another decoy list transformation using zip
paired_shifts = []
for a, b in zip(data_stream, data_stream[1:]):
    paired_shifts.append(abs(a['val'] - b['val']) * (a['id'] % 2))

# Core logic hidden among distractions: final score combines harmonic result and combinatoric weight
# But only uses harmonic_intermediate and n_active in a non-obvious way
scaling_hint = [x for x in [2, 4, 8, 16] if x > n_active]
scale_factor = scaling_hint[0] if scaling_hint else 32

# Final computation path — only this matters
def calculate_final_score(data):
    base = harmonic_intermediate  # From earlier complex computation
    bonus = combinatoric_weight * 0.1  # Weight from combinatorics (subtle relevance)
    penalty = math.ceil(scale_factor / 4)  # Based on number of active elements
    return int(base + bonus - penalty)

# Execution point of interest
processed_data = filtered_data
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")