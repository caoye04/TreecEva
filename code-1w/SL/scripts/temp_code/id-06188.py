def analyze_sequence(seq):
    """Misleading function that appears relevant but is never called."""
    temp_sum = 0
    for i in range(len(seq)):
        temp_sum += seq[i] * (i + 1)
    return temp_sum // 2 if temp_sum > 0 else 0


def preprocess_chunk(chunk):
    """Applies transformations, some of which are irrelevant."""
    a = [x ** 2 for x in chunk if x % 2 == 1]  # Only odd squares
    b = [x // 2 for x in chunk if x > 5]       # Distractor: unused later
    c = [x for x in chunk if x < 7][::-1]      # Reversed small values, partially used
    return a[:3] + c[:2]


def filter_and_shift(data):
    """Performs bit shifts and filtering with red herring logic."""
    shifted = []
    for val in data:
        if val & 1:  # if odd
            shifted.append(val << 1)  # left shift
        elif val % 4 == 0:
            shifted.append(val >> 1)  # right shift
        else:
            shifted.append(val)  # unchanged
    return shifted[1:-1]  # slice out edges


def compute_moving_average(series, window=3):
    """Dead code path – looks important but not used in final computation."""
    averages = []
    for i in range(len(series) - window + 1):
        averages.append(sum(series[i:i+window]) / window)
    return averages


def extract_key_features(arr):
    """Extracts features using slicing and conditional logic."""
    n = len(arr)
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Real computation starts here
    feature_1 = sum(left_half) * 2
    feature_2 = min(right_half) + max(left_half)
    feature_3 = (arr[1] ^ arr[-2]) & 7  # XOR + bitmask
    
    # Irrelevant transformation chain
    temp_arr = [x + feature_3 for x in arr]
    temp_arr = [x for x in temp_arr if x % 3 != 0]
    
    # This slice is critical
    core_segment = arr[2:7:2]  # takes indices 2,4,6
    feature_4 = sum(core_segment) - len(core_segment)
    
    return feature_1, feature_2, feature_3, feature_4


def calculate_final_score(data):
    """Main scoring logic with hidden key steps."""
    # Step 1: Use only specific part of data
    subset = data[1::2]  # Take every second element starting from index 1
    
    # Step 2: Apply real preprocessing
    processed_subset = preprocess_chunk(subset)
    
    # Step 3: Shift-based transformation
    shifted_vals = filter_and_shift(processed_subset)
    
    # Step 4: Extract actual features
    f1, f2, f3, f4 = extract_key_features(shifted_vals)
    
    # Step 5: Construct score with decoy variables
    base_score = f1 + f2
    adjustment = f3 * 3.5
    penalty = len(processed_subset) * 2
    bonus = 10 if len(shifted_vals) > 3 else 5
    
    # Misleading complex expression (partially dead)
    noise_factor = 0
    for i in range(3):
        noise_factor += (adjustment / (i + 1)) if i % 2 == 0 else 0
    
    # Final computation
    final_score = base_score + adjustment - penalty + bonus
    return int(final_score)

# --- Main execution ---
raw_input = [3, 8, 1, 4, 7, 2, 5, 9, 6]

# Unused but plausible computations (distractors)
decoy_analysis = analyze_sequence(raw_input)
moving_stats = compute_moving_average(raw_input, 2)

# Actual processing pipeline
processed_data = raw_input.copy()
processed_data.append(sum(raw_input[:4]))
processed_data.insert(0, processed_data[-1] // 3)

# Key statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")