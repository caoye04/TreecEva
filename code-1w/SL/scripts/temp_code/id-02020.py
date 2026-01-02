def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts


def extract_features(data_list):
    feature_map = {}
    temp_sum = 0
    
    for i, value in enumerate(data_list):
        if value % 3 == 0:
            temp_sum += value * 2
        elif value % 5 == 0:
            temp_sum -= value // 2
        
        # Irrelevant tracking
        feature_map[f'idx_{i}'] = value ** 0.5 if value > 0 else 0
    
    # Dead computation path (not used later)
    special_value = sum(x for x in data_list if x > 10 and x % 2 == 0)
    
    return [x for x in data_list if x > 0], temp_sum


def validate_structure(items):
    stack = []
    errors = 0
    for item in items:
        if item < 0:
            errors += 1
            continue
        stack.append(item)
    return len(stack) > 0 and errors == 0


def calculate_adjusted_score(records):
    base = 0
    multiplier = 1
    
    # Use of zip to align two derived sequences
    indices = list(range(len(records)))
    for idx, val in zip(indices, records):
        if idx % 2 == 0:
            base += val * 3
        else:
            base -= val
        
        # Distractor: cumulative product not used
        multiplier *= (val % 7) or 1
    
    # Additional irrelevant logic
    outlier_count = sum(1 for x in records if x > 50)
    adjustment = 5 if outlier_count > 2 else 0
    
    return base + adjustment

# Main execution flow
raw_input = [12, -5, 15, 8, 21, 0, 10, 25]

# Step 1: Analyze raw frequency (semi-relevant)
freq_analysis = analyze_pattern([x % 4 for x in raw_input if x >= 0])

# Step 2: Extract features with side outputs
processed_data, interim_total = extract_features(raw_input)

# Step 3: Validate structure (result not used directly but affects confidence)
is_valid = validate_structure(raw_input)

# Step 4: Key computation step
final_score = calculate_adjusted_score(processed_data)

print(f"Result: {final_score}")