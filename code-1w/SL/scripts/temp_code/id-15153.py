import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Misleading transformation with decoy logic
def decoy_transform(values):
    temp_result = 0
    for i in range(len(values)):
        if i % 2 == 0:
            temp_result += values[i] * 1.5
        else:
            temp_result -= values[i] * 0.5
    return temp_result  # Never used in actual computation

# Real processing function with embedded distractions
def preprocess_records(raw_entries):
    filtered = []
    total_chars = 0
    decoy_sum = 0  # Distractor variable

    for entry in raw_entries:
        stripped = entry.strip().lower()
        total_chars += len(stripped)

        # Real filtering condition
        if len(stripped) > 3 and stripped[0] != '#':
            try:
                num = float(stripped)
                filtered.append(num)
            except ValueError:
                # Character counting side task (partially relevant)
                letter_count = sum(1 for c in stripped if c.isalpha())
                decoy_sum += letter_count % 7  # Meaningless accumulation

    # List comprehension: relevant transformation
    processed = [abs(x) for x in filtered if x != 0]

    # Sorting is needed for downstream logic
    processed.sort(reverse=True)

    # Extra distraction: bit manipulation with no real effect
    bit_fiddle = 0
    for p in processed:
        if p > 5:
            bit_fiddle ^= int(p) & 0xFF

    return processed, total_chars

# Core logic obscured by multiple layers
def analyze_distribution(data_list):
    n = len(data_list)
    if n == 0:
        return 0.0

    # Compute quartiles using simple loops
    q1_idx = n // 4
    q3_idx = 3 * n // 4
    median_idx = n // 2

    sorted_data = data_list[:]  # Already sorted, but reassignment adds confusion

    q1 = sorted_data[q1_idx]
    q3 = sorted_data[q3_idx]
    median = sorted_data[median_idx]

    iqr = q3 - q1
    outlier_threshold = q3 + 1.5 * iqr

    # Use list comprehension to filter potential outliers
    clean_data = [x for x in data_list if x <= outlier_threshold]

    # Return trimmed mean
    return sum(clean_data) / len(clean_data) if clean_data else 0.0

# Final scoring with red herring parameters
def compute_final_score(data_chunk):
    base_value = 0
    penalty = 0.0
    bonus_tracker = []  # Unused list

    # Simulate complex business logic
    for idx, val in enumerate(data_chunk):
        if idx % 3 == 0:
            base_value += math.floor(val)
        elif idx % 4 == 0:
            base_value -= int(val % 3)
        else:
            base_value += int(math.sqrt(val)) if val >= 1 else 1

    # Real adjustment
    avg_val = sum(data_chunk) / len(data_chunk)
    size_factor = len(data_chunk) ** 0.5

    # Critical calculation buried among distractions
    raw_score = base_value * size_factor
    normalized = raw_score / (avg_val + 1e-8)

    # Decoy branching logic
    if raw_score > 100:
        scaling = 0.9
    elif raw_score < 50:
        scaling = 1.1
    else:
        scaling = 1.0  # Actual path taken

    # Final result
    final = int(normalized * scaling)

    # Irrelevant post-processing
    checksum = 0
    for c in str(final):
        checksum ^= ord(c)

    return final

# Main execution flow
if __name__ == '__main__':
    # Input data with comments and noise
    raw_input_data = [
        "  4.5 ",     # Valid entry
        "  #comment ", # Skipped due to #
        "  -2.3  ",   # Will be abs()'d later
        "  abc123  ", # Invalid number, contributes to letter count
        "  8.7  ",    # Valid
        "  0.0  ",    # Filtered out (zero)
        "  15.2 ",    # Valid
        "  hello  ",  # Only letters counted in decoy_sum
        "  6.1  ",    # Valid
        "  3.3  "     # Valid
    ]

    # Preprocess: returns both numeric data and metadata
    processed_data, char_count = preprocess_records(raw_input_data)

    # Secondary analysis (distraction)
    distribution_metric = analyze_distribution(processed_data)

    # Apply decoy transform on wrong data type (never used)
    _ = decoy_transform([int(x) for x in processed_data])

    # Key statement containing target variable
    final_score = compute_final_score(processed_data)

    # Output result as required
    print(f"Result: {final_score}")