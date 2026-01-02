from collections import defaultdict, Counter

def preprocess_records(raw_entries):
    # Irrelevant transformation: counts per category (not used in final score)
    category_tally = defaultdict(int)
    for entry in raw_entries:
        category_tally[entry['category']] += 1

    # Relevant processing: extract and normalize values
    values = []n    for entry in raw_entries:
        normalized = entry['value'] / (entry['factor'] + 1)
        if normalized > 0.5:
            values.append(normalized * 1.2)
        elif normalized > 0.2:
            values.append(normalized * 0.8)
        else:
            values.append(normalized * 0.5)

    status_flags = [e['status'] for e in raw_entries]  # Collected but unused
    flag_counter = Counter(status_flags)  # Distractor: computed but irrelevant

    return values

def calculate_entropy(data):
    # Dead-end function: not part of main logic
    if not data:
        return 0.0
    freq = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
    return round(entropy, 4)

def calculate_final_score(processed_data):
    base_accum = 0.0
    adjustment_factor = 1.75

    # Accumulate with conditional scaling
    for val in processed_data:
        if val < 1.0:
            base_accum += val ** 1.1
        elif val < 2.0:
            base_accum += val ** 1.05
        else:
            base_accum += val * 0.95

    # Secondary pass: correction based on distribution
    count_above_1_5 = sum(1 for v in processed_data if v > 1.5)
    if count_above_1_5 > 2:
        base_accum *= 1.1

    # Tertiary adjustment: subtle offset
    avg_val = sum(processed_data) / len(processed_data)
    if avg_val > 1.2:
        base_accum += 3.2
    else:
        base_accum += 1.8

    # Final nonlinear transform
    final = (base_accum ** 0.97) + 0.5
    return round(final, 4)

# Main execution
raw_data = [
    {'value': 8, 'factor': 7, 'category': 'X', 'status': 'active'},
    {'value': 6, 'factor': 4, 'category': 'Y', 'status': 'pending'},
    {'value': 9, 'factor': 8, 'category': 'X', 'status': 'active'},
    {'value': 5, 'factor': 2, 'category': 'Z', 'status': 'active'},
    {'value': 7, 'factor': 3, 'category': 'Y', 'status': 'active'},
    {'value': 4, 'factor': 1, 'category': 'X', 'status': 'failed'}
]

# Step 1: Preprocess the data
processed_data = preprocess_records(raw_data)

# Step 2: Calculate entropy (distractor computation)
entropy_metric = calculate_entropy(processed_data)  # Unused later

# Step 3: Key statement
final_score = calculate_final_score(processed_data)

# Print result
print(f"Target result: {final_score}")