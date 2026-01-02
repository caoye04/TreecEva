from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor data processing with red herrings
def collect_readings(samples):
    readings = defaultdict(list)
    for i, val in enumerate(samples):
        if i % 3 == 0:
            readings['type_a'].append(val * 1.5)
        elif i % 5 == 0:
            readings['type_b'].append(val + 2)
        else:
            readings['other'].append(val // 2)
    return readings

def filter_anomalies(data_dict):
    # Irrelevant filtering (distraction)
    clean = {}
    for k, v in data_dict.items():
        clean[k] = [x for x in v if x > 0]
    # Dead code path
    if len(clean.get('type_x', [])) > 100:
        return {k: sorted(v) for k, v in clean.items()}
    return clean

def generate_pairs(lst):
    # Unused combinatorial expansion (distractor)
    return list(combinations(lst, 2))

def shift_sequence(seq, key=3):
    # Bit manipulation red herring
    shifted = []
    for num in seq:
        transformed = (num << 1) ^ key  # Irrelevant transformation
        normalized = transformed % 100
        shifted.append(normalized)
    return shifted

def extract_frequency_profile(data_list):
    # Real work hidden among distractions
    count = Counter(data_list)
    freq_of_freq = Counter(count.values())
    return sorted(freq_of_freq.items())

def compute_entropy_signature(freq_items):
    total = sum(f for _, f in freq_items)
    entropy = 0
    for _, f in freq_items:
        p = f / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Non-standard measure as decoy
    return round(entropy, 6)

def derive_key_from_pattern(signal):
    # Complex but irrelevant derivation
    acc = 0
    for i, s in enumerate(signal):
        acc += s * (-1) ** i
    return acc % 77

def transform_signal_integrity(raw_values):
    # Main relevant transformation chain begins here
    base_shifted = [v * 2 + 1 for v in raw_values if v % 2 == 1]  # Only odd values used
    
    # Red herring: complex unpacking and cycling
    padded = []
    pad_cycle = cycle([1, -1])
    for val in base_shifted:
        padded.extend([val, next(pad_cycle)])
    
    # Actual core logic (obscured)
    processed = []
    for i, p in enumerate(padded):
        if i % 3 == 0 and isinstance(p, int):
            processed.append(p)
    
    # This is where real computation happens
    frequency_profile = extract_frequency_profile(processed)
    entropy_score = compute_entropy_signature(frequency_profile)
    key_index = derive_key_from_pattern(processed)  # Not actually used later
    
    # Final meaningful transformation
    result = int(abs(entropy_score * 100000)) % 999999
    return result

def analyze_pattern(dataset):
    # Orchestration function with multiple distractions
    temp_store = []
    meta_log = []
    
    # Distractor loop with no impact
    for i in range(3):
        snapshot = {"cycle": i, "status": "idle"}
        meta_log.append(snapshot)
    
    # Real data flow
    intermediate = []
    for chunk in dataset:
        if len(chunk) > 2:
            focused = [x for x in chunk if x > 10]
            shifted_chunk = shift_sequence(focused, key=len(focused))
            intermediate.extend(shifted_chunk)
    
    # Critical operation buried here
    cleaned = [x for x in intermediate if x % 4 == 0]
    final_value = sum(cleaned) // (len(cleaned) or 1)
    
    # Decoy calculation
    fake_diagnostic = transform_signal_integrity(intermediate)
    
    # Correct answer is based on final_value, not fake_diagnostic
    final_diagnostic = (final_value * 17) % 999999
    return final_diagnostic

# Simulated input data
sensor_input = list(range(15, 32))
raw_groups = [sensor_input[i:i+5] for i in range(0, len(sensor_input), 5)]
collected = collect_readings(sensor_input)
filtered = filter_anomalies(collected)
transformed_data = []
for group in raw_groups:
    transformed_data.append([g * 3 - 5 for g in group])

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")