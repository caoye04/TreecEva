import collections

def process_data_sources():
    raw_data = [3, 7, 2, 8, 5, 3, 9, 2, 7, 8, 4, 6, 1, 5, 3]
    irrelevant_cache = [x * 2 for x in raw_data if x > 4]
    data_counter = collections.Counter(raw_data)
    
    # Misleading intermediate calculations
    temp_sum = sum(raw_data) + len(irrelevant_cache)
    bogus_factor = temp_sum % 7
    
    most_common = data_counter.most_common(2)
    if len(most_common) >= 2:
        primary_freq = most_common[0][1]
        secondary_freq = most_common[1][1]
    else:
        primary_freq = 0
        secondary_freq = 0
    
    # Dead code path that looks important
    if bogus_factor > 3:
        quality_indicator = primary_freq * 10 - secondary_freq
    else:
        quality_indicator = primary_freq + secondary_freq * 5
    
    return quality_indicator, bogus_factor

def analyze_patterns():
    sample_sequences = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
    pattern_metrics = []
    
    for seq in sample_sequences:
        avg_val = sum(seq) / len(seq)
        pattern_metrics.append(avg_val)
    
    # Misleading operation that gets ignored
    pattern_sum = sum(pattern_metrics) * 3
    variance_factor = max(pattern_metrics) - min(pattern_metrics)
    
    return variance_factor, pattern_sum

def final_processing():
    quality_indicator, bogus_factor = process_data_sources()
    variance_factor, pattern_sum = analyze_patterns()
    
    # Key computation chain
    base_score = quality_indicator + variance_factor
    adjustment = (bogus_factor * 2) % 5
    
    # Multiple irrelevant operations
    dummy_calc = (pattern_sum // 10) + 25
    misleading_value = dummy_calc - adjustment
    
    # Critical calculation
    data_quality_score = base_score - adjustment
    
    # Print the target variable
    print(f"Target result: {data_quality_score}")
    return data_quality_score

# Execute the main processing
if __name__ == "__main__":
    final_processing()