import math

# Sensor calibration constants (some are red herrings)
CALIBRATION_A = 0.87
CALIBRATION_B = 1.03
CALIBRATION_C = 2.15  # Unused
CALIBRATION_D = 0.09  # Used only in decoy function

# Simulated sensor readings over time
raw_readings = [104, 98, 112, 95, 108, 115, 90, 120, 110, 97]

# Irrelevant transformation - looks important but unused in final path
def decoy_normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Decoy function with misleading intermediate result
def apply_noise_correction(readings):
    corrected = []
    for r in readings:
        if r < 100:
            corrected.append(r * (1 + CALIBRATION_D))
        else:
            corrected.append(r * (1 - CALIBRATION_D))
    return corrected

# Real processing: filter anomalies and apply actual calibration
def preprocess_readings(raw):
    filtered = [r for r in raw if 95 <= r <= 115]  # Remove outliers
    calibrated = [r * CALIBRATION_A for r in filtered]
    return sorted(calibrated, reverse=True)

# Secondary metrics derived from processed data
def compute_variability(metrics):
    n = len(metrics)
    mean_val = sum(metrics) / n
    variance = sum((x - mean_val) ** 2 for x in metrics) / n
    return math.sqrt(variance)

# Complex conditional logic with nested checks
def evaluate_stability(metrics, threshold=4.0):
    if len(metrics) < 5:
        return False
    
    variability = compute_variability(metrics)
    peak_ratio = metrics[0] / metrics[-1] if metrics[-1] != 0 else float('inf')
    
    # Multiple interdependent conditions
    condition_1 = variability < threshold
    condition_2 = 0.9 <= peak_ratio <= 1.1
    condition_3 = abs(metrics[0] - metrics[len(metrics)//2]) < 8
    
    return condition_1 and condition_2 and condition_3

# Data enrichment with distractor fields
def enrich_with_metadata(processed):
    metadata_bundle = {
        'readings_count': len(processed),
        'high_frequency_energy': sum(x ** 1.5 for x in processed[:3]),  # Irrelevant
        'spectral_entropy': math.log(sum(x * math.sin(x) for x in processed)),  # Distractor
        'valid': True,
        'calibration_used': 'A',
        'redundant_checksum': sum(processed) % 17  # Unused later
    }
    return metadata_bundle

# Core analysis function combining multiple concepts
def analyze_readings(metrics):
    stability = evaluate_stability(metrics)
    
    # Bit manipulation disguised as status encoding
    status_code = 0
    if stability:
        status_code |= (1 << 3)
    if sum(metrics) > 400:
        status_code |= (1 << 1)
    if len(metrics) % 2 == 0:
        status_code |= (1 << 0)
    
    # Conditional branching with list comprehension side-effect
    adjustments = []
    if status_code & (1 << 3):
        adjustments = [int(x * 0.95) for x in metrics if x > 100]
    else:
        adjustments = [int(x * 1.05) for x in metrics if x < 100]
    
    # Final diagnostic computed through multi-step reasoning
    base_score = sum(adjustments) * (1.0 if stability else 0.8)
    penalty = 0
    if not stability:
        penalty = compute_variability(metrics) * 10
    
    final_value = base_score - penalty + (status_code & 7)  # Key computation
    
    # Dead code branch that looks active
    if False:  # Simulates legacy deactivation
        fallback = sum(metrics) / len(metrics)
        final_value = fallback * 0.75
    
    return final_value

# Execution flow with hidden critical path
processed_metrics = preprocess_readings(raw_readings)

# Irrelevant parallel processing chain
noisy_readings = apply_noise_correction(raw_readings)
normalized_noisy = decoy_normalize(noisy_readings)

# Metadata generation - looks important but not used in answer
diagnostic_metadata = enrich_with_metadata(processed_metrics)

# Critical statement: this determines the answer
final_diagnostic = analyze_readings(processed_metrics)

print(f"Result: {final_diagnostic}")