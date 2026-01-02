import itertools

# Simulated sensor network diagnostic system
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Irrelevant transformation - distractor
def frequency_encode(signal, base=7):
    result = 0
    for i, val in enumerate(signal):
        result += (val * (base ** (i % 5))) % 97
    return result

# Dead function - never called but looks important
def compute_entropy(data):
    from math import log2
    freqs = {}
    for d in data:
        freqs[d] = freqs.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * log2(count/total) for count in freqs.values())
    return entropy

# Core processing with red herrings
def generate_phase_shifts(base_sequence, depth=3):
    shifts = []
    temp = base_sequence[:]
    for _ in range(depth):
        shifted = [temp[-1]] + temp[:-1]
        temp = [a ^ b for a, b in zip(temp, shifted)]
        shifts.append(sum(temp))
    # Distractor computation
    magic_offset = sum(itertools.accumulate(shifts, lambda x, y: (x * 31 + y) % 1000))
    return shifts

# Main analysis with multiple concepts
def analyze_signal(trace, thresholds):
    # Unpacking and set operations
    critical_nodes = {i for i, val in enumerate(thresholds) if val > 0.7}
    auxiliary_nodes = {i for i, val in enumerate(thresholds) if val < 0.3}
    
    # Real computation path
    segment_a = trace[:len(trace)//2]
    segment_b = trace[len(trace)//2:]
    
    # Bit manipulation red herring
    decoy_mask = 0
    for val in segment_a[:4]:
        decoy_mask ^= int(val * 100) << (int(val) % 4)
    
    # Actual relevant logic buried in noise
    valid_points = []
    for i, (a, b) in enumerate(zip(segment_a, segment_b)):
        if i in critical_nodes:
            adjusted = (a + b) * thresholds[i]
            if adjusted > 0.5:
                valid_points.append(adjusted)
        elif i in auxiliary_nodes and i < len(segment_b):
            # Misleading branch
            transformed = abs(segment_b[i] - segment_a[i]) ** 0.5
            if transformed > 0.1:
                valid_points.append(transformed * 0.1)
    
    # Key calculation
    aggregate = sum(valid_points)
    
    # Decoy aggregation using string methods - irrelevant
    status_log = "Processed_" + "_".join(f"P{idx}" for idx in sorted(critical_nodes | auxiliary_nodes)[:5])
    log_checksum = sum(ord(c) for c in status_log if c.isdigit())
    
    # Final determination - only this matters
    baseline = len(critical_nodes) * 0.85
    fluctuation = abs(aggregate - baseline)
    final_score = int((baseline - fluctuation) * 100)
    
    # Critical assignment point
    final_diagnostic = final_score + 50  # Offset applied
    
    # Never reached due to logic, but looks important
    if final_diagnostic < 0:
        final_diagnostic = -final_diagnostic
        
    return final_diagnostic

# Setup with misleading initializations
raw_data_stream = [15, 88, 45, 92, 11, 77, 54, 63, 99, 23]
config_weights = [0.85, 0.15, 0.92, 0.23, 0.67, 0.81, 0.19, 0.73, 0.05, 0.88]
calibration_key = 246

# Signal preprocessing chain
processed_signal = preprocess_readings(raw_data_stream)
scaled_signal = [round(p * 1.8 + 0.1, 2) for p in processed_signal]

# Generate fake features for distraction
trace_length = len(scaled_signal)
index_grid = list(itertools.product(range(2), repeat=3))
phase_patterns = generate_phase_shifts([int(x*10) for x in scaled_signal[:6]])

# Create composite trace with dummy transformations
extended_diagnostics = []
for i, val in enumerate(scaled_signal):
    if i % 2 == 0:
        extended_diagnostics.append(val * config_weights[i])
    else:
        extended_diagnostics.append(val + (config_weights[i] / 2))

composite_trace = [min(x, 1.0) for x in extended_diagnostics]

# Build threshold map with set logic
active_thresholds = []
for w in config_weights:
    if w > 0.8:
        active_thresholds.append(w - 0.3)
    elif w < 0.2:
        active_thresholds.append(w + 0.4)
    else:
        active_thresholds.append(w)

threshold_map = [round(t, 2) for t in active_thresholds]

# Execute main analysis
final_diagnostic = analyze_signal(composite_trace, threshold_map)

# Output required result
print(f"Result: {final_diagnostic}")