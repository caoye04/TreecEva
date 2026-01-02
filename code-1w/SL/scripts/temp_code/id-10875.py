def analyze_trend(data, threshold=5.0):
    trend_changes = 0
    prev = data[0]
    for val in data[1:]:
        if abs(val - prev) > threshold:
            trend_changes += 1
        prev = val
    return trend_changes

readings = [3.2, 4.1, 9.8, 10.2, 14.5, 13.7, 8.3, 7.9, 12.4]
baseline = [5, 7, 6, 8, 9, 7, 6, 5, 8]

# Irrelevant string processing (distractor)
def process_labels(labels):
    cleaned = []
    for label in labels:
        temp = label.strip().lower().replace('_', '-')
        if 'sensor' not in temp:
            cleaned.append(temp[:3])
    return set(cleaned)

label_set = ['temp_1', 'pressure_x', 'flow_rate', 'level_z']
encoded_tags = process_labels(label_set)

# Bitwise manipulation with no impact on result (distractor)
mask = 0b101010
shifted_mask = (mask << 2) & 0b111111
checksum = 0
for b in baseline:
    checksum ^= (b + 3) & 0b1111

# Real logic starts here
def compute_deviation(ref, sample):
    diffs = []
    for r, s in zip(ref, sample):
        diffs.append(abs(s - r))
    return sum(diffs) / len(diffs)

def calculate_performance(base, samples):
    avg_dev = compute_deviation(base, [x * 1.1 for x in base])
    
    # Unnecessary slicing and set operations (semi-relevant distractors)
    segment_a = samples[2:6]
    segment_b = samples[3:7]
    common_values = set(segment_a) & set(segment_b)
    
    adjustment_factor = len(common_values)
    
    # Actual key computation
    raw_score = 0
    for i, val in enumerate(samples):
        if val > base[i % len(base)]:
            raw_score += 1
    
    # Final score calculation depends only on raw_score and adjustment_factor
    final_score = raw_score * 2 - adjustment_factor
    
    # Red herring: unused accumulation
    cumulative = 0
    for v in samples:
        cumulative += v // 2
    
    return final_score

# Key execution point
trend_count = analyze_trend(readings)
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")