from itertools import combinations

def analyze_segments(data, threshold):
    segments = []
    temp_segment = []
    for val in data:
        if val > threshold:
            temp_segment.append(val)
        else:
            if len(temp_segment) > 1:
                segments.append(temp_segment[:])
            temp_segment = []
    if len(temp_segment) > 1:
        segments.append(temp_segment)
    return segments

# Simulate sensor readings with noise filtering
data_stream = [3, 7, 9, 2, 8, 6, 1, 4, 11, 5, 10, 12]
noise_floor = 5
clean_segments = analyze_segments(data_stream, noise_floor)

# Misleading computation: average of max values (not used in final result)
max_averages = [sum(segment) / len(segment) for segment in clean_segments if segment]
shadow_value = sum(max_averages) * 0.5 if max_averages else 0

# Process each segment to extract features
processed_data = []
for i, segment in enumerate(clean_segments):
    length = len(segment)
    weighted_sum = sum(x * (i + 1) for x in segment)
    squared_total = sum(x ** 2 for x in segment)
    normalized_energy = (squared_total ** 0.5) / length if length else 0
    
    # Distractor variables
    temp_debug = [x for x in segment if x % 2 == 0]
    dummy_shift = segment[-1:] + segment[:-1] if segment else []
    
    # Real feature extraction
    entropy_like = 0
    for x in segment:
        prob = x / sum(segment)
        if prob > 0:
            entropy_like -= prob * __import__('math').log(prob)
    
    processed_data.append({
        'id': i,
        'size': length,
        'energy': normalized_energy,
        'entropy': entropy_like,
        'weight_contrib': weighted_sum
    })

# Additional red herring: combinatorial analysis of unused features
unused_pairs = list(combinations([p['energy'] for p in processed_data], 2))
phantom_metric = sum(abs(a - b) for a, b in unused_pairs) if unused_pairs else 0

# Real scoring logic
baseline = 10
adjustment_factor = 0.75

score_components = []
for entry in processed_data:
    size_bonus = entry['size'] * 2
    entropy_penalty = int(entry['entropy'] * 3)
    contribution_score = (entry['weight_contrib'] // (entry['size'] + 1))
    raw_score = size_bonus - entropy_penalty + contribution_score
    score_components.append(raw_score)

# Final aggregation using enumerate and zip idiomatically
indexed_scores = list(enumerate(score_components))
offsets = [i * 1.5 for i in range(len(score_components))]
adjusted_scores = [sc + off for i, sc in indexed_scores for off in offsets if i == offsets.index(off)]

# Correct but subtle aggregation
aggregated_shift = sum([v for k, v in enumerate(offsets) if k < len(score_components)])
final_score = baseline + sum(score_components) - int(aggregated_shift) + int(adjustment_factor * 10)

# Critical execution point
final_score = calculate_final_score(processed_data)

# Dummy function to add interference
def calculate_final_score(data):
    base = 15
    total_weight = sum(item['weight_contrib'] for item in data)
    total_size = sum(item['size'] for item in data)
    entropy_adjusted = sum(item['entropy'] for item in data) * 2
    return base + (total_weight // max(total_size, 1)) - int(entropy_adjusted)

Result: {final_score}