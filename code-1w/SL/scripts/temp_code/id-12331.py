import math

def preprocess_signal(raw_data, threshold=0.75):
    """Irrelevant preprocessing function (dead code path)"""
    return [x for x in raw_data if abs(x) > threshold]

def deprecated_checksum(sequence):
    """Misleading utility - never called"""
    return sum(sequence) % 100

def transform_coordinate(x, y):
    # Distractor geometric function with no impact on final result
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r * math.cos(theta), r * math.sin(theta)

def rolling_average(data, window=3):
    # Unused signal processing function (red herring)
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def evaluate_stability_index(telemetry_stream):
    # Complex but irrelevant stability metric
    if len(telemetry_stream) == 0:
        return 0.0
    variance = sum((x - sum(telemetry_stream)/len(telemetry_stream))**2 for x in telemetry_stream) / len(telemetry_stream)
    return math.exp(-variance)

def filter_outliers(dataset, k=1.5):
    # Dead code path - distracts from main logic
    q1 = sorted(dataset)[len(dataset)//4]
    q3 = sorted(dataset)[3*len(dataset)//4]
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    return [x for x in dataset if lower_bound <= x <= upper_bound]

def analyze_subsystem_health(metrics, weights):
    # Decoy analysis with complex weighting (not used in final computation)
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    normalization = sum(weights)
    return weighted_sum / normalization if normalization else 0

def compute_entropy(values):
    # Misleading information-theoretic calculation
    total = sum(abs(v) for v in values)
    if total == 0:
        return 0.0
    probabilities = [abs(v) / total for v in values]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

def analyze_system_state(readings, factor):
    # Core relevant function with embedded logic chain
    adjusted = [r * factor for r in readings]
    
    # Step 1: Apply conditional scaling based on magnitude
    scaled = []
    for val in adjusted:
        scaled.append(val * 2 if val < 0 else val * 0.5)
    
    # Step 2: Generate diagnostic flags using conditional expressions
    flags = [1 if x > 0 else -1 for x in scaled]
    
    # Step 3: Compute weighted directional sum
    direction_weighted = sum(f * abs(s) for f, s in zip(flags, scaled))
    
    # Step 4: Apply modulo-based state reduction
    state_code = int(abs(direction_weighted)) % 89
    
    # Step 5: Conditional correction based on parity
    corrected_state = state_code + (10 if state_code % 2 == 0 else -5)
    
    # Step 6: Secondary adjustment using floor division
    intermediate = corrected_state // 3
    
    # Step 7: Final transformation using min/max clamping
    clamped = max(-500, min(500, intermediate * 4))
    
    # Step 8: Ultimate determination via arithmetic combination
    final_diagnostic = (clamped + 17) * 3 // 2  # Key assignment point
    
    return final_diagnostic

# Primary data inputs
quantum_readings = [0.3, -0.7, 1.2, 0.8, -1.1, 0.5]
calibration_factor = 2.5

# Irrelevant auxiliary data (distractors)
system_logs = [(1, 'OK'), (2, 'OK'), (3, 'ERROR')]
baseline_profile = {'a': 0.1, 'b': 0.9}
temporal_weights = [0.25, 0.5, 0.75, 1.0, 0.75, 0.5]

# Spurious intermediate calculations (misdirection)
signal_energy = sum(x**2 for x in quantum_readings)
normalized_vector = [x / max(quantum_readings) for x in quantum_readings if x > 0.5]
phase_shift = math.sin(math.pi / 3)

# Dummy control flow with no outcome effect
if len(quantum_readings) > 5:
    dummy_correction = 0.95
    filtered_data = [x for x in normalized_vector if x > 0.3]
else:
    dummy_correction = 1.05
    filtered_data = []

# Meaningful but obscured core computation
final_diagnostic = analyze_system_state(quantum_readings, calibration_factor)

# Output requirement
print(f"Result: {final_diagnostic}")