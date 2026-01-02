import math

def preprocess_records(records):
    cleaned = []
    temp_sum = 0
    for i, record in enumerate(records):
        if 'valid' in record and not record['valid']:
            continue
        value = record.get('value', 0)
        offset = record.get('offset', 1)
        adjusted = (value * 1.5) / (offset + 0.5)
        if i % 2 == 0:
            adjusted = math.sqrt(adjusted) if adjusted > 0 else 0
        temp_sum += adjusted
        cleaned.append({'index': i, 'adjusted_val': adjusted})
    
    # Distractor: irrelevant normalization
    norm_factor = max([c['adjusted_val'] for c in cleaned]) if cleaned else 1
    normalized = [c['adjusted_val'] / norm_factor for c in cleaned]

    # More distraction: unused transformation
    transformed = ''.join([chr(97 + int(v * 3) % 26) for v in normalized[:5]])

    return cleaned


def analyze_trends(data_list):
    trend_scores = []
    for j, entry in enumerate(data_list):
        raw_score = entry['adjusted_val']
        penalty = 0.1 * j if j > 2 else 0
        score = raw_score - penalty
        trend_scores.append(score)
    
    # Dead code path (never used)
    if len(trend_scores) > 100:
        average_trend = sum(trend_scores) / len(trend_scores)
    else:
        average_trend = None
    
    return trend_scores


def calculate_final_score(dataset):
    base_scores = analyze_trends(dataset)
    multiplier = len(base_scores) if base_scores else 1
    
    # Core logic: weighted sum with exponential decay
    weighted_total = 0.0
    for idx, s in enumerate(base_scores):
        weight = 0.9 ** idx  # decaying weight
        weighted_total += s * weight
    
    # Distractor: complex but unused calculation
    zipped_pairs = list(zip(base_scores, reversed(base_scores)))
    correlation_estimate = sum(a * b for a, b in zipped_pairs) / len(zipped_pairs) if zipped_pairs else 0
    
    # Another red herring
    placeholder = [x for x in base_scores if x > 1.0]
    phantom_sum = sum(placeholder) * 0.05

    final_value = weighted_total * multiplier
    return int(round(final_value))

# Main execution
raw_data = [
    {'value': 10, 'offset': 2, 'valid': True},
    {'value': 15, 'offset': 1, 'valid': True},
    {'value': 0, 'offset': 1, 'valid': True},
    {'value': 25, 'offset': 3, 'valid': True},
    {'value': 30, 'offset': 2, 'valid': False},  # filtered out
    {'value': 20, 'offset': 1, 'valid': True}
]

processed_data = preprocess_records(raw_data)
intermediate_flag = len(processed_data) > 3
extra_metric = sum(d['adjusted_val'] for d in processed_data) / len(processed_data)

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")