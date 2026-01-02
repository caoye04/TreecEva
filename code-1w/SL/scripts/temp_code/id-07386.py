import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [i * 0.5 for i in range(20)]
    filtered = [x for x in raw_samples if x > 5.0]
    return [round(math.sin(x) * 100, 2) for x in filtered]

# Irrelevant auxiliary function - dead code path (distractor)
def compute_entropy(data):
    total = 0
    for x in data:
        if x != 0:
            total -= x * math.log(abs(x))
    return round(total, 4)

# Data transformation with bitwise interference
def transform_signal(raw_values):
    shifted = []
    mask = 0b1111
    for i, val in enumerate(raw_values):
        # Meaningful transformation mixed with noise
        temp_val = int(abs(val)) ^ (i & mask)  # XOR with index bits
        if temp_val % 3 == 0:
            temp_val = (temp_val << 1) + 1
        else:
            temp_val = temp_val >> 1
        shifted.append(temp_val)
    return shifted

# Diagnostic engine - core logic
valid_codes = {23, 46, 58, 62, 71, 85}
diag_history = []

# Misleading accumulation (red herring)
cumulative_trace = 0
def analyze_pattern(metrics):
    global cumulative_trace
    result = 0
    threshold = len(metrics) * 2

    # Complex control flow with nested conditions
    for idx, m in enumerate(metrics):
        cumulative_trace += m  # Distractor: accumulates but not used in answer

        if m < 0:
            continue
        elif m > threshold:
            result += m // 3
        else:
            # Core calculation path
            mod_val = m % 7
            if mod_val in {1, 3, 5}:
                result += mod_val ** 2
            else:
                result -= mod_val

        # Dead branch - never executed due to data range (misleading)
        if m > 1000:
            result = -1
            break

    # Secondary transformation on result
    if result > 100:
        result = (result & 0xFF) + 17  # Bit masking
    else:
        result = (result ^ 42) + 8

    # Final check against valid codes (simulated calibration)
    while result not in valid_codes:
        result = (result + 1) % 100
        diag_history.append(result)  # Logs irrelevant debug info

    return result

# Unused function - decoy for signal modeling
def predict_trend(data):
    if len(data) < 5:
        return None
    avg = sum(data[-5:]) / 5
    return 'up' if avg > 0 else 'down'

# Main execution chain
sensor_data = collect_readings()
noise_floor = sum([x for x in sensor_data if x < -20])  # Irrelevant metric
transformed_metrics = transform_signal(sensor_data)
baseline_shift = len(sensor_data) * 0.95  # Red herring variable
intermediate_checksum = sum(transformed_metrics) & 0xFFFF  # Misleading checksum
final_diagnostic = analyze_pattern(transformed_metrics)
print(f"Result: {final_diagnostic}")