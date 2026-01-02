def analyze_readings(values):
    cleaned = [v for v in values if isinstance(v, (int, float)) and v >= 0]
    if not cleaned:
        return [0]
    smoothed = []
    for i, val in enumerate(cleaned):
        window = cleaned[max(0, i-1):i+2]
        avg = sum(window) / len(window)
        smoothed.append(round(avg, 2))
    return smoothed


def validate_entry(record):
    if not record.get('active'):
        return False
    tags = record.get('tags', [])
    if 'deprecated' in tags:
        return False
    return len(tags) > 0


def process_metrics(data, limits):
    temp_results = []
    metadata_log = []
    total_weight = 0.0

    for idx, entry in enumerate(data):
        if not validate_entry(entry):
            continue

        raw_values = entry['readings']
        processed = analyze_readings(raw_values)
        
        # Distractor: irrelevant aggregation
        magnitude = sum([x**2 for x in processed]) ** 0.5
        normalization_factor = max(processed) if processed else 1
        
        score = 0
        for j, val in enumerate(processed):
            threshold = limits.get(f'channel_{j % 3}', 50)
            if val > threshold:
                score += 1.5
            elif val > threshold * 0.8:
                score += 0.7

        # Semi-relevant transformation
        adjusted_score = score * (0.9 + 0.2 * (idx % 2))
        temp_results.append(adjusted_score)
        
        # Distractor: unused logging structure
        metadata_log.append({
            'index': idx,
            'magnitude': magnitude,
            'norm_factor': normalization_factor,
            'tag_count': len(entry.get('tags', []))
        })

    # Real computation path
    base_total = sum(temp_results)
    penalty = 0
    for log in metadata_log:  # Iterating over distractor data
        if log['tag_count'] > 2:
            penalty += 0.1  # Minor effect, but negligible
    
    final_score = int(base_total - penalty)  # Final deterministic integer result
    
    # Dead code path (never reached due to logic above)
    if len(temp_results) == 1000:
        fallback = sum([x * 0.5 for x in temp_results])
        final_score = int(fallback)

    return final_score

# Input construction
data = [
    {'readings': [60, -5, 70, 'invalid', 80], 'active': True, 'tags': ['urgent', 'monitor']},
    {'readings': [20, 30, 40], 'active': True, 'tags': ['low']},
    {'readings': [-10, -20], 'active': True, 'tags': []},
    {'readings': [90, 85], 'active': False, 'tags': ['deprecated']},
    {'readings': [45, 55, 65], 'active': True, 'tags': ['critical', 'urgent', 'reviewed']}]

thresholds = {
    'channel_0': 40,
    'channel_1': 50,
    'channel_2': 60
}

result = process_metrics(data, thresholds)
print(f"Result: {result}")