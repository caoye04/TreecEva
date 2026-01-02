def normalize_values(data):
    max_val = max(data)
    return [round(x / max_val, 6) for x in data]

# Irrelevant helper function (dead code path)
def deprecated_scale(data):
    return [x * 2 for x in data if x < 5]

# Another decoy function with misleading logic
def compute_legacy_metric(vals):
    temp = 0
    for i in range(len(vals)):
        temp += (i + 1) * vals[i] % 7
    return temp // 3

# Complex weighting with distractor logic
def apply_weighting(values, factors):
    if len(values) != len(factors):
        raise ValueError('Mismatched lengths')
    weighted = []
    for i in range(len(values)):
        # Some irrelevant bit manipulation distraction
        bit_shifted = (i ^ 5) & 3
        adjusted_factor = factors[i] + (bit_shifted * 0.05)
        weighted.append(values[i] * adjusted_factor)
    return weighted

# Red herring: string-based computation that seems important
def extract_priority_code(tag_list):
    codes = []
    for tag in tag_list:
        clean_tag = tag.strip().lower().replace('_', '')
        if 'high' in clean_tag:
            codes.append(3)
        elif 'med' in clean_tag:
            codes.append(2)
        else:
            codes.append(1)
    return codes

# Main evaluation logic hidden among distractions
def evaluate_performance(raw_metrics, weight_vector):
    # Step 1: Normalize input metrics
    normalized = normalize_values(raw_metrics)
    
    # Distractor: unused transformation
    inverted = [1 - x for x in normalized if x > 0.5]
    inverted_sum = sum(inverted) * 0.1  # Used nowhere
    
    # Step 2: Apply complex weighting
    scored = apply_weighting(normalized, weight_vector)
    
    # Step 3: Conditional adjustment based on threshold pattern
    adjusted_scores = []
    for val in scored:
        if val > 0.4:
            adjusted_scores.append(val * 1.1)
        elif val < 0.2:
            adjusted_scores.append(val * 0.9)
        else:
            adjusted_scores.append(val)
    
    # Step 4: Aggregate with rounding
    aggregate = sum(adjusted_scores)
    
    # Step 5: Apply arbitrary domain-specific cap
    capped = min(aggregate, 4.85)
    
    # Final adjustment based on length parity (misleading but deterministic)
    if len(weight_vector) % 2 == 0:
        capped -= 0.07
    
    return round(capped, 6)

# --- Input Data (with extra irrelevant entries) ---
data_metrics = [85, 92, 78, 96, 88]
weight_scheme = [0.2, 0.3, 0.15, 0.25, 0.1]
priority_tags = ['high_priority', 'normal_flow', 'high_critical', 'low_latency']

# Unused intermediate computations (distractors)
temp_normalized = normalize_values(data_metrics)
legacy_score = compute_legacy_metric([70, 80, 90])
scaled_legacy = deprecated_scale([1, 2, 3, 4, 5])
priorities = extract_priority_code(priority_tags)

# Key statement
final_score = evaluate_performance(data_metrics, weight_scheme)

print(f"Result: {final_score}")