import math

def analyze_signal_strength(signal_data, threshold=0.75):
    # Irrelevant function: signal analysis (dead end)
    filtered = [x for x in signal_data if x > threshold]
    return len(filtered) * 0.3

def preprocess_metrics(raw):
    # Distractor: preprocessing that isn't actually used later
    cleaned = [max(0, x - 0.1) for x in raw]
    return [round(x, 2) for x in cleaned]

def calculate_entropy(values):
    # Misleading mathematical transformation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def validate_consistency(trace_log):
    # Unused validation logic (red herring)
    if len(trace_log) < 5:
        return False
    gaps = [trace_log[i+1] - trace_log[i] for i in range(len(trace_log)-1)]
    return all(abs(g) < 1 for g in gaps)

def compute_rolling_average(data, window=3):
    # Decoy function with unused result
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(avg)
    return averages

def evaluate_component_health(temps, limits):
    # Another distractor: hardware monitoring
    overheat_count = sum(1 for t, l in zip(temps, limits) if t > l)
    return overheat_count < 2

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    base = 0
    for i, (m, w) in enumerate(zip(metrics, weights)):
        if i % 2 == 0:
            base += m * w * 1.1
        else:
            base += m * w * 0.9
    
    adjustment = 0
    if metrics[0] > 0.5:
        adjustment += 15
    if sum(1 for m in metrics if m > 0.6) >= 3:
        adjustment += 10
    
    # Key computation embedded in conditional logic
    if adjustment > 0:
        base *= 1.2
    
    # Final nonlinear transformation
    final = int(base + adjustment + 5)
    
    # Dead code branch (never reached due to structure)
    if final < 0:
        final = 0
        
    return final

# Main execution flow
if __name__ == "__main__":
    # Real input data
    raw_metrics = [0.82, 0.76, 0.88, 0.63, 0.91]
    benchmark_weights = [1.0, 0.8, 1.2, 0.9, 1.1]
    
    # Irrelevant data structures (distractors)
    system_temps = [67, 72, 65, 78, 70]
    temp_limits = [80, 85, 80, 82, 75]
    signal_readings = [0.81, 0.69, 0.77, 0.83, 0.71, 0.85]
    trace_timestamps = [1.0, 1.9, 3.1, 4.0, 5.2]
    
    # Unused transformations
    cleaned_metrics = preprocess_metrics(raw_metrics)
    entropy = calculate_entropy(raw_metrics)
    rolling_avgs = compute_rolling_average([int(x*100) for x in raw_metrics])
    
    # Red herring calls
    signal_count = analyze_signal_strength(signal_readings)
    is_consistent = validate_consistency(trace_timestamps)
    hardware_ok = evaluate_component_health(system_temps, temp_limits)
    
    # Critical execution point
    final_score = evaluate_performance(raw_metrics, benchmark_weights)
    
    # Output the target result
    print(f"Result: {final_score}")