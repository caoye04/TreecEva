from collections import defaultdict
import math

def preprocess_records(raw_entries):
    # Irrelevant transformation: counts per category (not used in final logic)
    category_count = defaultdict(int)
    for entry in raw_entries:
        category_count[entry['category']] += 1

    # Relevant processing: extract and normalize values
    normalized = []
    base_offset = sum([e['value'] for e in raw_entries]) / len(raw_entries)
    for e in raw_entries:
        norm_value = (e['value'] - base_offset) ** 2
        normalized.append(norm_value)
    
    return normalized

def calculate_entropy(values):
    # Dead function - not called in main flow, adds distraction
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return entropy

def calculate_final_score(data_chunk):
    # Apply window-based smoothing (irrelevant to final result but looks important)
    smoothed = [sum(data_chunk[i:i+3]) / min(3, len(data_chunk)-i) for i in range(len(data_chunk))]
    
    # Key computation: find max of even-indexed elements after threshold filter
    thresholded = [x for x in data_chunk if x > 1.5]
    
    # Distractor: tracking indices that don't matter
    index_log = []
    temp_sum = 0.0
    for idx, val in enumerate(thresholded):
        if idx % 2 == 0:
            index_log.append(idx)
            temp_sum += val

    # Actual core logic: average of thresholded values, floored, then mod 97
    avg_val = sum(thresholded) / len(thresholded) if thresholded else 0
    score_component = int(avg_val)
    
    # Final score influenced by length parity (minor but relevant)
    adjustment = len(data_chunk) % 3
    final_score = (score_component + adjustment) ** 2

    # Red herring: unused intermediate
    diagnostic_trace = f'Processed {len(data_chunk)} items with {len(thresholded)} above threshold'
    
    return final_score

# Main execution
raw_data = [
    {'value': 3, 'category': 'A'},
    {'value': 1, 'category': 'B'},
    {'value': 4, 'category': 'A'},
    {'value': 1, 'category': 'C'},
    {'value': 5, 'category': 'B'},
    {'value': 9, 'category': 'A'}
]

processed_data = preprocess_records(raw_data)
# Additional distraction: unused alternate path
if len(processed_data) > 10:
    processed_data = processed_data[:5]

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")