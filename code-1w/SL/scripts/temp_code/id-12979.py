def calculate_performance(data):
    # Preprocessing: clean and normalize string-based metrics
    normalized = []
    for entry in data:
        clean_entry = entry.strip().lower()
        if 'error' not in clean_entry:
            normalized.append(clean_entry)
    
    # Extract numeric values using string methods and lambda filtering
    raw_values = []
    for item in normalized:
        parts = item.split(':')
        if len(parts) == 2:
            key, val_str = parts
            if val_str.replace('.', '').isdigit():
                raw_values.append(float(val_str))
    
    # Irrelevant distraction: process keys (not used in final score)
    key_analysis = list(map(lambda k: len(k.strip()), [p[0] for p in map(lambda x: x.split(':'), normalized) if len(x.split(':'))==2]))
    avg_key_length = sum(key_analysis) / len(key_analysis) if key_analysis else 0
    
    # Core logic: compute weighted harmonic mean of valid values
    filtered = [v for v in raw_values if v > 0]
    if not filtered:
        return 0.0
    
    # Summation with accumulation and conditional weighting
    total_weight = 0.0
    reciprocal_sum = 0.0
    for i, val in enumerate(filtered):
        weight = 1.0
        if i % 2 == 0:
            weight = 1.5  # Boost even-indexed benchmarks
        elif val > 50:
            weight = 0.8
        
        # Track cumulative stats (some unused)
        running_avg = sum(filtered[:i+1]) / (i+1)
        stability_score = running_avg / (val + 1e-5)
        
        total_weight += weight
        reciprocal_sum += weight / val
    
    # Final performance metric: weighted harmonic mean
    harmonic_mean = total_weight / reciprocal_sum if reciprocal_sum > 0 else 0
    
    # Secondary transformation: scale by pattern density
    pattern_flags = [1 if 'opt' in entry or 'fast' in entry else 0 for entry in data]
    enhancement_factor = 1 + (sum(pattern_flags) / len(data) * 0.2) if data else 1
    
    # Distractor computation: analyze character frequency (unused)
    all_chars = ''.join(data)
    char_freq = {c: all_chars.count(c) for c in set(all_chars) if c.isalpha()}
    vowel_ratio = sum(char_freq.get(v, 0) for v in 'aeiou') / max(sum(char_freq.values()), 1)
    
    # Final adjustment based on length trends (semi-relevant)
    lengths = [len(entry) for entry in data]
    length_trend = sum(lengths[i] - lengths[i-1] for i in range(1, len(lengths))) if len(lengths) > 1 else 0
    
    # Final score calculation
    base_score = harmonic_mean * enhancement_factor
    penalty = 0.95 if length_trend < 0 else 1.0
    final_score = base_score * penalty
    
    # Debug print (not counted)
    # print(f'Avg key length: {avg_key_length}, Vowel ratio: {vowel_ratio}, Trend: {length_trend}')
    return final_score

# Input data with mixed quality indicators
benchmark_data = [
    "  SystemA: 45.2  ",
    "Error: failed to initialize",
    "OptimizedModule: 67.8",
    "LegacyComponent: 30.1",
    "FastPipeline: 88.5",
    "Analyzer: 52.0",
    "DeprecatedTool: 10.3"
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")