import itertools
import math

def analyze_frequency_components(raw_signals, sample_rate):
    # Extract dominant frequencies using simple heuristic
    frequencies = []
    for signal in raw_signals:
        period = len(signal) / 2
        freq = sample_rate / period
        frequencies.append(freq)
    return frequencies

def normalize_weights(weight_list):
    total = sum(abs(w) for w in weight_list)
    return [w / total for w in weight_list] if total != 0 else weight_list

def calculate_interference(angles, coeffs):
    # Accumulate weighted phase contributions
    accumulation = 0.0
    temp_buffer = []
    
    for i, (angle, coeff) in enumerate(zip(angles, coeffs)):
        adjusted_angle = angle + math.sin(math.pi * i / 4)
        temp_buffer.append(adjusted_angle)
        
        if i % 2 == 0:
            accumulation += coeff * math.cos(adjusted_angle)
        else:
            accumulation -= coeff * math.sin(adjusted_angle)
    
    # Dummy tracking for interference patterns (not used in final result)
    pattern_tracker = {}
    for pair in itertools.combinations(temp_buffer, 2):
        delta = abs(pair[0] - pair[1])
        rounded_delta = round(delta, 2)
        pattern_tracker[rounded_delta] = pattern_tracker.get(rounded_delta, 0) + 1
    
    # Final interference calculation - only this matters
    final_shift = 0.0
    for val in temp_buffer:
        final_shift += math.atan2(math.sin(val), math.cos(val))
    
    return final_shift

# Simulated sensor input data
sensor_readings = [
    [0.1, 0.3, 0.2],
    [0.4, 0.6, 0.5],
    [0.7, 0.9, 0.8]
]

# Derived frequency analysis
sample_rate = 1000
freq_components = analyze_frequency_components(sensor_readings, sample_rate)
base_phase = math.pi / 6
phase_angles = [base_phase * (1 + f / 100) for f in freq_components]

# Weighting from calibration data
raw_weights = [1.2, -0.8, 1.5]
calibrated_weights = normalize_weights(raw_weights)

# Irrelevant intermediate computation - simulates diagnostic check
amplitude_profile = []
for idx, reading in enumerate(sensor_readings):
    avg_amp = sum(reading) / len(reading)
    amplitude_profile.append((idx, avg_amp))

# Key state variables
buffer_state = {"timestamp": 12345, "status": "stable"}
diagnostic_flag = False

# Actual critical computation path
weighted_magnitude = sum(abs(w) * 10 for w in calibrated_weights)
scaled_factor = weighted_magnitude / len(calibrated_weights)

# Introduce dummy transformations
transform_log = []
for w in calibrated_weights:
    transformed = math.log(abs(w) + 1e-5)
    transform_log.append(transformed)

# Core result calculation with distractors around
net_phase_shift = calculate_interference(phase_angles, calibrated_weights)

# Additional irrelevant bookkeeping
summary_stats = dict(
    count=len(phase_angles),
    max_weight=max(calibrated_weights),
    min_weight=min(calibrated_weights),
    aux_data=transform_log
)

# Final output - must print exactly as shown
Result: {net_phase_shift}