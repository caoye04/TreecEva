def analyze_trends(data):
    trend_flags = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_flags.append(1)
        elif data[i] < data[i-1]:
            trend_flags.append(-1)
        else:
            trend_flags.append(0)
    return trend_flags


def filter_outliers(seq, threshold=2):
    mean_val = sum(seq) / len(seq)
    deviances = [abs(x - mean_val) for x in seq]
    filtered = [seq[i] for i in range(len(seq)) if deviances[i] <= threshold]
    return filtered if len(filtered) > 0 else seq


def transform_sequence(raw_seq):
    shifted = [x * 2 + 1 for x in raw_seq]
    reversed_slice = shifted[::-1]
    mid_section = reversed_slice[1:-1]
    normalized = [x / 2 for x in mid_section]
    return [round(x) for x in normalized]


def calculate_final_score(entries):
    base_total = sum(entries)
    bonus = 0
    
    if len(entries) > 5:
        bonus += 10
    elif len(entries) == 3:
        bonus += 5
    
    even_count = len([x for x in entries if x % 2 == 0])
    if even_count >= 2:
        bonus += 7
    
    unique_vals = set(entries)
    duplicate_penalty = len(entries) - len(unique_vals)
    
    temp_result = base_total + bonus - (duplicate_penalty * 3)
    
    # Irrelevant tracking variables
    state_log = []
    for idx, val in enumerate(entries):
        if val > 10:
            state_log.append(f"High at {idx}")
        elif val < 0:
            state_log.append(f"Negative at {idx}")
    
    # Unused transformation
    dummy_shift = [x + 5 for x in entries if x < 0]
    shadow_sum = sum(dummy_shift) if dummy_shift else 0
    
    # Actual score calculation
    adjustment = 0
    if base_total > 0 and len(unique_vals) > 1:
        adjustment = len(entries) // 2
    
    final_score = temp_result + adjustment
    
    # Dead code branch (never reached due to logic above)
    if shadow_sum > 1000:
        final_score -= 50
        
    return final_score

# Main execution
raw_input = [3, 7, 7, 1, 9, 4, 4]

# Step 1: Analyze trend direction (not used in final score but part of distraction)
trend_analysis = analyze_trends(raw_input)

# Step 2: Filter outliers with arbitrary threshold
cleaned_data = filter_outliers(raw_input, threshold=1.5)

# Step 3: Transform sequence through multiple stages
transformed = transform_sequence(cleaned_data)

# Step 4: Process data into usable format
processed_data = []
for val in transformed:
    if val > 0:
        processed_data.append(val)
    else:
        processed_data.append(1)

# Ensure we have at least some data
if len(processed_data) == 0:
    processed_data = [1]

# Add artificial padding (distractor)
padded_data = [0] + processed_data + [0]
diagnostic_sum = sum(padded_data[::2])  # Used nowhere

# Critical statement
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")