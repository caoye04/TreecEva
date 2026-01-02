import math

# Simulated sensor data processing for fluid dynamics analysis
def collect_readings(samples):
    raw_data = [math.sin(i * 0.5) + math.cos(i * 0.3) for i in range(len(samples))]
    filtered = [x * 1.2 for x in raw_data if x > 0]
    return filtered if len(filtered) > 3 else [0.0]

# Irrelevant auxiliary function - dead code path
def calculate_turbulence(data):
    if not data:
        return -1
    variance = sum((x - sum(data)/len(data))**2 for x in data) / len(data)
    return variance * 1.8

# Core transformation pipeline
def transform_sequence(values, threshold=0.5):
    processed = []
    temp_log = []
    for v in values:
        adjusted = abs(v) ** 0.8
        if adjusted > threshold:
            processed.append(round(adjusted, 6))
            temp_log.append(f"Kept: {adjusted}")
        else:
            temp_log.append(f"Skipped: {adjusted}")
    # Misleading intermediate
    summary_report = {'count': len(processed), 'actions': temp_log}
    return processed

# Recursive frequency counter (used later)
def count_frequency(seq, index=0, acc=None):
    if acc is None:
        acc = {}
    if index == len(seq):
        return acc
    key = int(seq[index])
    acc[key] = acc.get(key, 0) + 1
    return count_frequency(seq, index + 1, acc)

# Decoy statistical function - never called with real data
def compute_entropy(arr):
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for c in counts.values():n        prob = c / total
        entropy -= prob * math.log2(prob)
    return round(entropy, 4)

# Complex pattern analyzer with nested logic and distractors
def analyze_pattern(metrics):
    # Distractor variables
    baseline_offset = 2.17
    scaling_factor = 1.85
    debug_trace = []
    
    # Step 1: Transform using lambda and list comprehension
    normalized = [(lambda x: (x + baseline_offset) / scaling_factor)(val) for val in metrics]
    
    # Step 2: Filter significant components
    significant = [n for n in normalized if n > 0.7]
    
    # Step 3: Apply recursive counting on integer parts
    freq_map = count_frequency(significant)
    
    # Step 4: Compute weighted influence
    influence = 0.0
    for k, count in freq_map.items():
        if k % 2 == 0:
            influence += count * k * 1.1
        else:
            influence += count * k * 0.9
    
    # Step 5: Adjust with trigonometric modulation
    modulator = math.cos(len(significant)) * math.sin(influence % math.pi)
    final_raw = influence * (1 + modulator)
    
    # Step 6: Apply ceiling only if certain conditions met
    if len(significant) > 2 and final_raw < 50:
        final_raw = math.ceil(final_raw)
    
    # Dead branch - misleading logic
    if final_raw < 0:
        correction = math.exp(abs(final_raw))
        final_raw += correction  # Never reached
    
    # Key result computation
    adjustment = sum([math.tan(x) for x in normalized[:3]]) if len(normalized) >= 3 else 0
    equilibrium_score = int(final_raw - adjustment * 10)
    
    # Unused diagnostic structure
    diagnostics = {
        'input_size': len(metrics),
        'post_filter': len(significant),
        'freq_snapshot': dict(list(freq_map.items())[:3]),
        'modulator_value': modulator,
        'adjustment_impact': adjustment
    }
    
    return equilibrium_score

# Orchestration block
if __name__ == "__main__":
    # Initial sample indices
    time_points = list(range(15))
    
    # Collect synthetic flow readings
    flow_readings = collect_readings(time_points)
    
    # Transform into flow metrics (this is the actual input)
    flow_metrics = transform_sequence(flow_readings, threshold=0.6)
    
    # DEAD CODE - misleading usage
    dummy_metrics = transform_sequence([0.1, 0.2], threshold=0.9)
    backup_check = calculate_turbulence(dummy_metrics)  # unused
    
    # Critical statement: what is the value of equilibrium_score here?
    equilibrium_score = analyze_pattern(flow_metrics)
    
    # Print result as required
    print(f"Target result: {equilibrium_score}")