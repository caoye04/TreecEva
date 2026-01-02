def preprocess_data(raw):
    cleaned = []
    outlier_count = 0
    total_sum = 0
    
    for x in raw:
        if isinstance(x, str) and x.isdigit():
            val = int(x)
        elif isinstance(x, (int, float)):
            val = x
        else:
            continue
            
        if val < 0 or val > 100:
            outlier_count += 1
            continue
            
        cleaned.append(val)
        total_sum += val

    avg = total_sum / len(cleaned) if cleaned else 0
    adjusted = [c - avg for c in cleaned]
    return adjusted


def calculate_entropy(arr):
    # Irrelevant helper function for distraction
    from math import log2
    freq = {}
    for a in arr:
        freq[a] = freq.get(a, 0) + 1
    entropy = 0
    n = len(arr)
    for count in freq.values():
        p = count / n
        entropy -= p * log2(p)
    return round(entropy, 4)


def calculate_final_score(data, weight_map):
    base_scores = {}
    temp_results = []
    adjustment_factor = 0.85
    
    for i, d in enumerate(data):
        key = f"item_{i % 5}"
        weight = weight_map.get(key, 1.0)
        
        # Apply transformation using modular arithmetic and scaling
        transformed = (d ** 2) % 97
        scaled = transformed * adjustment_factor
        
        if scaled > 50:
            scaled = 50 + (scaled - 50) * 0.5  # Diminishing returns
        
        base_scores[key] = base_scores.get(key, 0) + scaled
        temp_results.append(scaled)

    # Compute aggregate statistics
    mean_val = sum(temp_results) / len(temp_results) if temp_results else 0
    variance = sum((tr - mean_val) ** 2 for tr in temp_results) / len(temp_results) if temp_results else 0
    std_dev = variance ** 0.5
    
    # Final weighted aggregation
    weighted_sum = 0
    total_weight = 0
    for k, v in base_scores.items():
        w = weight_map.get(k, 1.0)
        weighted_sum += v * w
        total_weight += w
    
    final_raw = weighted_sum / total_weight if total_weight else 0
    
    # Normalize to 0-100 scale
    normalized = (final_raw / 60) * 100
    
    # Clamp result
    clamped = max(0, min(100, normalized))
    
    # Distractor: unused complex string analysis
    debug_info = "Scores processed: " + ", ".join([f"{k}:{v:.2f}" for k, v in base_scores.items()])
    debug_hash = sum(ord(c) for c in debug_info) % 1000
    
    # Final adjustment based on length pattern
    length_code = len(temp_results) % 7
    final_score = clamped * (1 + (length_code * 0.01))
    
    return round(final_score, 2)

# Main execution
raw_input_data = [85, '90', 78, None, 'abc', 92, 88, 105, -5, 96, '87', 76, 89]
weights = {"item_0": 1.2, "item_1": 1.5, "item_2": 0.8, "item_3": 1.0, "item_4": 0.9}

processed_data = preprocess_data(raw_input_data)
entropy = calculate_entropy(processed_data)  # Unused but distracting

final_score = calculate_final_score(processed_data, weights)
print(f"Result: {final_score}")