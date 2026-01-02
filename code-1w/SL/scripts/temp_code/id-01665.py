from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor readings from a metallurgical alloy analysis pipeline
def analyze_crystal_structure(sequence):
    structure_map = defaultdict(int)
    for elem in sequence:
        structure_map[elem % 7] += 1
    return dict(structure_map)

def compute_thermal_gradient(seq):
    # Irrelevant thermal computation (red herring)
    grad = 0
    for i in range(1, len(seq)):
        grad += abs(seq[i] - seq[i-1]) * 0.3
    return round(grad, 4)

def evaluate_purity_levels(batch):
    # Misleading purity metric (not used in final result)
    counts = Counter(batch)
    dominant = counts.most_common(1)[0][1]
    return dominant / len(batch)

def shift_phase_elements(arr, shift_by=3):
    # Bit manipulation decoy function
    shifted = []
    for x in arr:
        temp = (x << 2) ^ 5
        shifted.append(temp >> (shift_by % 4))
    return shifted

def generate_reference_template():
    # Dead code path: generates unused reference pattern
    template = [i**2 % 13 for i in range(15)]
    filtered = [t for t in template if t % 3 != 0]
    return filtered[::-1]

def calculate_coherence_factor(data):
    # Intermediate distraction with XOR chain
    factor = 0
    for d in data[::2]:
        factor ^= (d * 2) % 9
    return factor

def extract_segment_features(window):
    # Unused feature extraction (distractor)
    features = []
    for w in zip_longest(window, window[1:], fillvalue=0):
        features.append((w[0] + w[1]) % 11)
    return features

def process_alloy_sequence(raw_batch):
    # Core relevant logic buried among distractions
    
    # Step 1: Filter anomalies using modulo pattern (key step)
    clean_batch = [x for x in raw_batch if x % 5 != 2]
    
    # Step 2: Group by residue mod 4 (important)
    groups = defaultdict(list)
    for val in clean_batch:
        groups[val % 4].append(val)
    
    # Step 3: Compute weighted dispersion (core calculation)
    dispersion = 0
    for key in sorted(groups.keys()):
        group_sum = sum(g * (i+1) for i, g in enumerate(groups[key]))
        dispersion += group_sum * (key + 1)
    
    # Step 4: Apply corrective shift based on list slicing pattern (critical)
    history_log = clean_batch[-5:] if len(clean_batch) >= 5 else clean_batch
    offset = sum(history_log[::2]) - sum(history_log[1::2])
    
    # Step 5: Final score with controlled interference
    filtration_score = dispersion + (offset * len(groups))
    
    # Irrelevant side calculations below (high interference)
    _ = analyze_crystal_structure(raw_batch)
    _ = compute_thermal_gradient(raw_batch)
    _ = evaluate_purity_levels(raw_batch)
    _ = shift_phase_elements(raw_batch)
    _ = generate_reference_template()
    _ = calculate_coherence_factor(raw_batch)
    _ = extract_segment_features(raw_batch[:6])
    
    return filtration_score

# Main execution
alloy_batch = [18, 23, 14, 29, 34, 11, 46, 53, 8, 41, 22, 37, 64]
filtration_score = process_alloy_sequence(alloy_batch)
print(f"Result: {filtration_score}")