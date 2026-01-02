import math

# Simulated system health monitoring with performance evaluation

def analyze_signal_strength(signal_data, threshold=0.75):
    strong_signals = 0
    total_signals = len(signal_data)
    for val in signal_data:
        if val > threshold:
            strong_signals += 1
    return strong_signals / total_signals if total_signals else 0


def compute_entropy(data):
    # Irrelevant entropy calculation (dead-end function)
    from collections import Counter
    counts = Counter(data)
    probs = [count / len(data) for count in counts.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)


def extract_features(raw_log):
    # Extract numeric features from log strings
    features = []
    for line in raw_log:
        parts = line.split(',')
        try:
            # Parse specific fields
            timestamp = float(parts[0])
            voltage = float(parts[2])
            temp = float(parts[3])
            if temp > 40:
                voltage *= 0.9
            features.append((timestamp, voltage))
        except (IndexError, ValueError):
            continue
    return features


def filter_outliers(data, factor=1.5):
    # Dead code path — never used in execution
    if not data:
        return []
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]


def normalize_vector(vec):
    # Unused utility function (distractor)
    norm = math.sqrt(sum(x**2 for x in vec))
    return [x/norm for x in vec] if norm else vec


def calculate_efficiency(power_in, power_out):
    # Another irrelevant function (red herring)
    return power_out / power_in if power_in != 0 else 0


def build_lookup_table(keys, values):
    # Creates a map but unused in main logic
    return dict(zip(keys, values))


def evaluate_performance(metrics, baseline):
    score = 0
    adjustments = []
    
    # Real logic begins here — key operations mixed with noise
    for i, (name, val) in enumerate(zip(metrics.keys(), metrics.values())):
        ref_val = baseline.get(name, 1.0)
        deviation = abs(val - ref_val) / ref_val
        
        if name.startswith('sys_'):
            if deviation < 0.1:
                score += 10
            elif deviation < 0.2:
                score += 5
            else:
                score -= 3
        elif 'temp' in name:
            if val < 60:
                score += 7
            elif val < 75:
                score += 3
            else:
                score -= 8
        elif 'voltage' in name:
            if 3.2 <= val <= 3.4:
                score += 6
            elif 3.1 <= val < 3.2 or 3.4 < val <= 3.5:
                score += 2
            else:
                score -= 5
    
    # Complex adjustment chain
    for i, adj in enumerate(adjustments):
        score = score * (1 + adj) if adj > 0 else score + adj
    
    # Final nonlinear transformation
    if score > 0:
        score = math.log(score + 10) * 5
    else:
        score = score * 0.5
    
    # Key variable assignment point
    final_score = int(round(score * 2)) + 17
    
    return final_score

# --- Main Execution ---
if __name__ == '__main__':
    # Simulated telemetry input (real data source)
    raw_telemetry = [
        "1678886400,INFO,v=3.3,t=55.2,fail=0",
        "1678886401,WARN,v=3.45,t=74.1,fail=1",
        "1678886402,INFO,v=3.25,t=58.9,fail=0",
        "1678886403,ERR,v=2.9,t=88.0,fail=1"
    ]

    # Parse logs to extract values
    parsed_features = extract_features([line.replace('v=', ',').replace('t=', ',').replace('fail=', ',') 
                                      for line in raw_telemetry])

    voltages = [f[1] for f in parsed_features]
    temperatures = [float(line.split(',')[3]) for line in raw_telemetry]

    # Compute derived signal metric (used later)
    signal_quality = [math.sin(t/10) * 0.5 + 3.3 for t in temperatures]
    avg_signal = sum(signal_quality) / len(signal_quality)

    # Build actual metrics dictionary needed for evaluation
    metrics = {
        'sys_response_time': 0.118,
        'sys_throughput': 0.92,
        'temperature_avg': sum(temperatures)/len(temperatures),
        'voltage_stable': sum(voltages)/len(voltages)
    }

    # Benchmark baseline configuration (ground truth)
    benchmark_data = {
        'sys_response_time': 0.12,
        'sys_throughput': 0.90,
        'temperature_avg': 65.0,
        'voltage_stable': 3.3
    }

    # Irrelevant intermediate variables (distractors)
    temp_variance = sum((t - 65)**2 for t in temperatures) / len(temperatures)
    peak_voltage = max(voltages)
    normalized_voltages = normalize_vector(voltages)
    signal_ratio = analyze_signal_strength(signal_quality, threshold=0.7)

    # Decoy data structure
    decoy_map = build_lookup_table(['a','b','c'], [100,200,300])
    decoy_map['status'] = 'unrelated'

    # Core logic call — answer depends on this
    final_score = evaluate_performance(metrics, benchmark_data)

    # Output result as required
    print(f"Result: {final_score}")