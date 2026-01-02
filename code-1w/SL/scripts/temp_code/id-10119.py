from collections import defaultdict, Counter

def preprocess_data(raw):
    # Irrelevant preprocessing step (not used in final logic)
    cleaned = [x for x in raw if isinstance(x, int) and x > 0]
    stats = defaultdict(int)
    for val in cleaned:
        stats['count'] += 1
        stats['sum'] += val
    return stats  # This return value is unused in main logic

def calculate_entropy(values):
    # Distractor function: calculates entropy but not used
    freqs = Counter(values)
    total = len(values)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * p  # Simplified placeholder
    return round(entropy, 4)

def calculate_final_score(data, threshold_config):
    # Core logic begins
    valid_entries = []
    temp_debug_log = []
    
    for idx, (key, values) in enumerate(data.items()):
        if idx % 2 == 0:  # Only process even-indexed keys
            item_total = sum(values)
            item_count = len(values)
            average = item_total / item_count if item_count else 0
            
            # Tracking intermediate state (some used, some not)
            temp_debug_log.append((key, item_total, average))
            
            high_vals = [v for v in values if v > threshold_config['high']]
            if len(high_vals) >= threshold_config['min_high_count']:
                valid_entries.append(average)
    
    # Secondary filtering based on length (semi-relevant)
    filtered_averages = [avg for avg in valid_entries if avg >= threshold_config['base']]
    
    # Dummy counting with zip and enumerate (moderately distracting)
    indexed_avgs = list(enumerate(filtered_averages))
    pair_sums = []
    for i, avg_val in indexed_avgs:
        if i > 0:
            prev_avg = filtered_averages[i-1]
            pair_sums.append(prev_avg + avg_val)
    
    # Final score computation (only this matters)
    base_score = sum(filtered_averages)
    bonus = len(pair_sums) * 0.5  # Bonus for consecutive qualifying groups
    final_score = base_score + bonus
    
    # Red herring variable
    outlier_count = sum(1 for v in flat_data(data) if v < 5)
    
    return round(final_score, 4)

def flat_data(nested):
    # Helper to flatten data (used once)
    result = []
    for vals in nested.values():
        result.extend(vals)
    return result

def main():
    # Input data
    raw_data = {
        'A': [12, 15, 23, 8],
        'B': [5, 6, 9],
        'C': [18, 19, 25, 21],
        'D': [3, 4, 7, 9],
        'E': [20, 22, 24]
    }
    
    config = {
        'high': 20,
        'min_high_count': 2,
        'base': 15
    }
    
    # Unused variables (distractors)
    summary_stats = preprocess_data([item for sublist in raw_data.values() for item in sublist])
    entropy = calculate_entropy(flat_data(raw_data))
    
    # Key execution point
    final_score = calculate_final_score(raw_data, config)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()