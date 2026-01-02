def analyze_metrics(raw_values, offset):
    processed = []
    temp_sum = 0
    for val in raw_values:
        if val < 0:
            adjusted = abs(val) * 2 + offset
        else:
            adjusted = val + offset // 3
        temp_sum += adjusted
        processed.append(adjusted)
    
    # Distractor: irrelevant transformation
    inverted = [1.0 / (x + 1) for x in processed if x != 0]
    avg_inverted = sum(inverted) / len(inverted) if inverted else 0

    # Semi-relevant normalization
    normalized = [round(p / temp_sum * 100, 2) for p in processed]
    return normalized, temp_sum, avg_inverted


def filter_outliers(data_list, limit):
    # Dead code path - never used in final logic
    if len(data_list) == 0:
        return []
    filtered = [x for x in data_list if x <= limit]
    return filtered if len(filtered) > 0 else data_list


def compute_baseline(ref_data):
    total = 0
    count = 0
    for item in ref_data:
        if isinstance(item, int) and item % 2 == 0:
            total += item ** 0.5
            count += 1
    # Irrelevant string operation distraction
    status_msg = "Processing complete".upper().replace(" ", "_")
    code_slice = status_msg[::2]
    return int(total) if count > 0 else 0


def evaluate_performance(metrics, threshold):
    score = 0
    penalty = 0
    
    for i, m in enumerate(metrics):
        if i % 2 == 0:
            score += int(m // 10)
        else:
            if m > threshold * 1.5:
                penalty += 1
    
    # Key logic step: final scoring with modular adjustment
    raw_score = score * (3 - penalty)
    final_score = (raw_score % 97) + 10  # Ensures positive small integer
    
    # Additional distraction: bitwise red herring
    mask = 0b1101
    masked_result = final_score ^ mask & 0b1010  # Computation not affecting output
    
    return final_score

# Main execution flow
base_threshold = 25
raw_input_data = [12, -8, 15, 22, -5, 30, 18]

# Step 1: Process metrics
norm_data, total_flow, inv_avg = analyze_metrics(raw_input_data, base_threshold)

# Step 2: Compute auxiliary baseline (not directly used)
baseline_value = compute_baseline(raw_input_data)

# Step 3: Evaluate performance using normalized metric values
final_score = evaluate_performance(norm_data, base_threshold)

# Step 4: Print result
print(f"Result: {final_score}")