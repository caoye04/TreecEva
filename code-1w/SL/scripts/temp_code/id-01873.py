def analyze_segment(segment):
    length = len(segment)
    sum_values = sum(segment)
    avg = sum_values / length if length > 0 else 0
    variance = sum((x - avg) ** 2 for x in segment) / length if length > 0 else 0
    return avg, variance, length

segment_weights = [0.1, 0.3, 0.4, 0.2]
dummy_tracker = {'max_val': float('-inf'), 'count_above_5': 0}

def process_segments(segments):
    results = []
    total_length = 0
    weighted_avg_sum = 0
    
    for seg in segments:
        # Irrelevant tracking (distractor)
        for val in seg:
            if val > dummy_tracker['max_val']:
                dummy_tracker['max_val'] = val
            if val > 5:
                dummy_tracker['count_above_5'] += 1
        
        avg, var, length = analyze_segment(seg)
        total_length += length
        results.append((avg, var, length))
    
    # Real computation path
    temp_correction = 0
    for i, (avg, var, length) in enumerate(results):
        if var < 2.5:  # low variance bonus
            temp_correction += 0.5
        elif var > 8.0:
            temp_correction -= 0.3

    adjusted_scores = []
    for i, (avg, var, length) in enumerate(results):
        weight = segment_weights[i] if i < len(segment_weights) else 0.1
        score = avg * weight * (1 + temp_correction / 10)
        adjusted_scores.append(score)
    
    # Final aggregation
    base_score = sum(adjusted_scores)
    penalty = len([s for s in segments if sum(s) < 10]) * 0.7  # penalty for low-sum segments
    final_score = int(round(base_score * 100 - penalty * 10))
    
    # Dead code (misleading)
    if final_score < 0:
        final_score = abs(final_score)
    
    return final_score

# Input data
segments = [
    [3, 4, 5],         # sum=12, avg=4
    [2, 2, 3, 4],      # sum=11, avg=2.75
    [6, 7, 8],         # sum=21, avg=7
    [1, 1]             # sum=2,  avg=1
]

result_var = process_segments(segments)
print(f"Target result: {result_var}")