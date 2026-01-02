import math

# Simulated sensor array data (irrelevant in part)
sensor_readings = [14.2, 18.7, 22.1, 19.5, 25.3, 30.0, 17.8, 20.4]
offset_compensation = sum([math.sin(r / 10) for r in sensor_readings])
filtered_diagnostics = [r for r in sensor_readings if r > 18.0]

# Historical benchmark values (red herring)
historical_averages = {"Q1": 19.2, "Q2": 20.5, "Q3": 21.8, "Q4": 23.0}
seasonal_adjustment = (historical_averages["Q3"] - historical_averages["Q1"]) * 0.75

# Core system parameters (some irrelevant)
system_id = 0xABCDEF
activation_epoch = 1672531200
lifecycle_stage = 'calibration'
validation_key = (system_id ^ activation_epoch) & 0xFFFF

# Data processing chain setup (mixed relevance)
base_sequence = list(range(1, 15))
transformed = [x**2 - 3*x + 2 for x in base_sequence]
masked_data = [y for y in transformed if y % 2 == 1]  # Only odd values kept

# Decoy statistical analysis (entirely irrelevant)
correlation_proxy = 0
for i in range(len(masked_data) - 1):
    correlation_proxy += masked_data[i] * masked_data[i+1]
correlation_proxy = correlation_proxy / len(masked_data)

# Actual relevant computation begins here
prime_flags = []
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for val in transformed:
    prime_flags.append(is_prime(abs(val)))

# Bit manipulation layer (partially relevant)
bit_encoded = 0
for i, flag in enumerate(prime_flags):
    if flag:
        bit_encoded |= (1 << (i % 16))

# Control flow with red herrings
checksum = 0
for ch in f"SYS-{lifecycle_stage.upper()}-{validation_key}":
    checksum += ord(ch) % 17
decoys_active = (checksum % 3 == 0)

# Real logic: find positions where transformed[i] > 20 and prime
qualified_indices = []
for i in range(len(transformed)):
    if transformed[i] > 20 and prime_flags[i]:
        qualified_indices.append(i)

# Secondary filtering based on index properties
index_sum = sum([idx for idx in qualified_indices if idx % 2 == 1])

# Tertiary filter: must have corresponding even-valued neighbor
robust_values = []
for idx in qualified_indices:
    neighbors = []
    if idx > 0: neighbors.append(transformed[idx-1])
    if idx < len(transformed)-1: neighbors.append(transformed[idx+1])
    if any(n % 2 == 0 for n in neighbors):
        robust_values.append(transformed[idx])

# Aggregation pipeline (core answer path)
processing_chain = set(robust_values)
thresholds = {"min": 25, "max": 200, "step": 5}

def aggregate_metrics(data_set, limits):
    result = 0
    sorted_vals = sorted(data_set)
    for val in sorted_vals:
        if limits["min"] <= val <= limits["max"]:
            # Contribution based on distance to center
            center = (limits["min"] + limits["max"]) / 2
            contribution = abs(val - center) // limits["step"]
            result += int(contribution)
    # Final adjustment based on bit pattern (actual dependency)
    global bit_encoded
    extra_mod = (bit_encoded & 0xFF) % 7
    return result + extra_mod

# Execution point of interest
final_diagnostic = aggregate_metrics(processing_chain, thresholds)

# Irrelevant logging output (distraction)
log_entry = f"Diag:{hex(bit_encoded)[:6]}|C:{correlation_proxy:.2f}|S:{index_sum}"

# Critical print statement (must include this format)
Result: final_diagnostic