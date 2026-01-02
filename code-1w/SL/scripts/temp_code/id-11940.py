import math

# Simulated sensor array data processing with diagnostic evaluation
def collect_readings():
    raw_signals = [i * 0.5 + math.sin(i) for i in range(15)]
    offset = 2.3
    calibrated = [round(x + offset, 3) for x in raw_signals]
    return calibrated

# Irrelevant auxiliary function - dead path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data if x > 1.0]

# Transform readings into binary fluctuation pattern
def extract_fluctuations(signal):
    trend = []
    for i in range(1, len(signal)):
        trend.append(1 if signal[i] >= signal[i-1] else 0)
    return trend

# Apply sliding window compression to bit pattern
def compress_pattern(bits):
    result = []
    for i in range(0, len(bits) - 2, 3):
        chunk = bits[i:i+3]
        compressed_bit = (chunk[0] ^ chunk[1]) | chunk[2]
        result.append(compressed_bit)
    # Padding logic - irrelevant to final result
    while len(result) % 4 != 0:
        result.append(0)
    return result

# Misleading transformation: frequency analysis (unused)
def compute_density_profile(pattern):
    ones = sum(pattern)
    zeros = len(pattern) - ones
    ratio = ones / len(pattern) if pattern else 0
    profile = []
    for i in range(5):
        profile.append(round(ratio * (i + 1), 4))
    return profile  # Never used

# Core analysis function
def evaluate_stability(metrics):
    score = 0
    for val in metrics:
        if val > 2.5 and val < 4.8:
            score += int(val)
        elif val < 1.2:
            score -= 1
    return score * 2  # Red herring calculation

# Set-based interference: environmental thresholds
env_thresholds = {1.2, 2.5, 3.1, 4.0, 4.8, 5.5}
dynamic_caps = {x * 2 for x in env_thresholds if x in {2.5, 3.1, 4.0}}  # unused

# Another decoy structure
temporal_weights = [(i, 0.8**i) for i in range(6)]
weight_map = {k: v for k, v in temporal_weights}  # distracting but unused

# Actual transformation pipeline
def transform_signal(raw):
    segment = raw[3:12]  # slicing operation
    diffs = [abs(segment[i] - segment[i-1]) for i in range(1, len(segment))]
    normalized_diffs = [d * 10 for d in diffs[:7]]  # limit to 7
    return [round(nd, 2) for nd in normalized_diffs]

# Pattern analyzer that feeds into final logic
def generate_signature(values):
    signature = []
    cumulative = 0
    for v in values:
        cumulative += v
        signature.append(int(cumulative // 1))
    return signature

# Critical function: uses set operations and list comprehension
def analyze_pattern(seq, limits):
    # Convert sequence to characteristic set
    observed = set([x for x in seq if x > 0])
    high_vals = {x for x in observed if x > 5}
    adjustment = len(high_vals) * 3 if high_vals else -2
    
    # Core accumulation logic
    total = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            total += val // (i + 1) if i > 0 else val
        else:
            total -= val % 3
    
    # Final adjustment using set difference (critical)
    baseline = {1, 2, 3, 4, 5}
    missing = baseline - observed  # some elements may be missing
    penalty = len(missing) * 2
    
    return total - penalty + adjustment

# --- Execution Flow ---
data = collect_readings()

# Dead code path - looks important but unused
if len(data) > 10:
    standardized = deprecated_normalization(data)
    stability_score = evaluate_stability(standardized)

transformed_data = transform_signal(data)

# Generate irrelevant intermediate results
fluctuations = extract_fluctuations(data)
compressed_code = compress_pattern(fluctuations)
density_fingerprint = compute_density_profile(compressed_code)  # unused

# Create signature (distraction)
sig = generate_signature(transformed_data)

# Define critical threshold set
threshold_set = {2, 3, 5}

# Key statement
final_diagnostic = analyze_pattern(transformed_data, threshold_set)

print(f"Result: {final_diagnostic}")