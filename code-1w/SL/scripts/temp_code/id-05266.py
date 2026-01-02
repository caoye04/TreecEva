import itertools

# System health monitoring simulation with noise and red herrings
def simulate_sensors(baseline, iterations):
    readings = []
    for i in range(iterations):
        perturbation = (i * 0.1) % 0.5
        noise = len(readings) * 0.01
        readings.append(baseline + perturbation + noise)
    return readings

# Irrelevant helper: computes geometric progression (unused later)
def geo_progression(a, r, n):
    return [a * (r ** i) for i in range(n)]

# Core diagnostic logic
def compute_stability_index(raw_data):
    if len(raw_data) < 2:
        return 0
    diffs = [abs(raw_data[i+1] - raw_data[i]) for i in range(len(raw_data)-1)]
    return sum(diffs) / len(diffs)

def evaluate_component_health(data_stream, sensitivity):
    avg = sum(data_stream) / len(data_stream)
    variance = sum((x - avg) ** 2 for x in data_stream) / len(data_stream)
    stability = compute_stability_index(data_stream)
    # Red herring computation
    phantom_score = (variance * sensitivity) % 7.0
    # Actual health metric
    health_metric = (avg * 0.6) - (variance * 0.3) - (stability * 0.1)
    return health_metric

# Misleading function that appears important but is never called
def deprecated_analysis(sequence):
    cumulative = 0
    for idx, val in enumerate(sequence):
        cumulative += val % (idx + 1) if idx > 0 else val
    return cumulative * 0.5

def generate_threshold_matrix(seed_value):
    # Creates a 3x3 matrix using modular arithmetic and bit shifts
    matrix = []
    temp = seed_value
    for i in range(3):
        row = []
        for j in range(3):
            temp = (temp * 7 + 3) % 256
            cell = (temp ^ (i * 4)) & 0b11111  # XOR and bitwise AND
            row.append(cell / 10.0)
        matrix.append(row)
    return matrix

# Data fusion engine
def aggregate_metrics(scores, load_profile, thresholds):
    base_score = sum(scores) / len(scores)
    
    # Complex transformation chain with distractions
    adjustment_factor = 0
    peak_load = max(load_profile)
    if peak_load > 80:
        adjustment_factor += 0.2
    elif peak_load > 60:
        adjustment_factor += 0.1
    
    # Bit manipulation red herring
    encoded_hint = 0
    for val in load_profile[-3:]:
        encoded_hint ^= int(val)  # Accumulate XOR (irrelevant)
    encoded_hint = (encoded_hint & 0xFF) >> 2
    
    # Real adjustment based on threshold regions
    boost = 0
    for i, score in enumerate(scores):
        for tier in range(3):
            if score > thresholds[tier][i % 3] and i % 2 == 0:
                boost += 0.05
    
    # Critical calculation path
    intermediate = base_score + adjustment_factor + boost
    
    # Decoy normalization (never used)
    normalized_intermediate = (intermediate - 1) / (max(thresholds[0]) * 0.1) if intermediate > 1 else 0
    
    # Final nonlinear transformation
    final_value = (intermediate ** 2) * 0.85
    
    # Dead code branch - unreachable
    if False:
        final_value = abs(final_value - 999) / 1000
    
    return final_value

# --- Main Execution with Distractors ---

# Simulate sensor data (red herring block)
sensor_A = simulate_sensors(2.1, 10)
sensor_B = simulate_sensors(1.9, 10)
sensor_C = simulate_sensors(2.3, 10)

# Unused synthetic sequences
fake_series = geo_progression(1.5, 1.1, 8)
dummy_weights = [0.1 * (i % 4 + 1) for i in range(12)]

# Real component data streams
primary_stream = [3.2, 3.4, 3.1, 3.5, 3.3, 3.6, 3.0, 3.4]
backup_stream = [2.9, 3.3, 3.0, 3.2, 3.1, 3.5, 2.8, 3.3]
fallback_stream = [2.7, 3.1, 2.8, 3.0, 2.9, 3.4, 2.6, 3.2]

# Compute individual health scores
primary_health = evaluate_component_health(primary_stream, 1.2)
backup_health = evaluate_component_health(backup_stream, 1.0)
fallback_health = evaluate_component_health(fallback_stream, 0.8)

# Assemble reliability scores
reliability_scores = [primary_health, backup_health, fallback_health]

# System load profile with irrelevant transformations
raw_load_data = [55, 62, 78, 85, 73, 68, 88, 77, 65, 81]
filtered_load = [x for x in raw_load_data if x > 50]  # Filter (trivial)
system_load = [x * 1.05 for x in filtered_load]  # Slight scaling

# Generate threshold matrix using seed
threshold_matrix = generate_threshold_matrix(seed_value=123)

# Introduce dead variable (misleading)
consistency_check = list(itertools.accumulate([1 if system_load[i] > system_load[i-1] else 0 for i in range(1, len(system_load))]))
spurious_correlation = sum(1 for x, y in itertools.product(reliability_scores, system_load[:3]) if x > 2.0 and y > 70)

# Key statement
final_diagnostic = aggregate_metrics(reliability_scores, system_load, threshold_matrix)

# Output result
print(f"Result: {final_diagnostic}")