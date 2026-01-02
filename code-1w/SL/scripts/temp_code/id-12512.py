import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_data(raw):    
    threshold = 42.5
    filtered = [x for x in raw if x > threshold]
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)), 6) for x in filtered]
    inverted = [1.0 - val for val in normalized][:len(normalized)//2]
    return normalized + inverted  # Misleading: includes irrelevant inverted portion

# Irrelevant auxiliary function (dead code path)
def legacy_compatibility_mode(data):
    return [d * 0.99 for d in data if d > 0.5]

# Signal segmentation – only slices matter here
def segment_signal(seq, size=4):
    segments = []
    for i in range(0, len(seq) - size + 1, size):
        if sum(seq[i:i+size]) > 1.5:  # Filtering condition
            segments.append(seq[i:i+size])
    return segments

# Decoy transformation chain
def transform_segment(s):
    a, b, c, d = s
    t1 = (a + d) * 0.5
    t2 = (b + c) * 0.7
    diff = abs(t1 - t2)
    score = round(math.sin(diff) * 100, 3)  # Looks important but unused
    return [t1, t2]  # Unused return

# Real processing begins here — subtle accumulation
def integrate_features(segments):
    accumulators = {'alpha': 0.0, 'beta': 1.0}
    history = set()
    
    for idx, seg in enumerate(segments):
        key = tuple(round(x, 3) for x in seg)
        if key in history:
            continue
        history.add(key)
        
        # Actual logic: product of middle two values after sorting
        sorted_seg = sorted(seg)
        mid_product = sorted_seg[1] * sorted_seg[2]
        accumulators['alpha'] += mid_product
        accumulators['beta'] *= (mid_product + 1) / (idx + 1)  # Distracting but not final

        # Red herring: conditional mutation that never triggers due to data range
        if len(str(mid_product)) > 5:
            accumulators['beta'] -= 0.1  

    return accumulators['alpha']  # Only alpha matters

# Complex analysis with multiple distractions
def analyze_signal(segs):
    if not segs:
        return -1
    
    # Decoy statistical measures
    all_vals = [val for seg in segs for val in seg]
    mean_val = sum(all_vals) / len(all_vals)
    variance = sum((v - mean_val)**2 for v in all_vals) / len(all_vals)
    peak = max(all_vals)
    entropy = -sum(p * math.log(p) for p in [v/sum(all_vals) for v in all_vals] if p > 0)  # Computed but unused

    # Real signal: count distinct tuples using slicing
    unique_signatures = set()
    for s in segs:
        signature = tuple(s[::2])  # Use every other element
        unique_signatures.add(signature)
    
    diversity_score = len(unique_signatures)
    
    # Critical accumulation from earlier
    base_metric = integrate_features(segs)
    
    # Final computation – only this matters
    final_diagnostic = int(base_metric * diversity_score + 0.5)
    
    # Multiple prints to distract
    print(f"Signal mean: {mean_val:.4f}")
    print(f"Entropy (unused): {entropy:.4f}")
    print(f"Diversity: {diversity_score}")
    
    return final_diagnostic

# --- Entry point ---
raw_input_stream = [
    43.0, 45.1, 47.3, 44.8, 46.2, 48.9, 42.7, 49.1,
    43.5, 46.0, 47.8, 45.4, 48.2, 44.1, 46.9, 47.6
]

# Step-by-step execution flow
cleaned = preprocess_sensor_data(raw_input_stream)
processed_segments = segment_signal(cleaned, size=4)
# The following line is the key statement
final_diagnostic = analyze_signal(processed_segments)
print(f"Result: {final_diagnostic}")