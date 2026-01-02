import math

# Simulated sensor data processing with embedded diagnostics
def collect_telemetry():
    raw_signals = [i * 0.25 for i in range(80)]
    noise_floor = sum([math.sin(x) * 0.1 for x in raw_signals])
    calibrated = [math.cos(x) + noise_floor for x in raw_signals]
    return calibrated

# Irrelevant signal smoothing (dead path)
def smooth_signal(data, window=3):
    temp_result = []
    for i in range(len(data)):
        start = max(0, i - window)
        segment = data[start:i+1]
        avg = sum(segment) / len(segment)
        temp_result.append(avg)
    return temp_result  # Never used

# Data slicing and transformation
def preprocess(stream):
    if len(stream) < 50:
        return [0]
    snapshot = stream[10:70]  # Meaningful slice
    downsampled = [snapshot[i] for i in range(0, len(snapshot), 4)]
    offset = sum(downsampled[:5]) * 0.01
    adjusted = [x + offset for x in downsampled]
    return adjusted

# Diagnostic engine with red herring counters
def run_diagnostics(samples):
    counter_a = 0
    counter_b = 0
    debug_state = []
    for val in samples:
        if val > 0.5:
            counter_a += 1
        elif val < -0.5:
            counter_b += 1
        debug_state.append(counter_a - counter_b)  # Distractor
    final_score = sum(debug_state) * 0.1  # Misleading metric
    return final_score

# Core analysis logic (uses slicing and conditional logic)
def analyze_pattern(seq):
    magnitude = sum([abs(x) for x in seq])
    peaks = [i for i in range(1, len(seq)-1) if seq[i-1] < seq[i] > seq[i+1]]
    troughs = [i for i in range(1, len(seq)-1) if seq[i-1] > seq[i] < seq[i+1]]
    volatility = len(peaks) + len(troughs)
    trend = seq[-1] - seq[0]
    if volatility > 10:
        adjustment = magnitude * 0.2
    else:
        adjustment = magnitude * 0.05
    # Key computation
    return int((magnitude + adjustment) * abs(trend))

# Orchestration function with decoy logic
def evaluate_system_health():
    telemetry = collect_telemetry()
    
    # Dead code path 1: Unused normalization
    normalized = [x / (max(telemetry) + 1e-9) for x in telemetry]
    entropy = -sum([x * math.log(abs(x) + 1e-9) for x in normalized])
    
    # Dead code path 2: Unused recursive filter
    def filter_recursive(data, threshold=0.1):
        if len(data) <= 1:
            return data
        pivot = len(data) // 2
        left = filter_recursive(data[:pivot], threshold)
        right = filter_recursive(data[pivot+1:], threshold)
        if abs(data[pivot]) > threshold:
            return left + [data[pivot]] + right
        return left + right
    
    processed_data = preprocess(telemetry)
    
    # Red herring diagnostic call
    dummy_diagnostic = run_diagnostics(processed_data)
    
    # Additional irrelevant dictionary mapping
    status_map = {
        'low': [],
        'medium': [],
        'high': []
    }
    for val in processed_data:
        key = 'low' if abs(val) < 0.2 else 'medium' if abs(val) < 0.6 else 'high'
        status_map[key].append(val)
    
    # Actual critical computation path
    base_analysis = analyze_pattern(processed_data)
    secondary_metric = len([x for x in processed_data if x > 0])
    
    # Final integration step
    final_diagnostic = base_analysis - secondary_metric
    
    # Output requirement
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    evaluate_system_health()