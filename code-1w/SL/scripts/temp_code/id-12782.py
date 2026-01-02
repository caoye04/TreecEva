from collections import defaultdict, Counter
import math

# Simulated sensor fusion system for environmental diagnostics
def analyze_readings(raw_data):
    temp_readings = [x for x in raw_data if x < 1000 and x > -50]
    pressure_readings = [x for x in raw_data if x >= 1000]
    
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    avg_pressure = sum(pressure_readings) / len(pressure_readings) if pressure_readings else 0
    
    # Irrelevant transformation (distractor)
    normalized = [math.log(abs(x) + 1) for x in raw_data]
    entropy_score = sum([abs(math.sin(x)) for x in normalized])

    return avg_temp, avg_pressure, entropy_score

def generate_baseline(samples):
    # Dead code path - never used in execution
    base_ref = defaultdict(int)
    for s in samples:
        base_ref[s % 7] += 1
    return dict(base_ref)

def compute_stability_factor(metrics_tuple):
    temp, pressure, entropy = metrics_tuple
    fluctuation_index = (abs(temp) * 0.3) + (pressure * 0.001)
    
    # Decoy calculation with misleading intermediate
    calibration_offset = 0
    if fluctuation_index > 50:
        calibration_offset = 2.5
    else:
        calibration_offset = -1.8
    
    # Actual relevant logic buried here
    raw_stability = 100 - fluctuation_index
    adjusted = raw_stability + calibration_offset
    
    # More red herring variables
    dummy_weights = [adjusted * math.cos(i) for i in range(5)]
    weight_sum = sum(dummy_weights)
    
    return adjusted

def extract_signatures(data_stream):
    # Complex but partially irrelevant processing
    chunks = [data_stream[i:i+3] for i in range(0, len(data_stream), 3)]
    signatures = []
    for chunk in chunks:
        if len(chunk) == 3:
            sig = (chunk[0] ^ chunk[1]) | chunk[2]  # Bit manipulation distractor
            signatures.append(sig)
    
    # Real but subtle use: only the length matters later
    return signatures

def validate_integrity(check_sequence):
    # Unused validation function (dead code)
    counts = Counter(check_sequence)
    return all(v % 2 == 0 for v in counts.values())

def process_metrics(signature, thresholds):
    # Core logic hidden among distractions
    base_value = sum(signature) % 1000
    
    # Multiple conditional expressions with red herrings
    mode_flag = 'A' if base_value > 600 else 'B' if base_value > 300 else 'C'
    
    adjustment = thresholds.get(mode_flag, 0)
    
    # Key computation
    preliminary = base_value * 1.5 - adjustment
    
    # Distracting data structure manipulations
    history_log = [{'step': i, 'val': preliminary - i*2} for i in range(3)]
    recent = history_log[-1]['val']
    
    # Final answer depends only on this
    final_diagnostic = int(recent + 17.8)
    
    # Extra noise
    debug_trace = {"final_raw": recent, "mode": mode_flag, "adjusted": adjustment}
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Input data
    sensor_input = [23.5, 1024, 18.9, 1500, -5.2, 1200, 30.1, 980, 27.3]
    
    # Step 1: Analyze readings
    analysis_result = analyze_readings(sensor_input)
    
    # Step 2: Compute stability (used later)
    stability_metric = compute_stability_factor(analysis_result)
    
    # Step 3: Extract signature (only length is actually used)
    raw_signature = extract_signatures([int(x) for x in sensor_input if isinstance(x, float)])
    
    # Irrelevant baseline generation
    _ = generate_baseline([1, 2, 3, 4, 5])
    
    # Threshold configuration (key to logic)
    threshold_map = {'A': 50, 'B': 30, 'C': 10}
    
    # Build health signature based on stability
    health_signature = [int(stability_metric)]
    health_signature.extend([len(raw_signature) * 2] * 2)
    
    # Final processing step - where the answer is produced
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    print(f"Target result: {final_diagnostic}")