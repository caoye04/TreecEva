def preprocess_text(data):
    cleaned = data.strip().lower().replace(' ', '_')
    parts = cleaned.split('_')
    filtered = [p for p in parts if len(p) > 2]
    joined = '|'.join(filtered)
    return joined.upper()

# Irrelevant helper function (decoy)
def analyze_frequency(text):
    freq_map = {}
    for char in text:
        if char.isalpha():
            freq_map[char] = freq_map.get(char, 0) + 1
    sorted_freq = sorted(freq_map.items(), key=lambda x: -x[1])
    return sorted_freq[:3] if sorted_freq else []

# Another decoy function with dead logic
def validate_checksum(seq):
    if not seq:
        return False
    checksum = 0
    for i, val in enumerate(seq):
        checksum += val * (i + 1)
    return checksum % 7 == 0

# Core transformation chain
def generate_sequence(key):
    base = [key ** 2, key * 3, key + 5]
    expanded = []
    for x in base:
        expanded.append(x % 19)
        expanded.append(x // 4)
    unique_vals = list(set(expanded))
    sorted_vals = sorted(unique_vals, reverse=True)
    return sorted_vals[:5]

# Misleading data path that computes but isn't used
def compute_shadow_matrix(n):
    matrix = [[(i*j) % n for j in range(n)] for i in range(n)]
    trace = sum(matrix[i][i] for i in range(n))
    flattened = [item for row in matrix for item in row]
    return trace, sum(flattened)

# Data obfuscation through string manipulation
def encode_features(raw_str):
    tokens = raw_str.split('|')
    encoded = []
    for token in tokens:
        if token.startswith('A'):
            encoded.append(len(token) * 2)
        elif token.endswith('X'):
            encoded.append(len(token) + 10)
        else:
            encoded.append(hash(token) % 100)
    return encoded

# Main processing pipeline with red herring variables
def process_sequence(seq):
    temp_results = []
    scaling_factor = 7
    offset = 13
    
    # Real computation branch
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed = (val * scaling_factor) - offset
        else:
            transformed = (val + offset) // 2
        temp_results.append(abs(transformed))
    
    # Dead branch - never executed due to condition
    debug_mode = False
    if debug_mode and len(temp_results) > 10:
        temp_results = [x for x in temp_results if x % 2 == 0]
    
    # Actual final computation
    aggregate = sum(temp_results)
    adjustment = len(temp_results) * 3
    final_score = aggregate - adjustment
    
    # Decoy variable with plausible name but no use
    auxiliary_metric = (aggregate * adjustment) % 1000
    
    # Key result
    final_output = final_score + 5  # Final adjustment
    return final_output

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
ACTIVE_MODULES = ['core', 'io', 'parser']

# Obfuscated setup with string operations
raw_input = "Data Pipeline Optimization Task"
processed_tag = preprocess_text(raw_input)
shadow_trace, flat_sum = compute_shadow_matrix(4)

# Real data flow initiation
base_key = len(processed_tag) % 17  # Derives to 7
sequence_data = generate_sequence(base_key)
# Injecting fake dependency (unused)
frequency_analysis = analyze_frequency(processed_tag)

token_string = "AX|BX|Complex"  # Triggers mixed encoding
transformed_data = encode_features(token_string)

# Critical execution point
final_output = process_sequence(transformed_data)
print(f"Result: {final_output}")