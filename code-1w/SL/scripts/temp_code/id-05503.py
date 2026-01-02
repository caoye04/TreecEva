import math

# Simulated sensor network data processing with diagnostic analysis
def collect_sensor_data():
    raw_data = [
        (1001, [23.4, 19.5, 20.1, 22.8]),
        (1002, [18.7, 19.3, 17.9, 18.0]),
        (1003, [25.6, 26.1, 25.8, 26.3]),
        (1004, [15.2, 14.8, 15.5, 15.0])
    ]
    return raw_data

def filter_outliers(readings, limit=27.0):
    # Irrelevant filtering for values above 27 (none in data)
    return [x for x in readings if x < limit]

def normalize_readings(readings):
    mean_val = sum(readings) / len(readings)
    normalized = [(r - mean_val) * 1.05 for r in readings]  # Slight adjustment
    adjusted = []
    for val in normalized:
        if val > 0:
            adjusted.append(val + 0.1)
        else:
            adjusted.append(val - 0.1)
    return adjusted

def compute_variability_index(seq):
    if len(seq) < 2:
        return 0.0
    diffs = [abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)]
    return sum(diffs) / len(diffs)

def generate_signature(data_block):
    # Decoy function - computes SHA-like index but unused
    sig = 0
    for item in data_block:
        sig ^= int(sum(item[1]) * 100)
    return sig % 999

def temperature_class(average):
    if average < 16.0:
        return 'LOW'
    elif average < 20.0:
        return 'MID'
    else:
        return 'HIGH'

def build_threshold_map():
    # Complex structure with unused fields
    thresholds = {
        'LOW': {'base': 15.0, 'tolerance': 1.5, 'weight': 0.8, 'decay': 0.05},
        'MID': {'base': 18.5, 'tolerance': 1.2, 'weight': 1.0, 'decay': 0.03},
        'HIGH': {'base': 24.0, 'tolerance': 2.0, 'weight': 1.3, 'decay': 0.07}
    }
    # Unused transformation
    inverse_map = {v['base']: k for k, v in thresholds.items()}
    scaling_factor = 1.0
    for t in thresholds.values():
        scaling_factor *= t['weight']
    return thresholds

def process_readings(raw_data):
    processed = {}
    variability_scores = []  
    total_sensors = len(raw_data)
    cumulative_offset = 0.0
    
    for sid, readings in raw_data:
        clean_reads = filter_outliers(readings)
        norm_reads = normalize_readings(clean_reads)
        avg = sum(norm_reads) / len(norm_reads)
        class_tag = temperature_class(avg)
        score = compute_variability_index(norm_reads)
        variability_scores.append(score)
        
        # Store multiple irrelevant metrics
        stats = {
            'sensor_id': sid,
            'readings_count': len(norm_reads),
            'average': avg,
            'class': class_tag,
            'variability': score,
            'confidence': 0.95 if score < 1.0 else 0.75,
            'flags': []
        }
        if score > 0.8:
            stats['flags'].append('VARIANCE_ALERT')
        processed[sid] = stats
        
        # Red herring: cumulative offset that isn't used later
        cumulative_offset += abs(avg - 20.0)
    
    # Dead code path: never accessed
    if len(variability_scores) > 10:
        global_summary = {
            'aggregated_stability': sum(variability_scores) / len(variability_scores)
        }
    
    return processed

def validate_diagnostic_integrity(diag_code):
    # Unused validation stub
    checksum = 0
    for c in str(diag_code):
        if c.isdigit():
            checksum = (checksum * 3 + int(c)) % 17
    return checksum == 0

def analyze_readings(processed_data, threshold_map):
    diagnostics = []
    alert_count = 0
    base_reference = 0.0
    
    # Extract relevant averages and compare against dynamic thresholds
    for sensor_id, data in processed_data.items():
        avg_val = data['average']
        class_key = data['class']
        threshold_info = threshold_map[class_key]
        expected_base = threshold_info['base']
        tolerance_band = threshold_info['tolerance']
        
        deviation = avg_val - expected_base
        
        if abs(deviation) > tolerance_band:
            if deviation > 0:
                diagnostics.append(3)
            else:
                diagnostics.append(-3)
        else:
            diagnostics.append(1)
        
        if 'VARIANCE_ALERT' in data['flags']:
            alert_count += 1
    
    # Secondary logic: modify diagnostics based on alert density
    alert_ratio = alert_count / len(processed_data) if processed_data else 0
    adjustment = 0
    if alert_ratio >= 0.5:
        adjustment = 2
    elif alert_ratio > 0.25:
        adjustment = 1
    
    final_score = sum(diagnostics) + adjustment * 2
    
    # Introduce misleading alternate computation
    phantom_score = 0
    for d in diagnostics:
        phantom_score = (phantom_score + d) * 0.9
    # But we don't use it
    
    # Key variable assignment - this is the answer
    final_diagnostic = int(final_score * 17)  # Final transformation
    
    # Additional red herring variables
    debug_trace = []
    for k in processed_data.keys():
        debug_trace.append(f"S{k}:OK")
    trace_hash = hash(tuple(debug_trace)) % 1000
    
    return final_diagnostic

# Main execution flow
sensor_data = collect_sensor_data()
total_blocks = len(sensor_data)
processed_data = process_readings(sensor_data)
threshold_map = build_threshold_map()
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")