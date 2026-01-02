from collections import defaultdict
import math

# Simulated sensor data from a chemical purification system
def generate_sensor_readings():
    return [78, 85, 62, 91, 75, 88, 67, 94, 73, 82]

# Irrelevant helper: computes average molecular weight (unused in final result)
def compute_avg_molecular_weight(readings):
    dummy_sum = 0
    for val in readings:
        dummy_sum += val * 1.07
    return dummy_sum / len(readings)

# Decoy function: appears important but is never called
def deprecated_calibration(x):
    return (x + 32) * 5/9

# Segment data into batches for processing
def segment_data(raw):
    segments = []
    for i in range(0, len(raw), 3):
        segments.append(raw[i:i+3])
    padding = [0] * (3 - len(segments[-1]) if len(segments[-1]) < 3 else 0)
    segments[-1].extend(padding)
    return segments

# Process each segment with noise filtering and amplification
def process_sequence(segments):
    processed = []
    amplification_factor = 2
    noise_floor = 60
    
    # Misleading intermediate: cumulative baseline drift (not used)
    baseline_drift = 0
    for seg in segments:
        filtered = []
        for val in seg:
            if val > noise_floor:
                # Apply non-linear enhancement
                enhanced = int(val ** 0.95) * amplification_factor
                filtered.append(enhanced)
        # Simulate erroneous double-processing (dead code path)
        if len(filtered) == 2:
            adjusted = [x - 5 for x in filtered]
        processed.append(filtered)
    
    # Flatten the processed segments
    flat_data = [item for sublist in processed for item in sublist]
    return flat_data

# Core validation logic: assess purity based on entropy-like dispersion
def validate_purity(signal):
    count_map = defaultdict(int)
    for x in signal:
        count_map[x] += 1
    
    # Compute dispersion metric (shannon-like entropy)
    total = len(signal)
    entropy = 0.0
    for count in count_map.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    
    # Transform entropy into integer score via modular scaling
    raw_score = int((entropy * 100) % 89)
    
    # Red herring: unused correction factor
    correction_bias = sum(1 for x in signal if x % 7 == 0) - 3
    
    # Final score computed using bitwise blending
    magic_constant = 0x1F
    filtration_score = (raw_score ^ magic_constant) & 0xFF
    
    # Dead branch: unreachable due to prior logic
    if len(signal) < 5:
        filtration_score = max(filtration_score, 50)
    
    return filtration_score

# Unused diagnostic function (distractor)
lambdify_diagnostic = lambda data: sum(x**2 for x in data if x < 70)

# Main execution pipeline
if __name__ == "__main__":
    raw_readings = generate_sensor_readings()
    segmented = segment_data(raw_readings)
    processed_signal = process_sequence(segmented)
    filtration_score = validate_purity(processed_signal)
    print(f"Result: {filtration_score}")