import math

# System configuration constants (some irrelevant)
BASE_FREQ = 440.0
HARMONIC_TOLERANCE = 0.05
MAX_ITERATIONS = 500
DEBUG_MODE = False
THRESHOLD_LIMIT = 987  # Unused in final computation

# Irrelevant sensor metadata
temperature_offset = 0.12
pressure_factor = 1.04
humidity_drift = -0.03

# Real-time signal processing variables
pattern_buffer = [0.5, 1.0, -0.5, 2.0, -1.0, 0.0, 1.5]
signal_strength = sum(abs(x) for x in pattern_buffer) / len(pattern_buffer)

# Calibration map with red herring entries
calibration_map = {
    'gain': 1.25,
    'offset': -0.15,
    'harmonic_shift': 0.08,
    'noise_floor': 0.02,
    'dummy_param_x': 3.14159,  # Distractor
    'irrelevant_flag': True,     # Distractor
    'unused_counter': 42        # Distractor
}

# Auxiliary diagnostic function (partially dead code)
def validate_phase_coherence(signal):
    if not signal:
        return 0.0
    coherence_score = 0.0
    for i in range(1, len(signal)):
        if signal[i] * signal[i-1] < 0:
            coherence_score += 0.1
    return round(coherence_score, 2)

# Decoy transformation (never called)
def transform_fourier_proxy(data):
    transformed = []
    for j, val in enumerate(data):
        transformed.append(val * math.sin(j * 0.5))
    return transformed

# Misleading preprocessing step (used but result discarded)
preprocessed = []
for index, value in enumerate(pattern_buffer):
    adjusted = value * calibration_map['gain'] + calibration_map['offset']
    if index % 2 == 0:
        adjusted = abs(adjusted)
    preprocessed.append(round(adjusted, 3))

# Secondary structure with distractor logic
event_log = [(1, 'start'), (2, 'calibrate'), (3, 'process')]
status_flags = set()
for code, msg in event_log:
    status_flags.add(msg)

# Another unused helper
def compute_entropy(values):
    total = 0.0
    for v in values:
        if v != 0:
            total -= v * math.log(abs(v))
    return total

# Core analysis logic with nested dependencies
def extract_moment_indices(signal):
    moments = []
    cumulative = 0.0
    for idx, val in enumerate(signal):
        cumulative += val ** 2
        if cumulative > 2.5 and len(moments) < 3:
            moments.append(idx * 100 + int(abs(val) * 10))
    return moments

# Main diagnostic engine
def analyze_signal(data, calib):
    # Step 1: Compute energy moment indices
    moment_indices = extract_moment_indices(data)
    
    # Step 2: Apply gain and offset correction
    corrected = []
    for v in data:
        corrected.append(v * calib['gain'] + calib['offset'])
    
    # Step 3: Calculate weighted phase integral
    phase_integral = 0.0
    for i, cv in enumerate(corrected):
        weight = math.cos(i * calib['harmonic_shift'])
        phase_integral += cv * weight
    
    # Step 4: Detect zero-crossing anomalies
    zero_crossings = 0
    for i in range(1, len(corrected)):
        if corrected[i-1] * corrected[i] < 0:
            zero_crossings += 1
    
    # Step 5: Compute harmonic distortion proxy
    raw_energy = sum(x**2 for x in data)
    corrected_energy = sum(x**2 for x in corrected)
    distortion_ratio = (corrected_energy - raw_energy) / (raw_energy + 0.1)
    
    # Step 6: Aggregate diagnostic score
    base_score = phase_integral * 100
    anomaly_penalty = zero_crossings * -15
    moment_bonus = sum(moment_indices) // 100 if moment_indices else 0
    
    # Step 7: Final composition
    intermediate = base_score + anomaly_penalty + moment_bonus
    
    # Step 8: Apply noise floor dampening (uses dict key)
    dampened = intermediate * (1 - calib['noise_floor'] * 2)
    
    # Step 9: Final nonlinear transformation
    final_value = int(math.floor(dampened ** 2 / 1000)) % 999
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_signal(pattern_buffer, calibration_map)

# Redundant validation block (dead logic path)
if __name__ == "__main__":
    temp_result = validate_phase_coherence(pattern_buffer)
    entropy_test = compute_entropy(pattern_buffer)
    # These don't affect final_diagnostic

print(f"Result: {final_diagnostic}")