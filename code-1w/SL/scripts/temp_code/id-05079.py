from collections import defaultdict
import math

# Simulated sensor data processing with noise filtering and hash derivation
def process_sensor_readings(raw_data, threshold=0.75):
    filtered_data = []
    noise_counter = defaultdict(int)
    temp_buffer = []
    cumulative_power = 0
    normalization_factor = 1.0

    for reading in raw_data:
        # Irrelevant noise tracking (distractor)
        signal_type = 'A' if reading > 0 else 'B'
        noise_counter[signal_type] += 1

        if abs(reading) < threshold:
            continue  # Filter out low-amplitude noise

        # Signal amplification and power accumulation (partially relevant)
        amplified = abs(reading) ** 1.5
        cumulative_power += amplified

        if cumulative_power > 100:
            cumulative_power /= 2  # Prevent overflow (red herring)

        temp_buffer.append(int(amplified * 10) % 97)

    # Dead code path - never reached due to logic above (decoy)
    if len(noise_counter) > 100:
        normalization_factor = math.log(len(noise_counter))

    # Dummy transformation chain with misleading intermediate values
    transformed = [val ^ 17 for val in temp_buffer if val % 2 == 1]
    shifted = [(x << 2) % 97 for x in transformed]  # Bit manipulation red herring

    # Unused statistical computation (distractor)
    avg_shift = sum(shifted) / len(shifted) if shifted else 0
    variance = sum((x - avg_shift) ** 2 for x in shifted) / len(shifted) if shifted else 0

    # Core logic hidden among distractions: prepare salt from initial data
    salt = len(raw_data) % 23
    if salt == 0:
        salt = 5

    # Critical function call buried in complexity
    checksum = finalize_hash(temp_buffer, salt)
    return checksum


def finalize_hash(buffer, salt):
    result = salt * 31
    for i, val in enumerate(buffer):
        result ^= val * (i + 1)
        result = (result + (result << 5)) % 1000007  # Simulated hash diffusion
    return result % 1000000

# Misleading auxiliary function (never called - decoy)
def compute_entropy(data):
    freq = defaultdict(float)
    total = len(data)
    for x in data:
        freq[x] += 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused but plausible-looking initialization data (distractor)
initial_calibration = [0.12, 0.88, -0.45, 0.63, 1.21, -0.91, 0.05]
calibration_weights = [w ** 2 for w in initial_calibration if w > 0.5]

# Simulated input - deterministic sensor trace
sensor_trace = [0.1, -0.3, 0.8, 1.2, -0.9, 0.05, 1.1, -1.3, 0.77, 2.1, -0.4, 0.95]

# Main execution flow obscured by surrounding noise
final_output = process_sensor_readings(sensor_trace)

# Key variable assignment
checksum = finalize_hash([x for x in range(len(sensor_trace)) if x % 3 == 0], final_output % 19)

print(f"Result: {checksum}")