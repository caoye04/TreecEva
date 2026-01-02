import math

# Simulated sensor array data (irrelevant initialization)
sensor_grid_a = [[i * j for j in range(5)] for i in range(5)]
sensor_grid_b = [[i + j for j in range(4)] for i in range(6)]

# Irrelevant calibration constants (distractors)
calibration_x = sum(sum(row) for row in sensor_grid_a) % 7
reference_phase = (calibration_x ** 2 + 3) // 5
auxiliary_mask = [reference_phase & (1 << i) for i in range(8)]

# Core signal processing setup
data_stream = [18, 24, 36, 48, 54, 60, 72]
scaling_factor = 1.5
offset_correction = -0.5

# Misleading preprocessing path (dead code - never used)
def deprecated_normalize(x):
    return [val / max(x) for val in x]

temp_normalized = deprecated_normalize(data_stream[:3])  # Unused result

# Actual relevant transformation
processed_data = []
for val in data_stream:
    if val % 6 == 0 and val > 20:
        transformed = (val // 6) * scaling_factor + offset_correction
        processed_data.append(round(transformed))

# Decoy function with plausible name but no real use
def compute_entropy(arr):
    total = 0
    for x in arr:
        if x > 0:
            total -= x * math.log(x)
    return total

entropy_value = compute_entropy([2, 3, 5, 7])  # Red herring computation

# Set operations: defining valid signal thresholds
base_thresholds = {x for x in range(5, 15)}
adaptive_boost = {x + 3 for x in base_thresholds if x % 2 == 1}
threshold_set = base_thresholds.union(adaptive_boost).difference({10, 14})

# Conditional expression chain with nested logic
signal_strength = len(processed_data) if sum(processed_data) > 30 else 0
activation_flag = 'HIGH' if signal_strength >= 5 else 'LOW'

# Primary analysis function with distractor variables inside
def analyze_signal(signal, thresholds):
    # Irrelevant local arrays (distractors)
    debug_log = []
    temp_analysis = []
    for i in range(len(signal)):
        debug_log.append((i, signal[i], signal[i] % 4))
        temp_analysis.append(signal[i] * 1.1)

    # Core logic masked by noise
    count_match = 0
    cumulative = 0
    for val in signal:
        # Key conditional expression
        penalty = 2 if val in {x for x in thresholds if x < 12} else 1
        adjusted_val = val - penalty
        if adjusted_val in thresholds:
            count_match += 1
            cumulative += adjusted_val

    # Final branching logic using set membership and conditionals
    final_score = cumulative * count_match if count_match > 2 else -1 * abs(cumulative)
    
    # Distractor block: unused statistical calculation
    mean_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    variance_proxy = sum((x - mean_temp) ** 2 for x in temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    return int(final_score)

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_set)

# Output required format
print(f"Result: {final_diagnostic}")