import math

# Simulated sensor array data (irrelevant initialization)
raw_sensor_data = [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]
baseline_offset = 0.5
calibration_factor = 1.2

# Irrelevant transformation chain
adjusted_values = [math.sin(x * calibration_factor) + baseline_offset for x in raw_sensor_data]
decoy_signal = sum([math.cos(x) for x in adjusted_values]) / len(adjusted_values)

# Real processing path begins
filtered_readings = [x ** 0.5 for x in raw_sensor_data if x > 0.5]  # Extract meaningful signals

# Simulate noise threshold filtering (distractor block)
noise_floor = 0.7
noisy_components = []
for val in raw_sensor_data:
    if abs(val - round(val)) > noise_floor:
        noisy_components.append(val)

# Actual signal processing with red herring variables
scaling_matrix = [[1, 0], [0, 1]]
weight_vector = [0.85, 0.92]

# Decoy function - never called but looks important
def compute_coherence(signal):
    return sum([math.log(1 + x) for x in signal]) / len(signal)

# Real intermediate transformation
normalized_power = [round(x * 10) / 10 for x in filtered_readings]

# Bit manipulation decoy (irrelevant to final result)
bit_encoded = 0
for i in range(len(normalized_power)):
    if int(normalized_power[i]) % 2 == 1:
        bit_encoded |= (1 << i)

# Conditional data augmentation (misleading path)
augmented_diagnostics = []
if len(normalized_power) > 5:
    for p in normalized_power:
        augmented_diagnostics.append(p * 1.1)
else:
    augmented_diagnostics = normalized_power.copy()  # Dead branch not taken

# Core logic disguised among distractions
status_flags = [1 if x >= 2.0 else 0 for x in normalized_power]
active_segments = sum(status_flags)

# Secondary analysis with fake dependency
reference_energy = sum([x**2 for x in normalized_power])
entropy_proxy = math.log(reference_energy) if reference_energy > 0 else 0

# Critical function: analyzes processed signals
def analyze_readings(signal_list):
    base_metric = sum(signal_list) / len(signal_list)
    
    # Nested logic with conditional weighting
    adjustment = 0.0
    for idx, val in enumerate(signal_list):
        if val > 2.0:
            if idx % 2 == 0:
                adjustment += 0.3
            else:
                adjustment -= 0.15
    
    # Complex interdependent calculation
    volatility_index = 0
    for i in range(1, len(signal_list)):
        volatility_index += abs(signal_list[i] - signal_list[i-1])
    
    # Final composition using multiple derived values
    composite_score = base_metric * (1 + adjustment / 10) + (volatility_index / 100)
    return int(composite_score * 100) / 100  # Rounded diagnostic value

# Processing pipeline with obfuscation
intermediate_frame = [x + 0.05 for x in normalized_power]

# Redundant smoothing pass (no effect on outcome due to override)
smoothed_frame = [x * 0.95 for x in intermediate_frame]
processed_signals = intermediate_frame  # Override - smoothing discarded

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Output requirement
print(f"Target result: {final_diagnostic}")