import math

# Irrelevant helper function (decoy)
def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total

# Unused transformation map (distractor data)
transform_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 100,
    'C': lambda x: abs(x - 50),
    'D': lambda x: x * 0.5
}

# Simulated sensor readings with noise (some relevant, some not)
sensor_data = [12, -8, 15, 0, 22, -3, 9]

# Red herring: statistical summary (not used in final result)
mean_val = sum(sensor_data) / len(sensor_data)
std_dev = (sum((x - mean_val) ** 2 for x in sensor_data) / len(sensor_data)) ** 0.5
outlier_threshold = mean_val + 2 * std_dev

# Real processing begins: filter valid signals
def filter_signals(data):
    filtered = []
    for val in data:
        # Only positive odd numbers are valid signals
        if val > 0 and val % 2 == 1:
            filtered.append(val)
    return filtered

# Transform via custom logic (not using transform_map)
def apply_gain(signal, base=3):
    adjusted = []
    for s in signal:
        # Non-linear amplification
        adjusted.append(int(s * (base ** (s % 4))))
    return adjusted

# Check integrity using checksum (irrelevant to output but looks important)
def validate_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) % 256
    return checksum == 128  # Always false for our data

# Core pipeline function
def process_pipeline(raw_input):
    # Step 1: Filter relevant signals
    step1 = filter_signals(raw_input)
    
    # Step 2: Apply gain based on dynamic condition
    dyn_base = 2 if sum(step1) > 20 else 4
    step2 = apply_gain(step1, dyn_base)
    
    # Step 3: Map into frequency bins (dictionary usage)
    freq_bins = {}
    for num in step2:
        bin_key = num // 10
        if bin_key not in freq_bins:
            freq_bins[bin_key] = 0
        freq_bins[bin_key] += 1
    
    # Step 4: Extract dominant bin (highest count)
    dominant_count = max(freq_bins.values())
    candidate_bins = [k for k, v in freq_bins.items() if v == dominant_count]
    primary_bin = min(candidate_bins)  # Use lowest bin if tie
    
    # Step 5: Apply decay factor based on bin position
    decay_factor = 0.8 if primary_bin < 5 else 0.6
    raw_score = primary_bin * dominant_count
    adjusted_score = raw_score * decay_factor
    
    # Step 6: Offset with magic constant from bit manipulation
    magic_offset = (17 ^ 23) & 0xF  # Results in 6
    
    # Final computation
    result = int(adjusted_score) + magic_offset
    
    # Dead code path (never executed)
    if False:
        backup = compute_entropy(step2)
        result = int(backup)
    
    return result

# Misleading intermediate analysis (unused)
aggregated = [x * 2 for x in sensor_data if x % 3 == 0]
anomaly_detected = any(abs(x) > 20 for x in aggregated)

# Key execution point
data = [14, 7, 11, 6, 3, 19, 4]
final_output = process_pipeline(data)

# Output the target result
print(f"Result: {final_output}")