def analyze_signal(samples, threshold=0.75):
    # Irrelevant signal processing steps
    normalized = [x / max(samples) for x in samples]
    filtered = [x for x in normalized if x > threshold]
    peak_count = len(filtered)
    avg_power = sum(x**2 for x in normalized) / len(normalized)
    return peak_count * avg_power


def generate_checksum(data):
    # Distractor: Unused checksum logic
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val + i) % 256
    return checksum

# Simulated sensor readings
temperature_stream = [23.4, 22.9, 24.1, 25.3, 26.0, 25.8, 24.7]
humidity_stream = [45, 47, 50, 55, 60, 58, 52]

# Misleading data transformation
aggregated_diagnostics = []
for t, h in zip(temperature_stream, humidity_stream):
    score = (t * 1.2) + (h * 0.3)  # Obsolete scoring formula
    aggregated_diagnostics.append(score)

# Unused recursive function as red herring
def compute_depth_factor(n):
    if n <= 1:
        return 1
    return n + compute_depth_factor(n - 2)

# Core calibration sequence with relevant operations
base_calibration = [1, 1, 2, 3, 5, 8, 13]
mod_sequence = [x % 4 for x in base_calibration]
shifted_mod = [(x << 1) ^ 3 for x in mod_sequence]  # Bit manipulation

# Error detection flags based on modular arithmetic
error_flags = []
for i, val in enumerate(shifted_mod):
    if (val + i) % 3 == 0:
        error_flags.append(1)
    else:
        error_flags.append(0)

# Linear search for first critical offset
offset_index = -1
for idx, flag in enumerate(error_flags):
    if flag == 1 and offset_index == -1:
        offset_index = idx

# Decoy list comprehension with no downstream use
decoy_analysis = [
    (i, temperature_stream[i] ** 0.5) 
    for i in range(len(temperature_stream)) 
    if i % 2 == 0
]

# Main metric processor - depends only on specific paths
def process_metrics(seq, errors):
    total = 0
    for i, (val, e_flag) in enumerate(zip(seq, errors)):
        if e_flag:
            total += (val * (i + 1))  # Weighted contribution
        else:
            total -= (val % 3)  # Small penalty
    # Final adjustment using offset from linear search
    total += offset_index * 2
    return total

# Execute key computation
calibration_sequence = shifted_mod
final_diagnostic = process_metrics(calibration_sequence, error_flags)

# Dead code path - never executed
def unused_postprocess(data):
    return sorted(data, reverse=True)

# Output result
print(f"Result: {final_diagnostic}")