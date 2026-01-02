import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 0 <= x <= 100]
    smoothed = []
    for i in range(1, len(filtered) - 1):
        avg = (filtered[i-1] + filtered[i] + filtered[i+1]) / 3
        smoothed.append(round(avg, 2))
    return smoothed

# Irrelevant helper: calculates statistical dispersion (not used in final result)
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Distraction function: processes timestamps but ultimately unused
def generate_timeline(start, count, step=1.5):
    timeline = []
    for i in range(count):
        timeline.append(round(start + i * step, 2))
    return timeline

timestamps = generate_timeline(100.0, 50)  # Dead code path
variance_snapshot = calculate_variance([12, 15, 18, 22, 25])  # Misleading computation

# Core transformation pipeline
def transform_signal(readings, factor=0.87):
    amplified = [r * factor for r in readings]
    # Apply non-linear correction using slicing and lambda
    corrector = lambda x: math.log(x + 1) if x > 10 else math.sqrt(x)
    corrected = [round(corrector(val), 3) for val in amplified]
    return corrected[::2]  # Every other element — meaningful slicing

# Decoy pattern matcher (never called)
def detect_anomaly_pattern(seq):
    anomalies = []
    for i in range(len(seq)):
        if seq[i] < 0 or seq[i] > 50:
            anomalies.append(i)
    return anomalies

# Real pattern analyzer with embedded logic chain
def analyze_pattern(data, threshold_fn):
    count = 0
    cumulative = 0.0
    # Nested conditional counting with string-based flag encoding
    flags = ''
    for idx, val in enumerate(data):
        if threshold_fn(val):
            count += 1
            cumulative += val
            # Encoding decision path as characters
            if val > 15:
                flags += 'H'
            elif val > 10:
                flags += 'M'
            else:
                flags += 'L'
    
    # Complex derived metric: combination of count, average, and flag hash
    avg = cumulative / count if count else 0
    flag_score = sum(ord(c) * (i + 1) for i, c in enumerate(flags))  # weighted char sum
    
    # String manipulation red herring
    reversed_flags = flags[::-1]
    duplicate_check = ''.join(sorted(set(flags)))
    
    # Final diagnostic combines multiple concepts
    diagnostic_base = int(avg * 1.76)
    final_score = diagnostic_base + (flag_score % 199)
    
    # Unused intermediate values — distractions
    peak_magnitude = max(data) * (len(flags) % 7)
    entropy_proxy = -sum(math.log(f / len(flags)) for f in [flags.count(c) for c in set(flags)])
    
    return final_score

# Orchestration block
def main_pipeline():
    # Initial sensor input
    raw_input = [10, 14, 16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100]
    
    # Step 1: Preprocess
    cleaned = preprocess_readings(raw_input)
    
    # Step 2: Transform
    transformed_data = transform_signal(cleaned)
    
    # Threshold logic based on dynamic condition
    dynamic_limit = 12.5
    threshold_func = lambda x: x > dynamic_limit and math.sin(x) > -0.9
    
    # Critical statement
    final_diagnostic = analyze_pattern(transformed_data, threshold_func)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Additional noise: unused aggregation
    summary_report = {
        'count': len(transformed_data),
        'max_val': max(transformed_data),
        'checksum': sum(int(x) for x in transformed_data) ^ 255,
        'version': 'DIAG-2.1'
    }
    
    return final_diagnostic

# Execute
result_value = main_pipeline()