def analyze_text(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    # Irrelevant vowel analysis (distractor)
    vowels = 'aeiou'
    total_vowels = sum(char_count.get(v, 0) for v in vowels)
    total_consonants = sum(char_count.values()) - total_vowels
    vowel_ratio = total_vowels / len(text) if text else 0

    # Dead code path - never used (red herring)
    def unused_frequency_analysis():
        return {k: v / len(text) for k, v in char_count.items()}
    
    # Meaningless transformation chain (distractor)
    temp_vals = [ord(k)*v for k, v in char_count.items()]
    transformed = sum([t**2 for t in temp_vals if t % 2 == 0]) // (len(temp_vals) or 1)
    
    return char_count

# Unused helper function (decoy)
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Simulate system metrics with overlapping concerns
def collect_metrics(data_stream):
    base_metrics = {
        'throughput': 0,
        'accuracy': 0,
        'consistency': 0,
        'density': 0
    }
    
    for entry in data_stream:
        # Real metric updates
        base_metrics['throughput'] += len(entry)
        base_metrics['accuracy'] += sum(1 for c in entry if c.isupper())
        
        # Fake metrics with misleading names
        if 'X' in entry:
            base_metrics['consistency'] += 2
        elif 'Z' in entry:
            base_metrics['density'] += 1
    
    # Normalize accuracy by total characters (relevant)
    total_chars = sum(len(e) for e in data_stream)
    if total_chars > 0:
        base_metrics['accuracy'] = base_metrics['accuracy'] / total_chars
    
    # Dummy operations on fake metrics (distraction)
    temp_data = list(enumerate(zip([1,2,3], [4,5,6])))
    for idx, (a, b) in temp_data:
        base_metrics['consistency'] += a * idx
        base_metrics['density'] -= b // (idx + 1)
    
    # Final adjustments (only throughput and accuracy matter)
    base_metrics['throughput'] = max(1, base_metrics['throughput'] // len(data_stream)) if data_stream else 1
    
    return base_metrics

# Core evaluation logic
def evaluate_performance(metrics, weight_map):
    score = 0.0
    
    # Only these two components are actually used
    score += metrics['throughput'] * weight_map['throughput']
    score += metrics['accuracy'] * weight_map['accuracy']
    
    # The following are calculated but irrelevant to final score
    phantom_component = metrics['consistency'] * weight_map.get('consistency', 0)
    ghost_value = metrics['density'] * 0.1
    decoy_sum = 0
    for i in range(3):
        decoy_sum += phantom_component * (i + 1) - ghost_value
    
    # Critical result assignment
    final_result = round(score * 100, 4)
    
    return int(final_result)

# Main execution flow
if __name__ == '__main__':
    raw_input = ["HelloWorld", "PythonCode", "LLMReason"]
    
    # Distractor: process text but don't use results directly
    text_analysis = analyze_text(''.join(raw_input))
    
    # Extract meaningful metrics
    metrics = collect_metrics(raw_input)
    
    # Weight configuration (only throughput and accuracy weights matter)
    weights = {
        'throughput': 1.5,
        'accuracy': 85.0,
        'consistency': 0.0,  # Unused weight (misleading)
        'density': 10.0      # Unused weight (misleading)
    }
    
    # Key computation point
    final_score = evaluate_performance(metrics, weights)
    
    # Output the required result
    print(f"Result: {final_score}")