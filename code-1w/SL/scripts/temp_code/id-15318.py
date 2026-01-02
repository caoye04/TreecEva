import itertools

def analyze_sequence(data_stream):
    # Irrelevant transformation: scrambles data but not used in final result
    scrambled = [x ^ 0xAA for x in data_stream if x % 3 != 0]
    return sum(scrambled[:5]) if len(scrambled) > 5 else 0

def compute_health_score(metrics):
    # Red herring function – looks important but unused
    base = sum(m * 0.7 for m in metrics)
    penalty = len([m for m in metrics if m < 50]) * 2.5
    return round(base - penalty, 2)

def filter_anomalies(records, threshold_map):
    filtered = []
    for i, record in enumerate(records):
        category = record['type']
        if category in threshold_map:
            # Real logic buried here among distractions
            adjusted_val = record['value'] >> 2  # Bit shift as part of real computation
            if adjusted_val < threshold_map[category]:
                filtered.append((i, adjusted_val))
    return filtered

def extract_signatures(payload):
    # Distractor: processes data but result ignored
    signatures = []
    for chunk in payload:
        sig = 0
        for b in chunk:
            sig = (sig << 1) ^ b
        signatures.append(sig & 0xFFFF)
    return sorted(signatures)

def process_metrics(entries, thresholds):
    # Core logic with meaningful steps
    temp_results = []
    for idx, entry in enumerate(entries):
        key = entry['tag']
        raw = entry['data']
        
        # Real processing step 1: bit manipulation
        processed_raw = list(itertools.starmap(lambda a, b: (a | b) & 0xFF, zip(raw[::2], raw[1::2])))
        
        # Real processing step 2: conditional accumulation
        total_shift = 0
        for val in processed_raw:
            if val & 0x1:
                total_shift += (val << 1) & 0xFF
            else:
                total_shift += val >> 1
        
        # Real processing step 3: mapping via thresholds
        if key in thresholds:
            ratio = total_shift / thresholds[key]
            temp_results.append(ratio * 100)
    
    # Real processing step 4: final aggregation
    aggregate = sum(temp_results) / len(temp_results) if temp_results else 0
    
    # Real processing step 5: correction based on enumeration logic
    correction_factor = 0
    for i, r in enumerate(temp_results):
        if i % 2 == 0 and r > 50:
            correction_factor += 1.5
    
    intermediate = aggregate + correction_factor * 2
    
    # Final diagnostic calculation – this is the answer
    final = int(intermediate - 32)  # Deterministic integer result
    
    # Dead code path – looks like it affects result but doesn't
    if final < 0:
        final = abs(final) ^ 0x55
    
    return final

# Simulated input data
log_entries = [
    {'tag': 'sensor_A', 'type': 'primary', 'value': 180, 'data': [23, 184, 91, 122, 67], 'timestamp': 1678800000},
    {'tag': 'sensor_B', 'type': 'backup',  'value': 95,  'data': [44, 201, 58, 133, 72], 'timestamp': 1678800060},
    {'tag': 'sensor_A', 'type': 'primary', 'value': 210, 'data': [31, 178, 88, 125, 69], 'timestamp': 1678800120}
]

system_thresholds = {
    'sensor_A': 150,
    'sensor_B': 100,
    'fallback_X': 80
}

# Unused variables – red herrings
baseline_readings = [76, 88, 92, 79, 85]
system_checksum = sum(baseline_readings) ^ 0xFFAA

# Auxiliary data for decoy functions
data_stream_input = [255, 128, 64, 32, 16, 8, 4, 2, 1]
payload_chunks = [[1, 2, 3], [4, 5], [6, 7, 8]]

# Execute decoy functions to increase interference
_ = analyze_sequence(data_stream_input)
_ = compute_health_score(baseline_readings)
_ = extract_signatures(payload_chunks)

# Main filtering – part of real logic chain
anomaly_list = filter_anomalies(log_entries, {'primary': 100, 'backup': 90})

# Key execution point: this produces the target result
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output result as required
print(f"Target result: {final_diagnostic}")