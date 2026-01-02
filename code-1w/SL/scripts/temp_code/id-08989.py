def analyze_sequence(seq, threshold):
    """Misleading function: appears relevant but unused in final computation."""
    count = 0
    for i, val in enumerate(seq):
        if val > threshold:
            count += (i ** 2) % 5
    return count

# Irrelevant data structures (distractor)
legacy_config = {
    'version': '2.1',
    'active': False,
    'priority_map': [3, 1, 4, 1, 5],
    'debug_mode': True
}

# Unused recursive helper (dead code path)
def compute_depth(n):
    if n <= 1:
        return 1
    return compute_depth(n-1) + compute_depth(n-2)

# Real processing begins here
log_data = [17, 23, 15, 42, 8, 31, 12, 29]
system_thresholds = {'low': 10, 'high': 30, 'critical': 25}

# Distractor: complex-looking but unused transformation
filtered_chunks = [log_data[i:i+3] for i in range(0, len(log_data), 3)]
processed_stats = []
for chunk in filtered_chunks:
    avg = sum(chunk) / len(chunk)
    processed_stats.append(round(avg))

# Bit manipulation red herring
obfuscation_key = 0
for i, val in enumerate(log_data):
    obfuscation_key ^= (val << 1) | (i & 1)

# Real logic hidden among noise
def extract_signals(data, config):
    signals = []
    for idx, reading in enumerate(data):
        if reading > config['low']:
            signals.append(idx * reading)
    return signals

def evaluate_stability(metrics, cutoff):
    total = 0
    for val in metrics:
        if val % 2 == 0:
            total += val // 3
        else:
            total -= val // 4
    return total if total >= cutoff else abs(total)

# Core actual computation chain
def integrate_diagnostics(readings, limits):
    # Step 1: filter readings above 'high' threshold
    elevated = [x for x in readings if x > limits['high']]
    
    # Step 2: apply scaling using integer division
    scaled = [x // 2 for x in elevated]
    
    # Step 3: use slicing to discard first element if exists
    trimmed = scaled[1:] if len(scaled) > 1 else []
    
    # Step 4: combine with index via enumerate
    indexed = [i + val for i, val in enumerate(trimmed)]
    
    # Step 5: convert to set to remove duplicates (though none here)
    unique_vals = list(set(indexed))
    
    # Step 6: zip with shifted version
    if len(unique_vals) > 1:
        zipped_pairs = list(zip(unique_vals, unique_vals[1:]))
        diffs = [abs(a - b) for a, b in zipped_pairs]
    else:
        diffs = [0]
    
    # Step 7: aggregate with weighted sum
    aggregate = 0
    for i, d in enumerate(diffs):
        aggregate += d * (i + 1)
    
    # Step 8: final adjustment using threshold cross-check
    high_count = sum(1 for x in readings if x > limits['critical'])
    return aggregate + (high_count * 2)

# Another decoy function that looks important
def validate_readings(entries):
    checksum = 0
    for item in entries:
        checksum = (checksum * 31 + item) % 10007
    return checksum == 1234

# Main processing function (actually used)
def process_metrics(data, thresholds):
    temp_result = extract_signals(data, thresholds)
    stability_score = evaluate_stability(temp_result, 10)
    diagnostic_value = integrate_diagnostics(data, thresholds)
    return diagnostic_value + (stability_score % 7)

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")