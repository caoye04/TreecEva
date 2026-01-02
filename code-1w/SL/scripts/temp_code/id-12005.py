import math

# Simulated sensor data processing with embedded logic chain
def collect_readings():
    raw = [i * 1.5 for i in range(10)]
    offset = sum([x % 2 for x in range(7)])  # irrelevant: counts odd numbers up to 6
    return raw

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(x):
    return (x + 2) ** 0.5 if x > 0 else 0

# Unused transformation chain
def deprecated_filter(seq):
    return [z for z in seq if z > 3]

# Core transformation: relevant

def transform_signal(data):
    shifted = [math.sin(x) * 100 for x in data]
    floored = [int(y) for y in shifted]  # truncate decimals
    adjusted = []
    for val in floored:
        if val == 0:
            adjusted.append(1)
        elif val < 0:
            adjusted.append(val - 1)
        else:
            adjusted.append(val + 1)
    return adjusted

# Red herring: complex-looking but unused bitwise routine
def scramble_bits(sequence):
    result = 0
    for item in sequence:
        temp = item ^ 255
        temp = (temp << 2) | (temp >> 6)
        result += temp % 100
    return result  # never used

# Decoy statistical analysis (not part of main flow)
def compute_entropy(arr):
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for k in counts:
        p = counts[k] / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Key pattern analyzer: actually used

def detect_anomalies(seq):
    count = 0
    for i in range(1, len(seq)):
        if abs(seq[i] - seq[i-1]) > 150:
            count += 1
    return count

# Data enrichment with dummy features

def augment_record(entry_list):
    record = {}
    record['raw'] = entry_list
    record['size'] = len(entry_list)
    record['max_val'] = max(entry_list)
    record['checksum'] = sum([x % 10 for x in entry_list])  # misleading metric
    record['flags'] = [1 if x < 0 else 0 for x in entry_list]
    record['flag_sum'] = sum(record['flags'])
    return record

# Central logic: transforms and analyzes

def analyze_pattern(input_data):
    # Step 1: Filter out near-zero values (with distraction)
    filtered = [x for x in input_data if abs(x) > 1]
    
    # Step 2: Apply scaling based on position (relevant)
    scaled = []
    for idx, val in enumerate(filtered):
        factor = 1.1 if idx % 2 == 0 else 0.9
        scaled.append(round(val * factor))
    
    # Step 3: Detect transitions (used later)
    transitions = 0
    for i in range(len(scaled) - 1):
        if (scaled[i] < 0) != (scaled[i+1] < 0):
            transitions += 1
    
    # Step 4: Compute weighted aggregate
    weights = [0.5 ** i for i in range(len(scaled))]  # decaying weights
    weighted_sum = sum(scaled[i] * weights[i] for i in range(len(scaled)))
    
    # Step 5: Generate diagnostic code
    base_score = int(abs(weighted_sum))
    adjustment = transitions * 10
    if base_score > 1000:
        adjustment -= 20
    elif base_score < 100:
        adjustment += 15
    
    # Final computation
    diagnostic_code = base_score + adjustment
    
    # Dead branch: looks important but not taken due to logic
    if diagnostic_code < 0:
        diagnostic_code = abs(diagnostic_code) * 2
    elif diagnostic_code == 42:
        diagnostic_code = 999  # unreachable with this data
    
    return diagnostic_code

# Spurious global variables (distractors)
current_mode = "diagnostic"
threshold_limit = 888
temp_buffer = []
log_entry_count = 0

# Main execution flow
if __name__ == "__main__":
    readings = collect_readings()  # [0.0, 1.5, 3.0, ..., 13.5]
    processed = transform_signal(readings)
    enriched = augment_record(processed)
    transformed_data = enriched['raw']  # extract original processed list
    anomaly_count = detect_anomalies(transformed_data)  # computed but not used
    entropy_metric = compute_entropy(transformed_data)  # red herring
    final_diagnostic = analyze_pattern(transformed_data)
    print(f"Result: {final_diagnostic}")