def preprocess_entries(entries):
    cleaned = []
    for entry in entries:
        if isinstance(entry, str):
            sanitized = entry.strip().lower().replace(" ", "_")
            if "invalid" not in sanitized:
                cleaned.append(sanitized)
    return cleaned

entries_raw = [" User Input ", "Data Point", " invalid entry ", "Sample Value", ""]
clean_data = preprocess_entries(entries_raw)

# Extraneous processing: irrelevant transformations
temp_analysis = {}
for item in clean_data:
    length_metric = len(item) * 1.5
    vowel_count = sum(1 for c in item if c in 'aeiou')
    temp_analysis[item] = (length_metric, vowel_count)

# Simulated weight map for scoring (some keys unused)
weights = {
    'base': 2.1,
    'bonus': 0.75,
    'penalty': -1.2,
    'multiplier': 3
}

# Auxiliary function with distraction logic
def assess_quality(tag):
    if 'value' in tag:
        return 1.5
    elif 'data' in tag:
        return 1.0
    else:
        return 0.5  # default boost

# Real data used in computation
data = [
    {'type': 'sample', 'value': 12, 'flag': True},
    {'type': 'point', 'value': 8, 'flag': False},
    {'type': 'input', 'value': 15, 'flag': True}
]

# Secondary irrelevant metric calculation
avg_value = sum(d['value'] for d in data) / len(data)
adjusted_avg = round(avg_value * 1.23, 2)
dummy_offset = adjusted_avg % 4

# Core score accumulator
def calculate_final_score(records, weight_map):
    base = weight_map['base']
    bonus = weight_map['bonus']
    penalty = weight_map['penalty']
    total = 0
    extra_points = 0

    for record in records:
        # Primary contribution
        contribution = record['value'] * base
        total += contribution

        # Conditional flag bonus
        if record['flag']:
            extra_points += bonus * 2

        # Type-based adjustment using string matching
        type_tag = record['type']
        quality_factor = assess_quality(type_tag)
        total += quality_factor

    # Apply global multiplier at end
    final_multiplier = weight_map['multiplier']
    aggregated = (total + extra_points) * final_multiplier

    # Red herring operation (not used)
    overflow_check = aggregated > 100
    debug_log = f"Final aggregation: {aggregated}, Overflow: {overflow_check}"

    return int(aggregated)  # Deterministic integer result

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")