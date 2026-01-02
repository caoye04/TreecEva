import math

def preprocess_signal(raw_samples):
    # Irrelevant transformation (dead code path)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in raw_samples if x > sum(raw_samples) / len(raw_samples)]
    return filtered

def encode_sequence(seq):
    # Unused encoding function (distractor)
    return ''.join([format(int(x), 'b') for x in seq])

def compress_data(data_stream):
    shifted = [int(x * 1.5) ^ 3 for x in data_stream]  # Bit manipulation red herring
    inverted = [abs(x - 255) for x in shifted if x < 100]  # Partial filtering (misleading)
    return [x for x in data_stream if x % 2 == 1]  # Actual relevant compression: keep odd values

def validate_checksum(arr):
    # Complex but irrelevant checksum logic
    total = 0
    for i, val in enumerate(arr):
        total += val * (i + 1)
    return total % 17 == 0

def analyze_signal(signal, limit):
    # Core logic hidden among distractions
    base_score = 0
    
    # Distractor: string-based analysis on numeric data (never used)
    str_rep = ''.join(str(int(x)) for x in signal[:5])
    vowel_count = sum(1 for c in str_rep if c in '02468')  # Treating digits as "vowels"
    
    # Real computation begins
    sorted_vals = sorted(signal, reverse=True)
    top_quartile = sorted_vals[:len(sorted_vals)//4]
    
    # Multiple layers of filtering and transformation
    adjusted = []
    for v in top_quartile:
        if v > limit:
            adjusted.append(v // 2)
        else:
            adjusted.append(v)
    
    # Set operation to eliminate duplicates (relevant)
    unique_adjusted = list(set(adjusted))
    
    # Linear search for specific pattern
    found = False
    for i in range(len(unique_adjusted) - 1):
        if unique_adjusted[i] - unique_adjusted[i+1] == 2:
            base_score += 3
            found = True
            break
    
    if not found:
        base_score -= 1
    
    # Final computation with logical operations
    multiplier = 7 if (len(unique_adjusted) > 3 and sum(unique_adjusted) < 100) else 5
    final_score = base_score * multiplier + sum(x for x in unique_adjusted if x < 20)
    
    # Critical result
    return final_score

# Main execution with extensive irrelevant setup
raw_sensor_data = [12, 15, 22, 8, 9, 34, 18, 7, 41, 3, 29]
threshold = 15

# Dead code assignments (distractors)
data_stats = {
    'mean': sum(raw_sensor_data)/len(raw_sensor_data),
    'peak': max(raw_sensor_data),
    'entropy': math.log(len(raw_sensor_data)),
    'noise_floor': 0.5
}

# Unused transformations
encoded_str = encode_sequence(raw_sensor_data)
checksum_valid = validate_checksum(raw_sensor_data)

# Relevant preprocessing chain
filtered_data = preprocess_signal(raw_sensor_data)
compressed_data = compress_data(filtered_data)  # Only this matters

# Signal analysis with key logic
final_diagnostic = analyze_signal(compressed_data, threshold)

print(f"Result: {final_diagnostic}")