import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    timestamps = list(range(100, 200, 3))
    signals = []
    for t in timestamps:
        raw = (t * 1.5) + math.sin(t / 10) * 5
        signals.append(round(raw, 2))
    return dict(zip(timestamps, signals))

# Irrelevant auxiliary function – dead code path
def deprecated_calibrate(x):
    if x < 0:
        return x ** 2 + 100
    else:
        return abs(x - 42)

# Misleading preprocessing chain with decoy transformations
def preprocess_stream(log_data):
    temp_buffer = []
    scaling_factor = 0.87
    offset_correction = 2.1
    
    for key, val in log_data.items():
        adjusted = val * scaling_factor + offset_correction
        if adjusted > 150:
            adjusted = 150  # clamp
        temp_buffer.append(adjusted)
    
    # Dead branch: never executed due to data range
    if len(temp_buffer) > 1000:
        temp_buffer = [x * 1.1 for x in temp_buffer]
    
    # Decoy statistical distraction
    mean_val = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in temp_buffer) / len(temp_buffer) if temp_buffer else 0
    entropy_distractor = -sum((x / 1000) * math.log2(x / 1000 + 1e-8) for x in temp_buffer)
    
    return temp_buffer

# Core diagnostic engine with nested logic and red herrings
def analyze_metrics(system_log):
    diagnostics = {}
    
    # Real computation begins: extract raw values
    raw_values = list(system_log.values())
    n = len(raw_values)
    
    # Irrelevant dictionary used only once then ignored
    aux_metadata = {
        'version': '2.1.5',
        'mode': 'diagnostic',
        'checksum': 0xDEADBEEF,
        'flags': [True, False, True]
    }
    
    # Distractor loop: computes but doesn't use result
    cumulative_product = 1
    for v in raw_values[:10]:
        if v > 0:
            cumulative_product *= int(v % 7)
    backfill_reference = cumulative_product % 997
    
    # Real processing path starts here — multi-step reasoning
    filtered = [v for v in raw_values if 120 <= v <= 160]
    if not filtered:
        return -1
    
    squared_devs = [(x - 140) ** 2 for x in filtered]
    avg_sq_dev = sum(squared_devs) / len(squared_devs)
    std_est = math.sqrt(avg_sq_dev)
    
    # Bit manipulation red herring
    bit_analysis = 0
    for i, x in enumerate(filtered):
        if i % 5 == 0:
            bit_analysis ^= int(x) & 0xF
    
    # Conditional override path — looks important but unused
    if std_est < 5.0 and bit_analysis > 8:
        candidate_fix = sum(filtered) // len(filtered)
        for k in system_log:
            system_log[k] += 0.5  # no effect on output

    # Key transformation: non-obvious dependency on initial raw structure
    index_map = {i: idx for i, idx in enumerate(sorted(system_log.keys(), reverse=True)[:len(filtered)])}
    mapped_sum = sum(filtered[i] * (index_map[i] % 7) for i in range(len(filtered)))
    
    # Final computation — depends on filtered data and index weights
    base_score = sum(filtered) / 10
    weight_adjustment = sum((i + 1) % 4 for i in range(len(filtered)))
    final_diagnostic = int(base_score - weight_adjustment + mapped_sum // 100)
    
    # Critical print for observable output
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Generate realistic telemetry log
    system_log = generate_telemetry()
    
    # Preprocessing call with no side effects — misleading usage
    _ = preprocess_stream(system_log)
    
    # Actual critical statement
    final_diagnostic = analyze_metrics(system_log)
    
    # Output result
    print(f"Result: {final_diagnostic}")