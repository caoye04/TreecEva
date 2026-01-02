def analyze_readings(readings):
    cumulative = 0
    for val in readings:
        if val > 75:
            cumulative += val // 3
        elif val < 25:
            cumulative -= val % 7
    return cumulative

# Irrelevant sensor calibration (dead code path)
def calibrate_sensor(x):
    return (x * 0.987) + 12.4
def normalize_string(s):
    return s.upper().strip().replace(' ', '_')

def compute_factorial(n):
    if n <= 1:
        return 1
    return n * compute_factorial(n - 1)

# Unused transformation matrix
transform_matrix = [[1, -1, 0], [0, 1, -1], [-1, 0, 1]]
temp_offset = sum([transform_matrix[i][i] for i in range(3)])  # Always 1

# Simulated health data from multiple sources
raw_values = [86, 42, 15, 91, 67, 23, 77]

# Misleading preprocessing step (not used in final calculation)
filtered_data = [x for x in raw_values if x > 20 and x < 80]
filtered_data.append(55)

# Primary dataset
data_stream = [88, 34, 12, 94, 61, 19, 82, 44]

# Distractor: Character frequency analysis (unrelated to main logic)
document_ref = "patient_scan_log_2024_v3"
char_count = {}
for ch in document_ref:
    char_count[ch] = char_count.get(ch, 0) + 1
vowel_score = sum(char_count.get(v, 0) for v in 'aeiou')

# Threshold configuration map (used later)
threshold_map = {
    'critical': 85,
    'warning': 65,
    'normal': 30
}

# Augmented data with conditional expression
augmented_stream = [val * 1.1 if val > threshold_map['warning'] else val * 0.95 for val in data_stream]

# Bit manipulation red herring
defect_flag = 0b101010
mask = 0b111100
masked_defect = defect_flag & mask  # Results in 40, unused

# Main processing pipeline
health_data = []
for idx, val in enumerate(augmented_stream):
    record = {
        'id': f'REC_{idx+1000}',
        'raw': data_stream[idx],
        'adj': round(val),
        'category': 'high' if val > threshold_map['warning'] else 'low'
    }
    health_data.append(record)

# Secondary metric based on string length (distractor)
sum_id_chars = sum(len(entry['id']) for entry in health_data)  # Always 5*8=40

# Actual core logic disguised among distractions
def process_metrics(data_list, limits):
    total_risk = 0
    high_count = 0
    
    # Linear search through records
    for entry in data_list:
        base_val = entry['raw']
        
        # Relevant logic branch
        if base_val > limits['critical']:
            total_risk += base_val // 4
            high_count += 1
        elif base_val > limits['warning']:
            total_risk += base_val // 5
        
        # Decoy operation using string method (no effect)
        if entry['id'].startswith('REC') and entry['category'] == 'high':
            _ = entry['id'].split('_')  # Dead computation
    
    # Final transformation
    adjustment = 7 if high_count >= 3 else 11
    final_score = total_risk * adjustment
    
    # Additional noise: unused recursion result
    _ = compute_factorial(high_count % 4)
    
    return final_score

# Key execution point
final_diagnostic = process_metrics(health_data, threshold_map)
print(f"Result: {final_diagnostic}")