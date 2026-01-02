import itertools

# Simulated sensor data processing with red herrings and multiple transformations
def collect_readings():
    raw_signals = [1.2, 0.8, 3.1, 2.5, 0.9, 1.7, 2.2]
    noise_floor = 0.5
    filtered = [x for x in raw_signals if x > noise_floor]
    return filtered

# Irrelevant auxiliary function (decoy)
def calculate_efficiency(metrics):
    if not metrics:
        return 0.0
    total = sum(m * 1.3 for m in metrics)
    return total / len(metrics) if total > 10 else total * 0.7

# Unused transformation path (dead code)
def deprecated_normalize(data):
    max_val = max(data) if data else 1
    return [d / max_val for d in data]

# Core recursive pattern detector (used)
def detect_cycle(pattern, index=0, seen=None):
    if seen is None:
        seen = {}
    if index >= len(pattern):
        return False
    rounded = round(pattern[index], 1)
    if rounded in seen:
        return True
    seen[rounded] = index
    return detect_cycle(pattern, index + 1, seen)

# Bit manipulation red herring (irrelevant to final result)
def encode_flags(mode, debug, active):
    flag = 0
    if mode > 1:
        flag |= (1 << 3)
    if debug:
        flag ^= (1 << 1)
    if active:
        flag |= (1 << 0)
    return flag * 17  # arbitrary scaling

# Main transformation (used in critical path)
def transform_sequence(raw):
    shifted = [round(x * 1.1, 1) for x in raw]
    doubled = [x for x in shifted for _ in range(2)]  # duplicate each element
    truncated = doubled[:10]  # limit length
    return truncated

# Primary analysis function (critical path)
def analyze_pattern(data, limit):
    count = 0
    for a, b in zip(data, data[1:]):
        if b > a and (b - a) < 0.5:
            count += 1
    if count >= limit:
        return count * 113
    else:
        return -count * 47

# Entry point
if __name__ == '__main__':
    # Collect real data
    readings = collect_readings()
    
    # Apply actual transformation
    transformed_data = transform_sequence(readings)
    
    # Irrelevant variables (distractions)
    efficiency_score = calculate_efficiency(readings)
    encoding_flag = encode_flags(2, True, False)
    baseline_ref = [round(x, 1) for x in readings]
    
    # Critical control logic
    threshold = 4
    if len(transformed_data) >= 8:
        has_cycle = detect_cycle(transformed_data)
        if has_cycle:
            threshold += 1
        else:
            threshold -= 1
    
    # Final computation (answer depends on this)
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Unused alternative path (dead code)
    if False:
        temp = [x for x in transformed_data if x > 2.0]
        final_diagnostic = len(temp) * 100
    
    # Output result
    print(f"Result: {final_diagnostic}")