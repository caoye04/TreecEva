from itertools import combinations

# Simulate sensor readings with noise and redundancy
def collect_sensor_data():
    raw_readings = [18, 23, 15, 42, 37, 29, 31]
    noise_offsets = [3, -1, 2]
    adjusted = [r + noise_offsets[i % len(noise_offsets)] for i, r in enumerate(raw_readings)]
    return adjusted

# Filter out anomalous values using sliding window logic
def filter_anomalies(data):
    filtered = []
    for i in range(2, len(data)):
        window = data[i-2:i+1]
        avg = sum(window) // len(window)
        if abs(data[i] - avg) <= 15:
            filtered.append(data[i])
    return filtered

# Generate diagnostic pairs for cross-validation
def generate_pairs(values):
    pairs = list(combinations(values, 2))
    diffs = [abs(a - b) for a, b in pairs]
    return diffs

# Apply bitmask correction based on hardware status
def apply_hardware_mask(values, mask=0b1101):
    corrected = []
    for v in values:
        masked_val = v ^ (mask & 0b111)  # Use only first 3 bits of mask
        corrected.append(masked_val)
    return corrected

# Compute rolling parity for error detection
def compute_parity(values):
    parities = []
    for val in values:
        binary = bin(val)[2:]
        parity_bit = binary.count('1') % 2
        parities.append(parity_bit)
    overall_parity = sum(parities) % 2
    return overall_parity

# Final validation using weighted sum
def final_validation(data):
    weights = [1, 3, 2, 1, 3, 2, 1][:len(data)]
    weighted_sum = sum(d * weights[i] for i, d in enumerate(data))
    return weighted_sum % 107  # Modulo prime to reduce range

# Misleading auxiliary function (dead code path)
def deprecated_normalization(x):
    return [val / max(x) for val in x]

# Unused intermediate tracking variables
timestamp_log = [1672540800, 1672540860, 1672540920]
redundant_flags = [True, False, True, True]

# Main execution chain
readings = collect_sensor_data()
cleaned = filter_anomalies(readings)
diagnostic_diffs = generate_pairs(cleaned)
masked_values = apply_hardware_mask(cleaned)
parity_check = compute_parity(masked_values)

# Key computation point
checksum = final_validation(masked_values)

# Print result as required
print(f"Result: {checksum}")