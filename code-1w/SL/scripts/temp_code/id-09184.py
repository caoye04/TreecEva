from collections import defaultdict, Counter
import math

# Simulated sensor diagnostics with irrelevant auxiliary data
def generate_diagnostics():
    raw_readings = [0.88, 1.02, 0.94, 1.11, 0.76, 1.33, 0.89, 1.05]
    timestamps = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8']
    sensors = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']
    
    # Irrelevant transformation (distractor)
    squared_offsets = [round((x - 1)**2, 4) for x in raw_readings]
    offset_map = dict(zip(timestamps, squared_offsets))
    
    # Relevant diagnostic structure
    diagnostics = defaultdict(list)
    for i, reading in enumerate(raw_readings):
        sensor_id = sensors[i]
        diagnostics[sensor_id].append(reading)
    
    return diagnostics, offset_map

# Decoy function – looks important but unused in final computation
def analyze_stability(logs, window=3):
    trend_scores = []
    for i in range(len(logs) - window + 1):
        segment = logs[i:i+window]
        variance = sum((x - sum(segment)/len(segment))**2 for x in segment)
        trend_scores.append(round(variance, 4))
    return max(trend_scores) if trend_scores else 0.0

# Auxiliary validation (mixed relevance)
def validate_calibration(data):
    calibrated = {}
    for k, v in data.items():
        avg = sum(v) / len(v)
        calibrated[k] = abs(avg - 1.0) < 0.15  # Acceptable drift threshold
    return calibrated

# Core processing with red herrings and nested logic
def process_metrics(diagnostics, thresholds):
    # Misleading intermediate: checksum of keys (not used later)
    key_checksum = sum(ord(c) for c in ''.join(diagnostics.keys())) % 17
    
    # Bit manipulation distractor
    flag_state = 0
    for i, key in enumerate(sorted(diagnostics.keys())):
        flag_state ^= (i + 1) << (len(key) & 3)
    
    # Real work begins: compute rolling consistency score
    consistency_scores = []
    for sensor, readings in diagnostics.items():
        filtered = [r for r in readings if 0.7 <= r <= 1.3]  # Validity window
        if not filtered:
            continue
        mean_val = sum(filtered) / len(filtered)
        deviation_score = sum(abs(r - mean_val) for r in filtered)
        consistency_scores.append(deviation_score)
    
    # Secondary metric: count of sensors passing calibration
    calibration_results = validate_calibration(diagnostics)
    passing_sensors = sum(calibration_results.values())
    
    # Tertiary, irrelevant list comprehension (dead code path)
    anomaly_pairs = [(a, b) for idx_a, a in enumerate(consistency_scores) 
                           for idx_b, b in enumerate(consistency_scores) if idx_a < idx_b and abs(a-b) > 0.1]
    
    # Critical calculation chain
    base_metric = sum(consistency_scores) * 100
    adjustment_factor = passing_sensors * thresholds.get('scale', 1.0)
    
    # Logical masking using comparisons and bitwise mix
    mask_input = int(base_metric) & 0xFF
    control_flag = (passing_sensors >= 2) and (len(consistency_scores) > 1)
    override_trigger = (mask_input ^ 42) == 15  # False in this case
    
    if control_flag and not override_trigger:
        final_adjustment = adjustment_factor * 1.25
    else:
        final_adjustment = adjustment_factor * 0.8
    
    # Final computation
    final_diagnostic = int(base_metric + final_adjustment)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Generate real diagnostics
    diag_data, aux_map = generate_diagnostics()
    
    # Threshold configuration (some fields are red herrings)
    thresholds = {
        'tolerance': 0.15,
        'scale': 2.0,
        'decay': 0.95,
        'version': 'v2.1'
    }
    
    # Unused variables to increase interference
    baseline_ref = [math.log(x + 1) for x in range(1, 9)]
    index_tracker = dict(enumerate(['start', 'mid', 'peak', 'end']))
    zipped_view = list(zip(baseline_ref, index_tracker.values(), [key_checksum := 0]))  # dummy assignment
    
    # Execute core logic
    final_diagnostic = process_metrics(diag_data, thresholds)