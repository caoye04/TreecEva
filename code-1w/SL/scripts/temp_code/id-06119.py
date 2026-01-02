from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic evaluation

def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    trend = all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))
    oscillation = sum(1 for i in range(1, len(sequence)-1) if sequence[i-1] < sequence[i] > sequence[i+1])
    return trend or oscillation > 2

# Irrelevant helper - dead logic path (never called)
def compute_entropy(data_list):
    freq = Counter(data_list)
    total = len(data_list)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return round(entropy, 4)

# Unused transformation map (distractor)
transformation_grid = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + (x % 7),
    'C': lambda x: abs(x - 100),
    'D': lambda x: x * (x % 3 + 1)
}

# Legacy calibration values (red herring)
calibration_offsets = [0.1, -0.3, 0.7, 1.2, -0.9, 0.0, 0.4]
reference_matrix = [[i * j for j in range(5)] for i in range(5)]

# Primary data input
raw_readings = [
    [12, 15, 13, 14, 16, 18],
    [22, 24, 23, 25, 27, 26],
    [8,  10, 12, 11, 10,  9],
    [30, 35, 40, 45, 50, 55],
    [5,   7,  6,  8,  7,  6]
]

# Decoy processing function (not used in final flow)
def legacy_filter(dataset, limit=10):
    result = []
    for seq in dataset:
        temp = [x for x in seq if x > limit]
        if len(temp) >= 4:
            result.append(temp)
    return result

# Threshold configuration map (used later)
threshold_map = defaultdict(lambda: (0, 100))
threshold_map.update({
    'critical_low': (0, 10),
    'moderate': (10, 30),
    'elevated': (30, 60),
    'critical_high': (60, 100)
})

# Secondary metadata (partially irrelevant)
diagnostic_flags = {
    'stability': True,
    'redundancy_check': 'passed',
    'version': '2.1a',
    'checksum': 5184
}

# Complex filtering with slicing and pattern analysis
filtered_data = []
for reading in raw_readings:
    segment_a = reading[:4]  # First four
    segment_b = reading[2:]   # Last four
    
    # Overlapping slice intersection
    overlap = [x for x in segment_a if x in segment_b]
    
    # Mean filter with distractor calculation
    mean_val = sum(reading) / len(reading)
    variance_proxy = sum((x - mean_val) ** 1.8 for x in reading) / len(reading)  # Not real variance
    
    # Actual relevance condition
    if mean_val > 15 and analyze_pattern(reading):
        filtered_data.append(overlap)

# Spurious intermediate transformation (no effect on output)
temp_output = []
for item in filtered_data:
    shifted = [x + 5 for x in item if x % 2 == 0]
    temp_output.append(shifted)

# Misleading normalization routine (unused)
def normalize_sequence(seq):
    min_val, max_val = min(seq), max(seq)
    if max_val == min_val:
        return [0.5] * len(seq)
    return [(x - min_val) / (max_val - min_val) for x in seq]

# Core processing function that determines final answer
def process_readings(data_blocks, thresholds):
    category_count = defaultdict(int)
    flat_values = [val for block in data_blocks for val in block]
    
    # Map values to categories using threshold ranges
    for value in flat_values:
        if value < 10:
            category_count['critical_low'] += 1
        elif 10 <= value < 30:
            category_count['moderate'] += 1
        elif 30 <= value <= 60:
            category_count['elevated'] += 1
        else:
            category_count['critical_high'] += 1
    
    # Diagnostic score calculation (actual answer source)
    score_parts = []
    for key in ['critical_low', 'moderate', 'elevated', 'critical_high']:
        base_weight = {'critical_low': 3, 'moderate': 1, 'elevated': 2, 'critical_high': 4}[key]
        count = category_count[key]
        contribution = base_weight * (count ** 1.5) if count > 0 else 0
        score_parts.append(round(contribution))
    
    # Final diagnostic value
    final_score = sum(score_parts) + 100  # Base offset
    
    # Dead code branch (never executed due to structure)
    if diagnostic_flags.get('invalid_condition', False):
        final_score *= 0.5
        
    return int(final_score)

# Trigger execution
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Target result: {final_diagnostic}")