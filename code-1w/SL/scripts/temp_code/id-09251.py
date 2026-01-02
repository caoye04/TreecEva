import math

def analyze_signal_integrity(signal, threshold=0.5):
    """Determine signal segments above threshold."""
    return [i for i, x in enumerate(signal) if x > threshold]

def normalize_weights(raw_weights):
    """Normalize a list of weights to sum to 1.0."""
    total = sum(raw_weights)
    return [w / total for w in raw_weights]

def calculate_interference(phases, magnitudes):
    """Compute net phase shift using weighted vector summation."""
    # Convert polar to Cartesian coordinates
    x_total, y_total = 0.0, 0.0
    for phase, mag in zip(phases, magnitudes):
        x_total += mag * math.cos(phase)
        y_total += mag * math.sin(phase)
    
    # Compute resultant angle (phase shift)
    net_angle = math.atan2(y_total, x_total)
    
    # Irrelevant intermediate calculation (distractor)
    temp_magnitude = math.sqrt(x_total**2 + y_total**2)  # Not used in final answer directly
    adjustment_factor = 1.0 if temp_magnitude > 0 else 0.0
    
    # Apply fake correction (dead computation)
    corrected_angle = net_angle * adjustment_factor
    
    # Final normalization to [-pi, pi]
    while corrected_angle > math.pi:
        corrected_angle -= 2 * math.pi
    while corrected_angle <= -math.pi:
        corrected_angle += 2 * math.pi
        
    return corrected_angle

# Main simulation setup
frequencies = [50, 60, 120, 400]
sampling_rate = 1000
time_points = [t / sampling_rate for t in range(sampling_rate)]

# Generate composite signal (distractor use)
composite_signal = [
    0.3 * math.sin(2 * math.pi * frequencies[0] * t) +
    0.5 * math.sin(2 * math.pi * frequencies[1] * t) +
    0.7 * math.sin(2 * math.pi * frequencies[2] * t) +
    0.2 * math.sin(2 * math.pi * frequencies[3] * t)
    for t in time_points
]

# Extract high-magnitude segments (not directly related to phase)
signal_peaks = analyze_signal_integrity(composite_signal, threshold=0.8)

# Define phase angles (radians) for four signal components
phases = [
    math.pi / 6,      # 30 degrees
    math.pi / 3,      # 60 degrees
    2 * math.pi / 3,  # 120 degrees
    5 * math.pi / 6   # 150 degrees
]

# Define raw influence weights
raw_influences = [1, 2, 3, 4]

# Normalize weights (semi-relevant, but not all are used)
weights = normalize_weights(raw_influences)

# Misleading slicing operation on irrelevant data (distractor)
segment_offset = len(time_points) // 4
sample_window = composite_signal[segment_offset: -segment_offset]
peak_density = len(signal_peaks) / len(time_points)

# Additional red herring: simulate temperature drift effect (unused)
temp_drift = [0.01 * math.sin(t * 0.5) for t in time_points[:100]]
baseline_drift = sum(temp_drift) / len(temp_drift)

dummy_correlation = 0.0
for i, s in enumerate(sample_window[:50]):
    dummy_correlation += s * temp_drift[i % len(temp_drift)]
dummy_correlation /= 50

# Core computation: calculate net phase interference
net_phase_shift = calculate_interference(phases, weights)

# Another distraction: process phases in reverse for checksum
reverse_sum = 0.0
for p in phases[::-1]:
    reverse_sum += math.cos(p)
checksum = int(abs(reverse_sum) * 1000)

# Output the target result
print(f"Result: {net_phase_shift}")