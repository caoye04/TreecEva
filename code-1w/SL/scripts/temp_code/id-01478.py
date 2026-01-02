def analyze_performance(metrics):
    # Irrelevant transformation (distractor)
    normalized = [m * 1.05 for m in metrics if m > 0]
    adjusted = [n - 0.5 for n in normalized]

    # Meaningful but indirect computation
    base_total = sum(metrics)
    penalty = 0
    for i, val in enumerate(metrics):
        if i % 3 == 0 and val < 50:
            penalty += 10

    # Dead code path (never executed due to condition)
    if len(metrics) > 100:
        scaling_factor = 0.9
        adjusted_again = [a * scaling_factor for a in adjusted]
    else:
        scaling_factor = 1.0  # Unused later

    # Red herring: complex but unused bitwise shift
    decoy_result = (base_total << 2) ^ 255

    return base_total - penalty


def evaluate_condition(flags):
    # Unused function - red herring
    return any(f == 'critical' for f in flags)


def transform_dataset(data):
    # Destructuring and zip usage (required feature)
    keys = ['x', 'y', 'z']
    paired = list(zip(keys, data))
    mapped = {k: v * 2 for k, v in paired}  # Unused mapping

    # Case conversion as distraction
    labels = ['A', 'B', 'C']
    upper_labels = [l.lower() for l in labels]  # Reversed logic

    # List comprehension with filter (has effect)
    processed = [x for x in data if x % 4 == 0]
    return processed


def aggregate_batches(batched_data):
    flat = []
    for batch in batched_data:
        for item in batch:
            if item > 0:
                flat.append(item)

    # Early break in loop (suggested paradigm)
    cumulative = 0
    for val in flat:
        cumulative += val
        if cumulative > 500:
            break  # Early exit

    return cumulative


def process_results(raw_data):
    # Key variable unpacking (required concept)
    header, body = raw_data[0], raw_data[1:]

    # Tuple unpacking (distractor)
    _, offset = header

    # Modular arithmetic used meaningfully
    mod_weights = [abs(b % 7) + 1 for b in body]
    weighted_sum = sum(body[i] % 13 * mod_weights[i] for i in range(len(body)))

    # Real logic hidden among distractions
    filtered_body = [b for b in body if b % 2 == 1]  # Only odd values
    base_score = analyze_performance(filtered_body)

    # Another decoy variable
    temp_result = aggregate_batches([[base_score]])

    # Final calculation using correct chain
    adjustment = len(filtered_body) * 3
    preliminary = base_score + adjustment

    # Bit manipulation that actually matters
    final_bit_shift = preliminary >> 1  # Divide by 2 via right shift

    # Final score computed here
    final_score = final_bit_shift + (preliminary % 11)

    return final_score

# Main execution data
assessment_data = [42, ("meta", 5), 67, 44, 81, 39, 72, 55]

# Unused variables (red herrings)
data_copy = assessment_data[:]
duplicate_check = set(data_copy)
flag_sequence = ['normal', 'warning', 'normal']

# Unused transformation
transformed = transform_dataset([6, 8, 12])

# Critical execution point
final_score = process_results(assessment_data)

print(f"Result: {final_score}")