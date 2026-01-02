import math

# Simulated sensor data from a distributed environmental monitoring system
def collect_sensor_data():
    raw_readings = [
        [0.8, 1.2, 0.9, 1.4],
        [1.1, 0.7, 1.3, 0.6],
        [0.5, 1.5, 1.0, 1.1],
        [1.3, 0.8, 0.7, 1.2]
    ]
    return raw_readings

# Legacy function - unused but looks relevant
def legacy_calibrate(data):
    adjusted = []
    for row in data:
        adjusted.append([x * 0.95 + 0.1 for x in row])
    return adjusted

# Signal processing with noise filtering and normalization
def preprocess_signal(raw_matrix):
    filtered = []
    for i, row in enumerate(raw_matrix):
        trend_compensated = [val - 0.05 * i for val in row]
        normalized = [max(min(val, 1.2), 0.6) for val in trend_compensated]
        filtered.append(normalized)
    return filtered

# Red herring: complex frequency analysis (never called)
def spectral_analysis(signal):
    fft_magnitude = 0
    for t in range(len(signal)):
        for f in range(1, 6):
            fft_magnitude += math.sin(2 * math.pi * f * t / len(signal))
    return fft_magnitude

# Real-time anomaly detection based on variance thresholds
def detect_anomalies(grid):
    anomalies = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            local_avg = sum(row) / len(row)
            if abs(val - local_avg) > 0.3:
                anomalies.append((i, j))
    return anomalies

# Decoy accumulator - collects nothing meaningful
def accumulate_diagnostics(logs):
    total_score = 0
    for entry in logs:
        for metric in entry:
            total_score += abs(metric) ** 0.5
    return total_score * 0.75

# Core metric transformation using list comprehensions and zip
def transform_metrics(grids):
    transposed_grids = [list(zip(*grid)) for grid in [grids]]
    flat_transposed = transposed_grids[0]
    
    # Compute column-wise stats
    col_means = [
        sum(col) / len(col) for col in flat_transposed
    ]
    
    # Apply non-linear gain
    amplified = [math.tanh(x) * 1.5 for x in col_means]
    return amplified

# Higher-order analysis combining spatial and temporal indicators
def compute_sti(metrics, time_factor=2.4):
    sti_values = []
    for idx, m in enumerate(metrics):
        spatial_weight = math.cos(idx * 0.4)
        temporal_component = time_factor * 0.1
        sti_values.append(m * spatial_weight + temporal_component)
    return sti_values

# Final diagnostic engine - combines multiple reasoning chains
def analyze_metrics(input_signals):
    # Step 1: Transform input using advanced statistical shaping
    shaped = transform_metrics(input_signals)
    
    # Step 2: Compute spatiotemporal index
    sti_result = compute_sti(shaped)
    
    # Step 3: Aggregate final score
    aggregate = 0
    for val in sti_result:
        if val > 0:
            aggregate += math.log(1 + val)
        else:
            aggregate -= math.log(1 - val)
    
    # Step 4: Apply final calibration (this is where answer is determined)
    final_diagnostic = int(round(aggregate * 1000))
    
    # Dead code branch - looks important but never executes
    if len(input_signals) > 10:
        backup = sum(shaped) * 2
        final_diagnostic = int(backup)
    
    return final_diagnostic

# Irrelevant utility function (distractor)
def generate_report_header(version):
    return f"=== DIAGNOSTIC REPORT v{version} ==="

# Unused global constants (red herrings)
CALIBRATION_OFFSET = 0.0034
MAX_ITERATIONS = 1500
THRESHOLD_ARRAY = [0.1, 0.3, 0.6, 0.8]

# Main execution flow
if __name__ == "__main__":
    # Collect raw sensor inputs
    signals = collect_sensor_data()
    
    # Preprocess to remove noise and bias
    processed_signals = preprocess_signal(signals)
    
    # Detect any outlying measurements
    anomaly_list = detect_anomalies(processed_signals)
    
    # Prepare dummy log for decoy function
    dummy_logs = [[1.2, 0.8], [0.9, 1.3]]
    decoy_score = accumulate_diagnostics(dummy_logs)
    
    # Perform core analysis
    final_diagnostic = analyze_metrics(processed_signals)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")