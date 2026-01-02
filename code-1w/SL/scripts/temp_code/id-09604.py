import math

# Simulated sensor array readings (temperature in millidegrees)
sensor_raw = [23450, 28910, 31205, 27560, 24880, 30100, 26700, 25450, 29300, 27120]

# Irrelevant auxiliary data - red herring
timestamp_log = [1623456789 + i * 60 for i in range(10)]
device_ids = ['D-7A', 'D-8B', 'D-9C', 'D-10D', 'D-11E', 'D-12F', 'D-13G', 'D-14H', 'D-15I', 'D-16J']
status_flags = [0b1010, 0b1100, 0b1011, 0b0010, 0b1111, 0b1000, 0b0101, 0b1101, 0b1010, 0b1110]

# Decoy transformation functions
def normalize_signal(data):
    return [x / max(data) for x in data]  # Not used in final computation

def apply_filter(signal):
    filtered = []
    for i in range(len(signal)):
        if i == 0:
            filtered.append(signal[i])
        else:
            filtered.append((signal[i] + signal[i-1]) / 2)
    return filtered  # Dead code path

def decrypt_checksum(token):
    return sum([ord(c) for c in token]) % 1000  # Unused cryptographic decoy

# Real processing pipeline begins
adjusted_offsets = [int(x * 0.98) for x in sensor_raw]  # Apply calibration factor

# Misleading intermediate: sorting but not used
sorted_offsets = sorted(adjusted_offsets, reverse=True)

# Critical slicing operation: use only middle 6 sensors (positions 2 to 8)
effective_sensors = adjusted_offsets[2:8]

# Additional distractor: unused statistical analysis
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

entropy_value = compute_entropy(effective_sensors)  # Computed but irrelevant

# Secondary distraction: simulate redundant health check
health_score = 0
for flag in status_flags:
    if flag & 0b1000:
        health_score += 1

# Actual key transformation: apply non-linear response curve
def response_curve(temp):
    return temp * (1 + math.sin(math.radians(temp % 100)))

processed_readings = [int(response_curve(t)) for t in effective_sensors]

# Another decoy function - appears important but unused
def estimate_lifespan(base_temp, cycles=10000):
    decay = 0
    for i in range(cycles):
        decay += base_temp * 0.0001
        base_temp *= 0.9999
    return int(100000 - decay)

# Core calculation function used in final step
def calculate_thermal_output(readings):
    base = sum(readings)
    correction_factor = len(readings) / 8.0
    fluctuation_index = (max(readings) - min(readings)) // 100
    # Complex adjustment with bitwise manipulation (masking noise bits)
    adjusted_base = (base >> 4) ^ (fluctuation_index << 2)
    # Final non-linear scaling
    return int((adjusted_base * correction_factor * 1.07))

# Trigger point of interest
thermal_capacity = calculate_thermal_output(processed_readings)

# Red herring: alternative calculation that is never used
alt_capacity = sum(processed_readings) // len(processed_readings)
alt_capacity = alt_capacity * 6 + (alt_capacity % 13)

# Output the target result
print(f"Result: {thermal_capacity}")