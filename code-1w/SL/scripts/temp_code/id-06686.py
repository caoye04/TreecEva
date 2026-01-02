import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
humidity_readings = [45, 47, 50, 44, 46]
raw_signal = [0.88, 0.91, 0.85, 0.93, 0.87]

# Irrelevant calibration offset (distractor)
calibration_offset_1 = sum([x ** 0.5 for x in humidity_readings]) / len(humidity_readings)

# Noise filter threshold (unused path - dead code)
if len(temperature_readings) > 10:
    noise_threshold = 0.05
else:
    noise_threshold = None  # Never used

# Auxiliary transformation (partially relevant but obfuscated)
squared_humidity = [h**2 for h in humidity_readings]
normalized_temp = [(t - 20) / 5 for t in temperature_readings]

# Decoy function that looks important but is never called
def compute_stability_index(data):
    return sum(d**2 for d in data) / len(data)

# Signal preprocessing with red herring variables
baseline_correction = sum(raw_signal) / len(raw_signal)
amplitude_envelope = [abs(s - baseline_correction) for s in raw_signal]

# Introduce misleading intermediate metric (not used later)
effective_power = sum([a**2 for a in amplitude_envelope]) * 0.5

# Apply non-linear transform with conditional logic (key step disguised)
distorted_components = []
for i, sig in enumerate(amplitude_envelope):
    if i % 2 == 0:
        distorted_components.append(math.log(sig + 1e-5))
    else:
        distorted_components.append(math.exp(-sig))

# Create tuple of summary stats (some irrelevant)
summary_stats = (
    max(distorted_components),
    min(distorted_components),
    sum(normalized_temp),  # Red herring
    len(squared_humidity)   # Distractor
)

# Set-based uniqueness check on indices (appears significant)
valid_indices = {i for i in range(len(distorted_components)) if distorted_components[i] < -0.5}
adjusted_indices = valid_indices.union({len(distorted_components)})

# Core processing chain begins here
processed_data = [
    dc + summary_stats[0] for i, dc in enumerate(distorted_components)
    if i not in adjusted_indices
]

# Secondary adjustment using set difference (misleading)
index_set_a = {1, 2, 3}
index_set_b = {2, 3, 4}
masking_set = index_set_a.difference(index_set_b)  # evaluates to {1}

# Another decoy variable influenced by masking_set
shadow_correction = 0
for idx in masking_set:
    shadow_correction += processed_data[idx % len(processed_data)]

# Real computation hidden among distractions
def analyze_signal(signal):
    # Weighted harmonic mean with exponential damping
    weights = [math.exp(-0.1 * i) for i in range(len(signal))]
    weighted_inv_sum = sum(weights[i] / (abs(signal[i]) + 1e-6) for i in range(len(signal)))
    weight_sum = sum(weights)
    harmonic_estimate = weight_sum / weighted_inv_sum
    
    # Apply corrective shift based on parity of length
    if len(signal) % 2 == 1:
        adjustment = math.pi / 4
    else:
        adjustment = -math.pi / 4
    
    # Final nonlinear mapping
    result = math.tanh(harmonic_estimate + adjustment)
    
    # Dead branch - never executed due to prior filtering
    if len(signal) == 0:
        return -999.0
        final_backup = sum(signal) / 1e5  # unreachable
    
    return result

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Print target result
print(f"Target result: {final_diagnostic}")