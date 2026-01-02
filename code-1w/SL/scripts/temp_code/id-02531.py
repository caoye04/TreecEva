import math

def preprocess_data(raw_values):
    # Normalize and filter noise (some distraction)
    filtered = [x for x in raw_values if x > 0.1]
    normalized = [math.log(val) for val in filtered]
    return normalized

# Simulate chemical reaction concentrations over time
time_series = [0.5, 0.8, 1.2, 0.9, 1.4, 2.1, 1.8, 2.5]
processed_readings = preprocess_data(time_series)

# Create a matrix of concentration gradients (relevant structure)
concentration_matrix = []
for i in range(len(processed_readings) - 1):
    row = []
    for j in range(4):
        # Some values are irrelevant but part of pattern
        base_val = processed_readings[i] * (j + 1) / (i + 1)
        noise_component = (i * j) % 3 / 10  # minor distraction
        row.append(round(base_val + noise_component, 3))
    concentration_matrix.append(row)

# Extra unused data structures to increase interference
auxiliary_cache = {f'key_{i}': i * 2 for i in range(10)}
dummy_histogram = [0] * 5
for val in time_series:
    bucket = min(int(val * 2), 4)
    dummy_histogram[bucket] += 1  # Dead-end computation

# Threshold logic for stability detection
threshold = 0.75
activation_log = []

for row in concentration_matrix:
    active_count = sum(1 for x in row if x > threshold)
    activation_log.append(active_count)

# Secondary validation check (semi-relevant)
valid_rows = [idx for idx, count in enumerate(activation_log) if count >= 2]

# Core calculation function
def calculate_equilibrium(matrix, limit):
    score = 0
    decay_factor = 0.9
    for idx, row in enumerate(matrix):
        if idx not in valid_rows:
            continue
        # Weighted contribution based on position
        weight = decay_factor ** idx
        # Use slicing to extract mid-segment
        segment = row[1:3]  # Focus on central elements
        segment_sum = sum(segment)
        contribution = segment_sum * weight
        # String-based condition as red herring (never triggers)
        flag = "critical" if 'xyz' in str(contribution) else "normal"
        if flag == "critical":
            score -= 1  # Dead code path
        score += contribution
    return round(score, 4)

# Final computation
interim_total = sum(sum(row) for row in concentration_matrix)  # Irrelevant summary
scaling_constant = len(valid_rows) if valid_rows else 1
normalized_total = interim_total / scaling_constant  # Distractor

# Key statement
equilibrium_score = calculate_equilibrium(concentration_matrix, threshold)

print(f"Result: {equilibrium_score}")