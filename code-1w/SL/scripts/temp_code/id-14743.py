import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 58, 43, 60, 55, 48, 50, 53, 57]
pressure_readings = [1013, 1015, 1012, 1016, 1010, 1014, 1011, 1017, 1013, 1015]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 35, 30, 40, 38, 33, 36, 31, 39, 34]  # Not used in final computation
light_intensity = [800, 850, 700, 900, 750, 820, 880, 730, 860, 810]  # Unused

# Misleading preprocessing: appears important but not directly used
drift_compensated = [round(t + 0.2, 1) for t in temperature_readings]
baseline_adjusted = [h - 2 for h in humidity_readings]

# Real signal filter: only temperatures above 22.0 are considered valid
effective_mask = [t > 22.0 for t in temperature_readings]
filtered_data = [temp for temp, mask in zip(temperature_readings, effective_mask) if mask]

# Multiple red herrings below:
aggregated_diagnostics = []
for i, val in enumerate(filtered_data):
    # Fake diagnostic path
    if i % 2 == 0:
        fake_score = val * humidity_readings[i] // 10
        aggregated_diagnostics.append(fake_score)

# Decoy function that looks relevant but isn't called in critical path
def compute_air_quality_index(hum, temp, press):
    """Irrelevant function - distractor"""
    base = temp * 1.5 + hum * 0.8
    adjusted = base / (press / 1000.0)
    return round(adjusted, 2)

# Another decoy: complex but unused transformation
cyclic_pairs = list(itertools.combinations(humidity_readings[:5], 2))
weighted_cycles = [abs(p[0] - p[1]) * 0.7 for p in cyclic_pairs]

# Real processing function with embedded distractions
def process_readings(data, limit):
    # Simulate calibration offset
    offset = 0.3
    calibrated = [x + offset for x in data]
    
    # Red herring: entropy-like calculation (not actually used in result)
    diffs = [abs(calibrated[i+1] - calibrated[i]) for i in range(len(calibrated)-1)]
    if diffs:
        average_change = sum(diffs) / len(diffs)
        fluctuation_penalty = int(average_change * 10)
    else:
        fluctuation_penalty = 0
    
    # Key logic hidden among noise
    total_energy = sum([x ** 2 for x in calibrated])  # Relevant
    sample_count = len(calibrated)  # Relevant
    
    # More distractions
    peak = max(calibrated)
    normalized_peak = round(peak / 30.0, 3)
    
    # Actual formula buried here
    if sample_count > 0:
        raw_index = total_energy / sample_count
        # Apply arbitrary field correction
        corrected_index = raw_index * 0.88
        # Final adjustment based on threshold logic
        threshold_factor = 1.15 if limit < 24.0 else 0.95
        final_value = corrected_index * threshold_factor
        return int(round(final_value))
    return 0

# Dead code path - never executed but looks plausible
def legacy_process(seq):
    return sum(seq) // len(seq)

# Global configuration that seems important
SYSTEM_MODE = 'ADVANCED'
CALIBRATION_CYCLE = 3
LOGGING_ACTIVE = False  # Never actually checked

# Critical variables
threshold = 23.8  # Used in final decision
reference_anchor = sum(pressure_readings) / len(pressure_readings)  # Distractor

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold)

# Print required output
print(f"Result: {final_diagnostic}")