import math

def analyze_signal(samples):
    # Irrelevant signal processing function (dead end)
    fft_magnitude = [abs(s) ** 2 for s in samples]
    normalized = [x / sum(fft_magnitude) for x in fft_magnitude]
    return sum(normalized[:len(normalized)//2])

def validate_entry(record):
    # Distractor: complex validation that isn't actually used
    if not record.get('active'):
        return False
    checksum = sum(ord(c) for c in record['id']) % 11
    return checksum == record['version'] % 11

def transform_sequence(seq, factor=1.5):
    # Unused transformation path
    return [int(x * factor) if i % 2 == 0 else x for i, x in enumerate(seq)]
data = [
    {'value': 85, 'meta': {'flags': [1, 0, 1], 'level': 3}},
    {'value': 92, 'meta': {'flags': [0, 1, 1], 'level': 2}},
    {'value': 78, 'meta': {'flags': [1, 1, 0], 'level': 4}}
]

weights = [0.4, 0.3, 0.3]  # Weight distribution for scoring

# Decoy variables with plausible but unused computations
baseline_offset = 12.5
adjustment_factor = lambda x: x * 1.05 if x > 80 else x * 0.98
dummy_flags = [f for sample in data for f in sample['meta']['flags']]  # Collected but unused
flag_sum = sum(dummy_flags)  # Misleading intermediate result

# Complex conditional expression involving slicing and filtering
filtered_values = [
    entry['value'] * (1 + 0.1 * entry['meta']['level']) 
    for entry in data 
    if sum(entry['meta']['flags']) >= 2
]

# Unused recursive helper (red herring)
def calculate_depth(node, depth=0):
    if 'children' not in node or not node['children']:
        return depth
    return max(calculate_depth(child, depth + 1) for child in node['children'])

# Core logic embedded within distractions
def process_metrics(records, w):
    raw_scores = [r['value'] for r in records]
    
    # Bit manipulation distraction
    magic_correction = 0
    for i, val in enumerate(raw_scores):
        magic_correction ^= (val & (0x7FFFFFFF >> (i + 1))) & 0xF
    
    # Conditional expression with slicing
    primary_slice = raw_scores[:2] if len(raw_scores) > 2 else raw_scores
    extended_slice = raw_scores[1:] or [0]
    
    # Key computation hidden among distractors
    base_metric = sum(
        score * weight 
        for score, weight in zip(primary_slice, w[:len(primary_slice)])
    )
    
    # Secondary adjustment using lambda and conditional logic
    adjustment = adjustment_factor(base_metric) if base_metric > 85 else base_metric
    
    # Final nonlinear transformation (answer depends on this)
    final_component = adjustment * math.cos(math.pi / 6)  # cos(π/6) ≈ 0.866025
    
    # Irrelevant aggregation
    avg_level = sum(r['meta']['level'] for r in records) / len(records)
    level_influence = avg_level * 0.2  # Not actually used
    
    # Critical assignment buried in logic
    final_score = int(final_component + 0.5)  # Round to nearest integer
    
    return final_score

# Simulated unused control flow (misleads tracing)
if __name__ == "__main__":
    temp_result = analyze_signal([1, 2, 3, 4, 5])
    dummy_seq = transform_sequence([10, 20, 30])

# Execution point of interest
final_score = process_metrics(data, weights)
print(f"Result: {final_score}")