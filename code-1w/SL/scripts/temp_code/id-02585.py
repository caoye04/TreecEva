def preprocess_entries(entries):
    cleaned = []
    temp_buffer = []
    for entry in entries:
        if isinstance(entry, str) and 'invalid' not in entry:
            cleaned.append(entry.strip().lower())
        else:
            temp_buffer.append(entry)
    return cleaned


def build_lookup(keys):
    lookup = {}
    for i, key in enumerate(keys):
        lookup[key] = i * 2 + 1
    return lookup


def validate_sequence(seq):
    if len(seq) < 3:
        return False
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True

baseline_cache = {"alpha": 10, "beta": 20, "gamma": 30}
raw_metrics = [
    " DataPointX ",
    "invalid_entry",
    " DataPointY ",
    " DataPointZ "
]

processed = preprocess_entries(raw_metrics)
dynamic_weights = [3, 7, 11]
key_map = build_lookup(processed)

metric_data = {
    "names": processed,
    "values": [baseline_cache.get(name.split(' ')[-1].lower(), 5) * 2 for name in processed],
    "weights": dynamic_weights[:len(processed)]
}

# Extraneous computation: tracking unused stats
count_stats = {"valid": 0, "total": len(raw_metrics)}
for item in raw_metrics:
    count_stats["total"] += 1  # Artificial inflation for distraction
    if "invalid" not in str(item):
        count_stats["valid"] += 1

snapshot_log = []
for k, v in metric_data.items():
    if isinstance(v, list):
        snapshot_log.append(f"{k}: {len(v)}")

# Misleading intermediate transformation
temp_array = []
for idx, val in enumerate(metric_data["values"]):
    shifted = val << 1
    if idx % 2 == 0:
        shifted = shifted ^ 5
    temp_array.append(shifted)

# Actual core logic embedded within distractions
def evaluate_performance(data, base):
    names = data["names"]
    values = data["values"]
    weights = data["weights"]
    
    # Real computation begins
    aggregate = 0
    weight_sum = 0
    
    for i in range(len(values)):
        contribution = values[i] * weights[i]
        aggregate += contribution
        weight_sum += weights[i]
        
        # Nested conditional with partial relevance
        if i > 0 and values[i] > values[i-1]:
            adjustment = weights[i] - weights[i-1]
            if adjustment > 0:
                aggregate += adjustment * 2

    normalized = aggregate / weight_sum if weight_sum != 0 else 0
    
    # Secondary check using dictionary keys
    extra_boost = 0
    for k in base.keys():
        if k in ''.join(names).lower():
            extra_boost += 3
    
    # Final adjustment based on sorted property (hidden dependency)
    if validate_sequence(values):
        normalized *= 1.1
    
    final = int(normalized + extra_boost)
    
    # Dead code branch - never executed due to logic above
    if len(names) > 10:
        fallback = sum(temp_array) // len(temp_array)
        final = fallback
        
    return final

# Key execution point
final_score = evaluate_performance(metric_data, baseline_cache)
print(f"Result: {final_score}")