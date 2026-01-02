def analyze_metrics(values, weights):
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    norm_factor = max(values) if values else 1
    normalized = [v / norm_factor for v in values]
    return weighted_sum, normalized


def filter_outliers(entries, limit):
    # Irrelevant filtering (not used in final result)
    clean = [e for e in entries if abs(e - sum(entries)/len(entries)) < limit]
    return clean or entries


def compute_final_score(raw_data, config):
    # Distractor variables
    temp_buffer = []
    debug_log = []
    
    for item in raw_data:
        if isinstance(item, str):
            # Use string method (semi-relevant)
            processed = item.strip().upper()
            ascii_vals = [ord(c) for c in processed if c.isalpha()]
            temp_buffer.extend(ascii_vals)
        else:
            temp_buffer.append(item * 2)  # Distraction: doubles values but not used directly
    
    # Actual relevant data path
    numeric_data = [x for x in raw_data if isinstance(x, (int, float))]
    weights = [1.0, 0.5, 0.25] * (len(numeric_data)//3 + 1)
    weights = weights[:len(numeric_data)]
    
    # Key computation chain
    score_base, normalized_data = analyze_metrics(numeric_data, weights)
    
    adjustment = 0
    for i, val in enumerate(normalized_data):
        if i % 2 == 0 and val > 0.5:
            adjustment += 0.1
        elif i % 2 == 1:
            adjustment -= 0.05
    
    # Secondary distractor loop
    history = {}
    for idx in range(len(normalized_data)):
        key = f"entry_{idx}"
        history[key] = round(normalized_data[idx], 3)
        if idx > 5:  # Dead code path
            break
    
    # Core logic with modular arithmetic influence
    mod_contrib = 0
    for v in numeric_data:
        mod_contrib += (v * 7) % 4
    
    # Final score formation (only some components are actually used)
    base_component = score_base * 0.8
    mod_component = mod_contrib * 1.2
    final_score = int(base_component + mod_component + adjustment * 10)
    
    # This print is required to show result
    print(f"Result: {final_score}")
    
    return final_score

# Input data with mixed types (string + numbers)
data = [12, " log2x ", 16, 8, "data", 20]
thresholds = {'upper': 25, 'lower': 5}

# Execute main computation
final_score = compute_final_score(data, thresholds)