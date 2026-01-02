import math

# Simulated sensor data processing with diagnostic logic
def collect_readings():
    raw_values = [i * 0.7 for i in range(30)]
    offset = sum([v ** 0.5 for v in raw_values if v > 5]) / 10
    return [round(v + offset, 3) for v in raw_values]

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(x):
    return [val * 1.02 for val in x if val < 15]

# Transform readings using sliding window and exponential smoothing
def preprocess_stream(data):
    window_size = 4
    smoothed = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        avg = sum(window) / len(window)
        exp_weight = math.exp(-0.1 * i)
        smoothed.append(avg * exp_weight)
    return [round(s, 4) for s in smoothed]

# Bit manipulation to generate control flags (some irrelevant)
def generate_flags(length):
    flags = []
    for i in range(length):
        flag = (i ^ 0xCAF) & 0xFF
        flag = (flag << 1) | (flag >> 7)
        flags.append(flag % 17)
    return flags

# Real transformation: maps data through nonlinear compression
# Only this part feeds into the final analysis
# Distractor: multiple unused intermediate variables

def transform_signal(sequence):
    base_shift = 1.414
    compressed = [(abs(x) ** 0.8) * math.cos(x * 0.1) + base_shift for x in sequence]
    filtered = [c for c in compressed if c > 0.5]  # Filter out low values
    return [round(f, 5) for f in filtered]

# Threshold map generation with red herring logic
# Some thresholds are never used

def build_thresholds(count):
    temp_ref = [math.log(n + 2) for n in range(count)]
    phase_shifts = [math.sin(t) for t in temp_ref]
    unused_checksum = sum(phase_shifts) * 0xDEADBEEF % 100
    
    # Actual used thresholds
    critical = [t * 1.618 for t in temp_ref]
    warning = [t * 0.618 for t in temp_ref]
    
    # Return only the one used in analysis
    return {"critical": critical}

# Core analysis: counts how many transformed points exceed dynamic thresholds
def analyze_pattern(data, limits):
    threshold_line = limits["critical"][:len(data)]  # Truncate to match
    anomalies = 0
    debug_logs = []
    for i, point in enumerate(data):
        # Misleading comparison with unused warning level
        if i < len(threshold_line) and point > threshold_line[i]:
            anomalies += 1
            debug_logs.append((i, point))
    # Final result derived from non-trivial interaction
    scaling_factor = 3.141592
    result = int(anomalies * scaling_factor * 100) / 100  # Emulate fixed-point
    return result

# Unused but plausible-looking diagnostic chain

def post_validate(diag, data):
    if diag > len(data) * 0.3:
        return "REVIEW"
    return "OK"

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor readings
    sensor_input = collect_readings()
    
    # Step 2: Preprocess with smoothing (used)
    processed_signal = preprocess_stream(sensor_input)
    
    # Step 3: Generate control flags (distractor - not used)
    security_flags = generate_flags(len(processed_signal))
    
    # Step 4: Transform signal with nonlinear compression (used)
    transformed_data = transform_signal(processed_signal)
    
    # Step 5: Build threshold map (only 'critical' is used)
    threshold_map = build_thresholds(len(transformed_data) + 10)  # Extra length to distract
    
    # Step 6: Analyze pattern against thresholds
    final_diagnostic = analyze_pattern(transformed_data, threshold_map)
    
    # Print target result
    print(f"Result: {final_diagnostic}")