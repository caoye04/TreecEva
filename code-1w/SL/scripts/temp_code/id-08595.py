import math

def generate_phase_matrix(size):
    # Distractor: Unused complex computation
    return [[(i * j + 1) % 7 for j in range(size)] for i in range(size)]

def detect_anomalies(data_stream):
    # Real but indirect contributor: finds indices where variance spikes
    anomalies = []
    for i in range(2, len(data_stream) - 2):
        window_prev = data_stream[i-2:i]
        window_curr = data_stream[i:i+2]
        mean_prev = sum(window_prev) / len(window_prev)
        mean_curr = sum(window_curr) / len(window_curr)
        if abs(mean_curr - mean_prev) > 15 and data_stream[i] % 2 == 1:
            anomalies.append(i)
    return anomalies

def transform_kernel(base_kernel):
    # Dead code path — never used
    transformed = [k ** 1.5 for k in base_kernel if k > 3]
    return [t - 2 for t in transformed]

def compute_entropy(sequence):
    # Red herring: looks important, not used in final calculation
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq_map.values():
        p = count / total
        entropy -= p * (p and math.log2(p))
    return round(entropy, 4)

def evaluate_cohesion(grid):
    # Irrelevant metric — distracts from main logic
    cohesion_score = 0
    for row in grid:
        for i in range(len(row) - 1):
            if row[i] & row[i+1]:
                cohesion_score += 1
    return cohesion_score

def calculate_stability_index(grid, anomaly_indices):
    # Core function that actually matters
    total_influence = 0
    decay_factor = 0.85
    
    for idx in anomaly_indices:
        row = idx // len(grid[0])
        col = idx % len(grid[0])
        if row < len(grid) and col < len(grid[0]):
            raw_value = grid[row][col]
            adjusted = (raw_value ** 2) * decay_factor
n            total_influence += adjusted
    
    # Secondary relevant logic: filter and aggregate neighbors
    neighbor_bonus = 0
    for (r, c) in [(i//len(grid[0]), i%len(grid[0])) for i in anomaly_indices]:
        for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] & 1:  # odd values contribute
                    neighbor_bonus += grid[nr][nc] * 0.1

    final_index = total_influence * (1 + neighbor_bonus / (total_influence + 1e-6))
    return int(round(final_index))

# Simulated sensor grid readings (relevant data)
grid = [
    [12, 18, 23, 7, 41],
    [5,  89, 14, 6, 33],
    [92, 11, 27, 8, 19],
    [3,  77, 36, 52, 13],
    [61, 24, 44, 9, 58]
]

# Sensor data stream used to derive anomaly indices
sensor_data = [10, 12, 15, 30, 45, 47, 20, 18, 80, 85, 87, 22, 25, 40, 100, 105, 110, 33, 35, 42]

# Unused kernel — red herring
kernel_template = [4, 5, 6, 7, 8]
transformed_kernels = transform_kernel(kernel_template)

# Generate anomalies from sensor stream — this is critical
anomalies = detect_anomalies(sensor_data)

# Compute irrelevant metrics to distract
phase_matrix = generate_phase_matrix(5)
redundant_entropy = compute_entropy([grid[i][i] for i in range(5)])
cohesion = evaluate_cohesion(grid)

# Key statement: this determines the answer
energy_threshold = calculate_stability_index(grid, anomalies)

# Print result as required
print(f"Target result: {energy_threshold}")