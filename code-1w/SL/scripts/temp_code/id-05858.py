def analyze_sequence(pattern):
    count_upper = sum(1 for c in pattern if c.isupper())
    count_lower = sum(1 for c in pattern if c.islower())
    normalized = (count_upper - count_lower) ** 2
    return normalized if normalized > 0 else 1


def compute_statistics(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    adjusted_variance = max(variance, 0.1)
    return mean_val, adjusted_variance

def extract_segments(text_blocks):
    segments = []
    for idx, block in enumerate(text_blocks):
        if idx % 2 == 0:
            segments.append(block.strip().upper())
        else:
            segments.append(block.strip().lower())
    return segments

def compute_performance(data):
    # Irrelevant pre-processing (distractor)
    temp_buffer = [len(item) for item in data['texts']]
    avg_length = sum(temp_buffer) / len(temp_buffer)
    deviation_penalty = abs(avg_length - 10) * 0.5
    
    # Key transformation: extract and transform text segments
    processed = extract_segments(data['texts'])
    
    # Analyze each transformed segment
    scores = []
    for seg in processed:
        analysis_score = analyze_sequence(seg)
        scores.append(analysis_score)
    
    # Compute statistical properties (only mean used later)
    mean_score, var_score = compute_statistics(scores)
    
    # Simulate environmental interference (mostly irrelevant)
    interference_level = 0
    for i in range(len(data['texts'])):
        if i % 3 == 0:
            interference_level += 2
        elif i % 5 == 0:
            interference_level += 1
    
    # Core logic chain
    base_metric = mean_score * data['multiplier']
    adjustment_factor = 1 + (deviation_penalty / 10)
    applied_adjustment = base_metric * adjustment_factor
    
    # Secondary path: sequence validation
    validation_chain = [analyze_sequence(s.upper()) for s in data['texts'] if s]
    validation_sum = sum(validation_chain)
    validation_norm = validation_sum / len(validation_chain)
    
    # Final integration
    final_score = int(applied_adjustment + validation_norm - interference_level)
    
    # Output required result
    print(f"Result: {final_score}")
    return final_score

# Input data
benchmark_data = {
    'texts': [
        'SignalA',
        'noiseB',
        'CARRIERc',
        'staticD',
        'PULSEe'
    ],
    'multiplier': 3
}

# Execution point
final_score = compute_performance(benchmark_data)