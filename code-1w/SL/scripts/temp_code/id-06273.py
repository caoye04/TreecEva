def analyze_text_patterns(input_str):
    chars = list(input_str)
    char_freq = {}
    for c in chars:
        char_freq[c] = char_freq.get(c, 0) + 1
    unique_chars = set(chars)
    repeated = {k for k, v in char_freq.items() if v > 1}
    return unique_chars, repeated


def compute_hash_value(data):
    hash_val = 0
    for i, ch in enumerate(data):
        hash_val += (i + 1) * ord(ch)
    return hash_val % 1000


def extract_segments(text, delimiter=' '):
    segments = text.split(delimiter)
    segment_lengths = [len(s) for s in segments]
    total_length = sum(segment_lengths)
    avg_length = total_length / len(segment_lengths) if segments else 0
    return segments, segment_lengths, avg_length


def evaluate_performance(metrics, data_samples):
    base_score = 0
    penalty = 0
    
    # Relevant logic: count overlap between metrics and sample keys
    key_overlap = metrics.intersection(set(data_samples.keys()))
    base_score += len(key_overlap) * 10
    
    # Distraction: process string data unnecessarily
    dummy_text = "sample text for analysis"
    _, repeated_chars = analyze_text_patterns(dummy_text)
    if len(repeated_chars) > 3:
        penalty += 5
    
    # Semi-relevant: compute hash but only use conditionally
    hash_code = compute_hash_value("evaluation_key_2024")
    if hash_code < 500:
        base_score += 2
    
    # Distractor: segment extraction with no impact
    raw_input = "alpha beta gamma delta epsilon"
    parts, lengths, average_len = extract_segments(raw_input)
    temp_sum = sum(l for l in lengths if l > 4)
    adjustment = temp_sum // 10 if temp_sum > 0 else 0  # unused
    
    # Real logic continues
    sample_count = len(data_samples)
    if sample_count > 0:
        base_score += (sample_count // 2) * 3
    
    final_score = base_score - penalty
    return final_score

# Main execution
metric_set = {'precision', 'recall', 'f1_score', 'accuracy', 'coverage'}
benchmark_data = {
    'precision': 0.92,
    'recall': 0.85,
    'latency_ms': 45,
    'memory_usage': 'low',
    'f1_score': 0.88
}

interim_result = compute_hash_value('temp')
dummy_overlap = analyze_text_patterns('aabbcc')

final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Target result: {final_score}")