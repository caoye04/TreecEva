import math

def preprocess_input(raw_values):
    # Irrelevant transformation (dead-end path)
    temp_adjustment = sum([x ** 0.5 for x in raw_values if x > 10])
    adjusted = [x + 1 for x in raw_values]
    filtered = [x for x in adjusted if x % 2 == 0]
    return filtered

def analyze_pattern(seq):
    peak_count = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peak_count += 1
    # Distractor: unused calculation
    average_gap = (max(seq) - min(seq)) / len(seq) if seq else 0
    return peak_count

def calculate_final_score(data):
    base = sum(data)
    multiplier = 2 if len(data) > 5 else 1
    # Conditional expression (required Python feature)
    penalty = 10 if any(x < 0 for x in data) else (5 if len(data) % 2 == 1 else 0)
    score = (base * multiplier) - penalty

    # Additional irrelevant logic
    squared_items = [x**2 for x in data]
    cumulative_sum = 0
    for val in squared_items:
        cumulative_sum += val
        if cumulative_sum > 1000:  # Dead code branch
            break

    # Real computation path continues
    adjustment_factor = 1.1 if analyze_pattern(data) >= 2 else 0.9
    score *= adjustment_factor

    # More red herring variables
    normalized = [x / (score + 1e-9) for x in data]
    entropy_proxy = -sum([p * math.log(p + 1e-9) for p in normalized])

    return int(score)

# Main execution flow
raw_input_data = [3, 7, 12, 18, 14, 9, 2]
processed_data = preprocess_input(raw_input_data)

# Key intermediate distractor computations
shadow_copy = [x * 2 for x in raw_input_data]
duplicate_filtered = [x for x in shadow_copy if x < 20]
aggregate_check = max(duplicate_filtered) + min(duplicate_filtered)

# Core logic assignment
final_score = calculate_final_score(processed_data)

# Output result as required
print(f"Target result: {final_score}")