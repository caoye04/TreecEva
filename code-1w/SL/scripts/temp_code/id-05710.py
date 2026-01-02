from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for a health monitoring system
def collect_readings():
    timestamps = list(range(100, 200))
    raw_values = [t * 1.5 + ((t % 7) ** 2) for t in timestamps]
    return dict(zip(timestamps, raw_values))

def analyze_pattern(sequence):
    # Irrelevant pattern analysis (red herring)
    freq = Counter(sequence)
    mode = freq.most_common(1)[0][1]
    entropy = -sum((count / len(sequence)) * math.log2(count / len(sequence)) 
                   for count in freq.values())
    return mode, entropy

def generate_baseline(ref_data):
    # Dead code path — never actually used in final computation
    base = defaultdict(float)
    for k, v in ref_data.items():
        if k % 3 == 0:
            base[k] = math.sqrt(v) * 0.1
    return base

def compute_checksum(data_list):
    # Bit manipulation distractor: looks important but unused later
    checksum = 0
    for val in data_list:
        shifted = int(val) >> 1
        checksum ^= shifted & 0xFF
    return checksum

def extract_features(raw):
    # Extract statistical features, some relevant, some not
    values = list(raw.values())
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    
    # Midpoint filtering (partially relevant)
    filtered = [v for v in values if abs(v - avg) < 2 * std_dev]
    mid_avg = sum(filtered) / len(filtered)
    
    # Decoy metrics
    peak_count = sum(1 for i in range(1, len(filtered)-1) 
                     if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1])
    
    return {
        'average': avg,
        'mid_avg': mid_avg,
        'spread': std_dev,
        'peaks': peak_count  # unused later
    }

def derive_signature(metrics, ts_data):
    # Create a 'health signature' using XOR-based encoding (only part matters)
    sig = 0
    sig ^= int(metrics['average']) & 0xFFFF
    sig ^= int(metrics['spread'] * 100) << 2
    sig &= 0xFFFFFF
    
    # Extra misleading operation
    temp_key = sum(len(str(k)) for k in ts_data.keys() if k % 11 == 0)
    decoy = (temp_key * 37) ^ 0xAA
    
    return sig

def validate_structure(data):
    # Unused validation function (dead code)
    if not isinstance(data, dict):
        return False
    return all(isinstance(k, int) and isinstance(v, (int, float)) for k, v in data.items())

def process_metrics(signature, full_readings):
    # Core logic hidden among distractions
    readings_list = list(full_readings.values())
    n = len(readings_list)
    
    # Real computation begins
    segment_a = readings_list[:n//3]
    segment_b = readings_list[n//2:n*2//3]
    
    sum_a = sum(segment_a)
    sum_b = sum(segment_b)
    
    # Key transformation
    ratio = sum_a / sum_b if sum_b != 0 else 0
    
    # Combine with signature using bitwise rotation
    rotated = ((signature << 3) & 0xFFFFFF) | (signature >> 19)
    combined = rotated ^ int(ratio * 1000)
    
    # Final diagnostic is derived from combined metric
    adjustment = len([x for x in readings_list if x > 150])
    final_diagnostic = (combined - adjustment) + 50
    
    # Red herring: irrelevant print that mimics importance
    debug_info = {"size": n, "checksum": compute_checksum(readings_list)}
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect sensor data
    sensor_data = collect_readings()
    
    # Step 2: Extract meaningful features
    stats = extract_features(sensor_data)
    
    # Step 3: Generate health signature
    health_signature = derive_signature(stats, sensor_data)
    
    # Step 4: Compute irrelevant baseline (distractor)
    baseline_map = generate_baseline(sensor_data)  # unused later
    
    # Step 5: Analyze pattern on raw values (decoy analysis)
    raw_vals = list(sensor_data.values())
    pattern_mode, pattern_entropy = analyze_pattern(raw_vals)
    
    # Step 6: Validate structure (unnecessary but looks important)
    is_valid = validate_structure(sensor_data)
    
    # Step 7: Process final metrics to get diagnostic
    final_diagnostic = process_metrics(health_signature, sensor_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")