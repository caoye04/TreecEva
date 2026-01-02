from itertools import combinations

# Simulate signal processing with noise filtering and pattern detection
def analyze_segment(data, threshold):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    
    # Irrelevant computation: count transitions (not used later)
    transitions = 0
    for i in range(1, len(data)):
        if (data[i-1] > threshold) != (data[i] > threshold):
            transitions += 1

    # Relevant metric: average of values above threshold
    avg_above = sum(above_threshold) / len(above_threshold) if above_threshold else 0
    
    # Distractor: complex unused combination logic
    possible_pairs = list(combinations(above_threshold, 2))
    high_product_count = sum(1 for a, b in possible_pairs if a * b > 100)
    
    return avg_above

# Secondary helper - appears important but only used once
def normalize_values(values):
    max_val = max(values) if values else 1
    return [v / max_val for v in values]

# Main processing function
def process_segments(segments, thresholds):
    results = []
    temp_buffer = []
    
    for i, segment in enumerate(segments):
        # Use corresponding threshold or default
        thresh = thresholds[i] if i < len(thresholds) else 50
        
        # Preprocessing: normalize segment (has side effect on flow but not critical)
        norm_seg = normalize_values(segment)
        scaled_seg = [int(x * 100) for x in norm_seg]  # Scale back to integer
        
        # Core analysis
        score = analyze_segment(scaled_seg, thresh)
        
        # State tracking with red herring
        temp_buffer.append(len([x for x in scaled_seg if x > thresh]))
        
        results.append(score)
    
    # Final aggregation: weighted by original segment length
    total_weighted = 0
    total_length = 0
    
    for i, res in enumerate(results):
        weight = len(segments[i])
        total_weighted += res * weight
        total_length += weight
    
    final_score = total_weighted / total_length if total_length else 0
    
    # Dead code path - never executed under normal inputs
    if False and len(temp_buffer) > 100:
        fallback = sum(temp_buffer) / len(temp_buffer)
        final_score = fallback

    return final_score

# Input data
segments = [
    [85, 90, 78, 92],
    [45, 55, 60, 58, 53],
    [15, 20, 25, 30, 18, 22]
]

thresholds = [75, 50, 20]

# Execution point
final_score = process_segments(segments, thresholds)

# Output result
print(f"Result: {final_score}")