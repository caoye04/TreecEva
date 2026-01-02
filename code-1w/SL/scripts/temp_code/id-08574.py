def analyze_sample(sample_str):
    char_count = {}
    for char in sample_str.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Distractor: unused computation
    entropy = 0.0
    total_chars = sum(char_count.values())
    for count in char_count.values():
        p = count / total_chars
        entropy -= p * __import__('math').log2(p)
    
    # Semi-relevant transformation
    normalized_freq = [count / total_chars for count in char_count.values()]
    avg_freq = sum(normalized_freq) / len(normalized_freq) if normalized_freq else 0
    
    return avg_freq * 100


def filter_outliers(data_list):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (__import__('math').sqrt(sum((x - mean_val) ** 2 for x in data_list) / len(data_list)))
    filtered = [x for x in data_list if abs(x - mean_val) <= 2 * std_dev]
    return filtered if len(filtered) > 0 else data_list


def compute_robust_trend(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    q1 = sorted_vals[n // 4]
    q3 = sorted_vals[3 * n // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Distractor: dead code path (never used)
    extreme_lower = q1 - 3.0 * iqr
    extreme_upper = q3 + 3.0 * iqr
    
    trimmed = [v for v in values if lower_bound <= v <= upper_bound]
    return sum(trimmed) / len(trimmed) if trimmed else 0


def harvest_results(raw_data):
    processed_scores = []
    
    for idx, entry in enumerate(raw_data):
        text_block = entry['content']
        base_score = analyze_sample(text_block)
        
        # Use of enumerate and string method: case conversion
        tag_weight = len([c for c in entry['tags'] if c.upper() == 'CRITICAL']) * 1.5
        
        weighted_score = base_score + tag_weight
        processed_scores.append(weighted_score)
        
        # Distractor: irrelevant tracking
        debug_info = f"Processed {idx+1}: '{text_block[:10]}...'")

    cleaned_scores = filter_outliers(processed_scores)
    trend = compute_robust_trend(cleaned_scores)
    
    # Key logic step: apply combinatorics adjustment based on number of entries
    n = len(raw_data)
    combination_factor = __import__('math').factorial(n) // (__import__('math').factorial(n-2) * __import__('math').factorial(2)) if n >= 2 else 0
    adjustment = combination_factor / 100.0
    
    final_yield = trend + adjustment
    
    # Print required for deterministic output visibility
    print(f"Result: {final_yield}")
    return final_yield

# Simulated experiment data
experiment_data = [
    {'content': 'ACGTGCTAGCT', 'tags': ['normal', 'analyzed']},
    {'content': 'TTAACCGGTTT', 'tags': ['normal', 'CRITICAL']},
    {'content': 'GGGAAATTTCCC', 'tags': ['CRITICAL']},
    {'content': 'ATGCATGCATGC', 'tags': ['normal']}
]

# Execution point
final_yield = harvest_results(experiment_data)