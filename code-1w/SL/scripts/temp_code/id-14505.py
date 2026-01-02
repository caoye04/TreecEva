import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [54, 57, 52, 60, 65, 63, 58, 55, 53]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_B = 2.15
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_RANGE = 1024

# Preprocess signals using various transformations
smoothed_temps = [round((t * 0.7 + prev * 0.3), 2) for t, prev in zip(temperature_readings[1:], temperature_readings)]
expanded_humidity = [h * 1.02 + 3 for h in humidity_readings]

# Dummy transformation chain with red herring logic
transform_chain = lambda x: math.log(x + 10) if x > 20 else math.exp(x / 50)
applied_chain = [transform_chain(t) for t in smoothed_temps]

# Real signal processing path
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) * 1.5 for x in signal]

normalized_temp = normalize_signal(smoothed_temps)
clipped_signal = [max(0.5, min(x, 5.0)) for x in normalized_temp]  # Range limiting

# Decoy function that looks important but is unused
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Another decoy: complex frequency analysis (dead code path)
def spectral_analysis(signal):
    fft_result = []
    for i in range(len(signal)):
        comp = 0
        for j in range(len(signal)):
            angle = 2 * math.pi * i * j / len(signal)
            comp += signal[j] * (math.cos(angle) + math.sin(angle))
        fft_result.append(comp)
    return fft_result

# Signal fusion module
combined_weights = [
    round(0.6 * t + 0.3 * h / 10 + 0.1 * p / 100, 3)
    for t, h, p in zip(smoothed_temps, expanded_humidity, pressure_readings)
]

# Secondary derived metrics (some relevant, some not)
average_weight = sum(combined_weights) / len(combined_weights)
weight_variance = sum((w - average_weight) ** 2 for w in combined_weights) / len(combined_weights)
stability_index = 1 / (1 + weight_variance) if weight_variance != 0 else 1

# Mask generation based on threshold crossings (distractor)
threshold_mask = [1 if w > average_weight else 0 for w in combined_weights]
activation_count = sum(threshold_mask)

# Core diagnostic engine
processed_signals = [
    w * stability_index * 1.2 + 0.5
    for w in combined_weights
]

# Red herring: dummy state machine
states = ['IDLE', 'ACTIVE', 'STANDBY', 'ERROR']
current_state = states[1]
state_code = ord(current_state[0]) * 1000  # Misleading intermediate result

# Auxiliary logging system (irrelevant computations)
log_entries = []
for i, sig in enumerate(processed_signals):
    entry = {
        'id': f'LGN{i:03d}',
        'val': round(sig, 4),
        'flag': bool(i % 2),
        'meta': hex(int(sig * 100))
    }
    log_entries.append(entry)

# True diagnostic analyzer (only this matters)
def analyze_readings(signals):
    base_score = sum(signals)
    penalty = 0
    
    # Conditional adjustments
    if len(signals) > 5:
        penalty += 0.5
    if signals[0] < signals[-1]:
        penalty += 0.3
    
    # Critical adjustment based on middle segment
    mid_segment = signals[3:6]
    if sum(mid_segment) > 15:
        base_score += 2.0
    
    return round(base_score - penalty, 4)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output required format
print(f"Result: {final_diagnostic}")