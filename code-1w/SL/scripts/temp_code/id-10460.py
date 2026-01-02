def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count


def extract_segments(text, delimiter='-', min_len=2):
    parts = text.split(delimiter)
    segments = []
    total_chars = 0
    for part in parts:
        if len(part) >= min_len:
            segments.append(part)
            total_chars += len(part)
    avg_length = total_chars / len(segments) if segments else 0
    return segments, avg_length


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * log2(prob)
    return round(entropy, 4)


def calculate_final_score(data, thresholds):
    # Step 1: Process numeric patterns
    peaks = analyze_pattern(data['readings'])
    
    # Misleading intermediate: unused transformation
    scaled_readings = [x * 1.5 for x in data['readings'] if x > 0]
    temp_sum = sum(scaled_readings[:3]) if len(scaled_readings) >= 3 else 0  # Distractor
    
    # Step 2: String processing with slicing
    raw_log = data['log_string']
    cleaned = raw_log.strip().upper()
    tokens = cleaned[::2] + cleaned[1::2]  # Interleaved slicing — irrelevant
    token_segments, avg_seg_len = extract_segments(cleaned, '-', 1)
    
    # Step 3: Threshold filtering
    valid_readings = [x for x in data['readings'] if thresholds['min'] <= x <= thresholds['max']]
    reading_sum = sum(valid_readings)
    
    # Step 4: Weighted score computation
    peak_bonus = peaks * 100
    base_score = reading_sum * 1.5
    length_penalty = len(token_segments) * 10
    
    # Hidden dependency: only every third reading above threshold contributes extra
    bonus_trigger = sum(1 for i, x in enumerate(valid_readings) if i % 3 == 2 and x > thresholds['max'] * 0.9)
    dynamic_bonus = bonus_trigger * 50
    
    # Final aggregation (key result)
    final_score = base_score + peak_bonus - length_penalty + dynamic_bonus
    
    # Dead code branch — misleading
    if final_score < 0:
        final_score = abs(final_score)  # Never reached due to data
    
    return int(final_score)

# Input data
sensor_data = {
    'readings': [12, 45, 23, 67, 33, 89, 44, 23],
    'log_string': 'err-warn-info-debug-trace'
}

thresholds_config = {
    'min': 20,
    'max': 85
}

# Execute main logic
final_score = calculate_final_score(sensor_data, thresholds_config)
print(f"Result: {final_score}")