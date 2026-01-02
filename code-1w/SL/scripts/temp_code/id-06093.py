def analyze_sequence(data):
    temp_results = []
    running_total = 0
    noise_counter = 0  # Tracks irrelevant fluctuations

    for i, val in enumerate(data):
        if i % 3 == 0:
            running_total += val ** 2
        elif i % 5 == 0:
            noise_counter += 1  # Distractor: not used later
        else:
            temp_results.append(val * 0.5)

    processed = [x for x in temp_results if x > 10]  # List comprehension
    return running_total, processed


def generate_diagnostics(seq):
    diagnostics = {}
    diagnostics['length'] = len(seq)
    diagnostics['peak'] = max(seq) if seq else 0
    diagnostics['baseline'] = sum(seq) / len(seq) if seq else 0
    diagnostics['dummy_metric'] = 999  # Irrelevant metric
    return diagnostics


def calculate_rating(log_entry):
    base = log_entry['initial_sum']
    adjustments = log_entry['adjustments']
    penalty_factor = 0

    for adj in adjustments:
        if adj['type'] == 'overhead':
            penalty_factor += adj['value']

    rating = base - penalty_factor
    if rating < 0:
        rating = abs(rating) * 0.5
    return rating

# Main execution
input_data = [4, 12, 7, 15, 3, 9, 11, 6, 8, 10]

# Step 1: Analyze sequence
raw_total, filtered_values = analyze_sequence(input_data)

# Step 2: Generate unused diagnostics (distractor)
diag_info = generate_diagnostics(input_data)

# Step 3: Prepare adjustment logs
adjustment_log = [
    {'type': 'overhead', 'value': 3},
    {'type': 'calibration', 'value': 5},  # Not used
    {'type': 'overhead', 'value': 7}
]

# Step 4: Build analysis log
analysis_log = {
    'initial_sum': raw_total,
    'adjustments': adjustment_log,
    'timestamp': '2023-10-05',
    'version': '2.1'
}

# Step 5: Calculate final score
final_score = calculate_rating(analysis_log)

# Output result
print(f"Result: {final_score}")