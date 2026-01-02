import math

# Simulate sensor array processing with noise filtering and signal transformation
def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.1
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    return sorted(filtered, reverse=True)

# Apply non-linear transformation using lambda for dynamic weighting
dynamic_weight = lambda x, idx: x * (0.8 + 0.2 * math.sin(idx))

# Transformation pipeline
def transform_signal(amplitudes):
    weighted = [dynamic_weight(amp, i) for i, amp in enumerate(amplitudes)]
    normalized = [w / max(weighted) for w in weighted] if weighted else [0]
    # Introduce irrelevant intermediate computation (distractor)
    entropy_proxy = sum(-x * math.log(x) for x in normalized if x > 0)
    smoothed = [math.sqrt(x) for x in normalized]
    return smoothed

# Threshold-based activation detector
def apply_threshold(processed_signal, threshold):
    activations = [1 if x >= threshold else 0 for x in processed_signal]
    return sum(activations)

# Simulated raw data from IoT sensors
raw_sensor_data = [0.05, -0.3, 0.67, -0.03, 0.88, 0.44, -0.61, 0.91, 0.12, -0.21]

# Step 1: Filter and sort meaningful signals
active_signals = preprocess_signals(raw_sensor_data)

# Step 2: Transform with non-linear dynamics
transformed_data = transform_signal(active_signals)

# Step 3: Compute activation count above threshold
final_output = apply_threshold(transformed_data, 0.5)

# Irrelevant diagnostic metrics (distractor variables)
total_energy = sum(x**2 for x in raw_sensor_data)
peak_magnitude = max(active_signals) if active_signals else 0
redundant_flag = len(active_signals) > 5 and final_output > 0

# Critical variable tracking
activation_score = final_output + 1  # Final adjustment

# Output target result
print(f"Result: {activation_score}")