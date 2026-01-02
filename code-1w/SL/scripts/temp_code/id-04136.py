def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(len(seq) - 2):
        if seq[i] < seq[i+1] > seq[i+2]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def validate_input(x):
    return isinstance(x, list) and all(isinstance(i, (int, float)) for i in x)

# Unused transformation chain
def transform_values(v):
    shifted = [x << 1 for x in v if x % 2 == 0]
    mapped = list(map(lambda y: y ** 0.5, shifted))
    filtered = [z for z in mapped if z > 2]
    return sorted(filtered, reverse=True)

# Dead code path with misleading calculation
def compute_shadow_index(arr):
    total = 0
    for item in arr:
        total += (item * 17) % 9
    avg = total / len(arr) if arr else 0
    return round(avg * 2.5)

# String-based red herring
def extract_metadata(log_entry):
    parts = log_entry.split('|')
    timestamp_str = parts[0].strip()
    tags = parts[2].split(',') if len(parts) > 2 else []
    criticality = sum(1 for t in tags if 'urgent' in t.lower())
    return {
        'hour': int(timestamp_str[11:13]) if len(timestamp_str) > 13 else 0,
        'tag_count': len(tags),
        'critical': bool(criticality)
    }

# Distractor: unused complex data structure
log_data = """2023-07-15T08:22:10|SYSTEM|urgent_init,core_boot
2023-07-15T12:45:33|USER|normal_op,info_sync"""

logs_parsed = [extract_metadata(line) for line in log_data.strip().split('\n')]
off_topic_result = sum(item['hour'] for item in logs_parsed)

# Actual core logic buried among noise
def evaluate_stability(readings):
    baseline = sum(readings) / len(readings)
    deviations = [(x - baseline) ** 2 for x in readings]
    variance = sum(deviations) / len(deviations)
    return int(baseline), round(variance, 3)

# Heavily obscured main processing chain
def process_metrics(raw_data, importance_weights):
    # Step 1: Filter valid entries
    clean_data = [x for x in raw_data if isinstance(x, (int, float)) and x >= 0]
    
    # Step 2: Apply weighted transformation (only some weights matter)
    weighted = [clean_data[i % len(clean_data)] * importance_weights[i % len(importance_weights)]
               for i in range(len(clean_data) * 2)]
    
    # Step 3: Detect rising-falling patterns
    pattern_strength = analyze_pattern(weighted[:15])
    
    # Step 4: Compute stability metrics
    base_val, var = evaluate_stability(weighted)
    
    # Step 5: Generate secondary indicator (distractor but used in final mix)
    secondary_index = (base_val + pattern_strength) // 2
    
    # Step 6: Final score derived from multiple sources, but only variance matters
    temp_score = var * 100
    offset = len([w for w in importance_weights if w > 1])
    
    # Step 7: Key assignment - this is where answer is determined
    final_score = int(temp_score + offset)
    
    # Red herring: unused branching
    if final_score > 100:
        shadow = compute_shadow_index([final_score, base_val, secondary_index])
        final_score -= shadow % 7
    
    return final_score

# Real input data hidden among decoys
data = [4, 8, 6, 12, 9, 15]
weights = [1.5, 2.0, 0.5]

# Unused but plausible-looking computations
phantom_sequence = [data[i] ^ weights[0] for i in range(len(data))]
dummy_analysis = transform_values(phantom_sequence)

# Critical execution point
final_score = process_metrics(data, weights)

print(f"Result: {final_score}")