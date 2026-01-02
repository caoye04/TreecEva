def analyze_pattern(sequence):
    count = 0
    for i, char in enumerate(sequence):
        if char.isupper() and i % 2 == 0:
            count += 1
    return count

# Irrelevant helper function (decoy)
def validate_input(text):
    if not isinstance(text, str):
        return False
    return text.strip() != ''

# Misleading data transformation (red herring)
raw_data = ['TempA', 'B2', 'C3X', 'Dxx', 'EXYZ']
decoy_matrix = [[ord(c) for c in s if c.isalpha()] for s in raw_data]
summed_features = sum(sum(row) for row in decoy_matrix)

# Unused but plausible-looking normalization function
def normalize_vector(vec):
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [v / magnitude for v in vec] if magnitude else vec

# Core logic buried among distractions
config_flags = {
    'enable_scaling': True,
    'use_legacy': False,
    'debug_mode': True
}

scaling_factor = 3.14 if config_flags['enable_scaling'] else 1.0
legacy_offset = -999  # Dead constant, never used

# Simulated sensor readings with noise
readings = [12, 15, 10, 8, 20, 13]
filtered = [x for x in readings if x > 10]

# Decoy statistical measures
mean_val = sum(readings) / len(readings)
variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
std_dev = variance ** 0.5

# Actual relevant data
weights = [0.2, 0.3, 0.5]
data = [85, 90, 78]

# Complex preprocessing with distractor operations
def preprocess_entry(item):
    base = item * 1.1
    adjustment = 0
    for j in range(2):
        if j == 1:
            adjustment += 0.5  # Red herring adjustment
    return int(base + adjustment)

def transform_dataset(arr):
    result = []
    for idx, val in enumerate(arr):
        temp = preprocess_entry(val)
        if idx % 2 == 0:
            temp -= 5
        postfix = f"item_{idx}"
        checksum = sum(int(c) for c in postfix if c.isdigit())  # Useless computation
        temp += checksum
        result.append(temp)
    return result

def compute_baseline(seq):
    total = 0
    for a, b in zip(seq[:-1], seq[1:]):
        total += abs(b - a)
    return total // 2

# Secondary distraction: file path simulation
current_path = "/sys/diag/metrics/log_2024.txt"
extension = current_path.split('.')[-1].upper()
path_flag = 1 if extension == 'TXT' else 0

# Real processing chain hidden in noise
def evaluate_component(x, w):
    return x * w * scaling_factor

def process_metrics(values, coeffs):
    # Apply transformations
    transformed = transform_dataset(values)
    base_metric = compute_baseline(transformed)
    
    # Additional interference
    audit_log = []
    for k in range(len(transformed)):
        audit_log.append(f"Step{k}: {transformed[k]}")
    
    # Actual weighted sum calculation
    aggregate = 0.0
    for v, c in zip(transformed, coeffs):
        contribution = evaluate_component(v, c)
        aggregate += contribution
    
    # Final adjustments
    final_modifier = analyze_pattern(audit_log)  # Uses string methods and enumerate
    final_score = aggregate + final_modifier * path_flag
    
    # Print for traceability
    print(f"Result: {final_score}")
    return final_score

# Execution point of interest
final_score = process_metrics(data, weights)