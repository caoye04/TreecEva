from itertools import combinations

# Simulate system performance metrics under varying load conditions
def collect_diagnostics(base_load, duration):
    diagnostics = []n    peak_memory = 0
    total_cycles = 0

    for i in range(duration // 10):
        load_snapshot = (base_load + i * 5) % 90 + 10
        computation_cycle = (load_snapshot ** 2) % 101
        total_cycles += computation_cycle

        if computation_cycle > 85:
            peak_memory += 1

        diagnostics.append(computation_cycle)

    avg_diagnostic = sum(diagnostics) / len(diagnostics) if diagnostics else 0
    return avg_diagnostic, peak_memory, total_cycles

# Filter anomalous patterns using sliding window analysis
def detect_anomalies(data_stream, threshold=75):
    anomalies = []
    for i in range(len(data_stream) - 2):
        window = data_stream[i:i+3]
        if sum(window) / 3 > threshold and window[1] != 0:
            anomalies.append(i)
    return anomalies if anomalies else [0]

# Compute signal coherence across subsystems
def calculate_coherence(readings):
    coherent_pairs = 0
    for a, b in combinations(readings, 2):
        if abs(a - b) < 15:
            coherent_pairs += 1
    return coherent_pairs / len(readings) if readings else 0

# Evaluate overall system performance based on multiple weighted metrics
def evaluate_performance(metrics, weights):
    score = 0.0
    for i, weight in enumerate(weights):
        score += metrics[i] * weight
    
    # Apply nonlinear adjustment for stability factor
    stability = metrics[2]
    if stability > 40:
        score *= 1.15
    elif stability < 20:
        score *= 0.85
    
    return int(score)

# Main execution flow
if __name__ == "__main__":
    base_load = 25
    duration = 100

    # Collect low-level diagnostics
    avg_diag, peak_mem, total_ops = collect_diagnostics(base_load, duration)
    
    # Generate synthetic signal readings
    signal_readings = [avg_diag * (1 + i * 0.1) for i in range(8)]
    signal_readings = [int(x % 100) for x in signal_readings]
    
    # Detect any anomalous behavior windows
    anomaly_indices = detect_anomalies(signal_readings, threshold=60)
    
    # Calculate cross-signal coherence
    coherence = calculate_coherence(signal_readings)
    
    # Prepare evaluation metrics: [average diagnostic, memory peaks, coherence, total operations]
    metrics = [
        avg_diag,           # Normalized system activity
        peak_mem,            # High-load memory pressure events
        coherence * 100,     # Inter-signal consistency scaled to percentage
        total_ops % 50       # Cyclic operation residue
    ]
    
    # Weight vector for scoring (empirically calibrated)
    weights = [0.3, 0.2, 0.4, 0.1]
    
    # Compute final performance score
    final_score = evaluate_performance(metrics, weights)
    
    # Irrelevant secondary calculation (distractor)
    expected_median = sorted(signal_readings)[len(signal_readings)//2]
    outlier_count = 0
    for val in signal_readings:
        if abs(val - avg_diag) > 30:
            outlier_count += 1
    
    # This print is required for result extraction
    print(f"Result: {final_score}")