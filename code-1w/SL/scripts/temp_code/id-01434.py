def process_signal(data, limit):
    adjusted = [x * 1.5 for x in data if x > 0]
    clipped = [min(val, limit) for val in adjusted]
    return sum(clipped) // len(clipped) if clipped else 0

# Sensor data simulation with noise filtering
timestamps = [100, 101, 102, 103, 104, 105]
signal_raw = [30, -10, 45, 0, 60, 25]
noise_floor = 5
amplitude_correction = 1.2

# Irrelevant transformation (distractor)
corrected_raw = [round(x * amplitude_correction) for x in signal_raw]
valid_indices = [i for i, val in enumerate(signal_raw) if val >= noise_floor]
filtered_data = [signal_raw[i] for i in valid_indices]

# Secondary processing path with dead-end computation (misleading)
baseline_shift = 10
dummy_envelope = [abs(x - baseline_shift) + 2 for x in corrected_raw]
avg_dummy = sum(dummy_envelope) / len(dummy_envelope)

# Control flow with conditional expression (nested logic)
threshold = 50 if sum(filtered_data) > 100 else 30

# Key computation with slicing side-effect (non-impacting but cognitively distracting)
temp_segment = filtered_data[1:4]
scaling_factor = 1.1
scaled_temp = [int(x * scaling_factor) for x in temp_segment]

# Final processing step
final_output = process_signal(filtered_data, threshold)

# Output result as required
print(f"Result: {final_output}")