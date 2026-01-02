def preprocess_sequence(raw_seq):
    normalized = [x / sum(raw_seq) for x in raw_seq]
    shifted = [x + 0.1 for x in normalized]
    return shifted


def generate_pairs(values):
    pairs = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            pairs.append((values[i], values[j]))
    return pairs

# Simulate sensor data from three sources
sensor_a = [12, 15, 18, 21]
sensor_b = [9, 14, 17, 23]
sensor_c = [11, 16, 19, 20]

# Combine and normalize readings
all_readings = sensor_a + sensor_b + sensor_c
filtered_readings = [x for x in all_readings if x > 10]  # filter out low noise
scaled_readings = [x * 0.95 for x in filtered_readings]

# Apply preprocessing
processed = preprocess_sequence(scaled_readings)

# Create overlapping windows (slicing used here)
window_size = 3
sliding_windows = [processed[i:i+window_size] for i in range(len(processed) - window_size + 1)]

# Compute moving average for each window
moving_averages = []
for window in sliding_windows:
    avg = sum(window) / len(window)
    moving_averages.append(round(avg, 4))

# Generate frequency map of rounded averages
freq_map = {}
for val in moving_averages:
    rounded = round(val, 2)
    freq_map[rounded] = freq_map.get(rounded, 0) + 1

# Extract top frequencies (distractor computation)
top_frequencies = sorted(freq_map.values(), reverse=True)[:3]
dummy_metric = sum(top_frequencies) * 1.5  # irrelevant metric

# Construct matrix for stability analysis
matrix_data = [
    [moving_averages[0], moving_averages[1]],
    [moving_averages[2], moving_averages[3]]
]

# Analyze eigenvalue-like proxy (trace approximation)
def calculate_equilibrium(matrix):
    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if trace != 0:
        score = det / trace
    else:
        score = det
    
    # Additional distractor logic
    adjustment = 0
    for row in matrix:
        for elem in row:
            if elem > 0.5:
                adjustment += 0.01
    score += adjustment  # minor tweak, but included

    return round(score, 4)

# Critical statement
equilibrium_score = calculate_equilibrium(matrix_data)

# Print result as required
print(f"Result: {equilibrium_score}")