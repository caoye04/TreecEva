def analyze_pattern(sequence):
    """Irrelevant analysis function with misleading computations."""
    temp_sum = 0
    for i, val in enumerate(sequence):
        temp_sum += val * (i + 1)
    return temp_sum % 7

def validate_checksum(items):
    """Decoy validation logic that is never used."""
    checksum = 0
    for idx, item in enumerate(items):
        if item % 2 == 0:
            checksum ^= idx + item
    return checksum > 5

def transform_data(arr, factor=3):
    """Distractor transformation with unused bit manipulation."""
    transformed = []
    shift_key = len(arr) % 4
    for x in arr:
        # Complex but irrelevant transformation
        shifted = (x << shift_key) ^ factor
        transformed.append(shifted % 100)
    return sorted(transformed, reverse=True)

def count_characters(text_list):
    """Unused utility simulating character counting."""
    total_chars = 0
    for text in text_list:
        total_chars += len(text.strip())
    return total_chars

def main_process(input_vals):
    """Main flow with red herrings and early exits."""
    if sum(input_vals) < 50:
        return -1  # Early exit not taken

    # Irrelevant sorting and zipping
    indexed = list(enumerate(input_vals))
    reversed_vals = input_vals[::-1]
    paired = list(zip(indexed, reversed_vals))

    # Dummy filter operation
    filtered = [v for i, v in enumerate(input_vals) if i % 3 != 2]

    # Actual relevant computation starts here
    base_values = [x for x in input_vals if x > 5]
    
    # Secondary filtering
    processed = []
    for val in base_values:
        if val % 2 == 1:  # Keep only odd values > 5
            processed.append(val)
    
    # Weight application using modular arithmetic
    weights = [3, 7, 2, 5]
    weighted_sum = 0
    weight_idx = 0
    for num in processed:
        weighted_sum += num * weights[weight_idx % len(weights)]
        weight_idx += 1
    
    # Misleading normalization path
    max_val = max(weighted_sum, 1)
    normalized = weighted_sum / (max_val ** 0.1)
    
    # Final adjustment
    final_score = int(normalized) + (weighted_sum % 19)
    
    # Dead code path
    if final_score < 0:
        final_score = 0
    
    return final_score

def calculate_final_score(data, weights):
    # Core logic reused with minor variation
    base_values = [x for x in data if x > 5 and x % 2 == 1]  # Odd and > 5
    weighted_sum = 0
    for i, val in enumerate(base_values):
        weighted_sum += val * weights[i % len(weights)]
    
    # Key adjustment step
    result = weighted_sum + (len(base_values) ** 2)
    return result

# Global decoy variables
config_flag = True
debug_mode = False
temp_buffer = [0] * 10
log_entries = set()

# Input data
raw_data = [4, 7, 12, 9, 6, 15, 3, 8]
weights = [3, 7, 2, 5]

# Call irrelevant functions to create distractions
analyze_pattern(raw_data)
transform_data(raw_data, factor=5)
validate_checksum(raw_data)

# Actual execution point
final_score = calculate_final_score(raw_data, weights)

# Print result
print(f"Target result: {final_score}")