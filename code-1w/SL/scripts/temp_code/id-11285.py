from collections import defaultdict, Counter

# Simulated sensor readings over time (temperature in tenths of °C)
sensor_data = [201, 203, 198, 205, 210, 180, 215, 220, 175, 225, 230, 160, 235, 240, 150]

def filter_anomalies(data, limit):
    # Irrelevant: Count frequency of values (distractor)
    freq = Counter(data)
    
    # Actual logic: Remove extreme outliers beyond threshold
    cleaned = []
    for val in data:
        if val > limit * 1.5:  # Arbitrary scaling to confuse
            continue
        if abs(val - 200) > 50 and val < 170:  # Real filter: exclude cold extremes below 170
            pass  # Dead code branch (misleading)
        elif val < 165:
            continue
        else:
            cleaned.append(val)
    
    # Decoy transformation (never used)
    normalized = [x / 10.0 for x in data if x > 0]
    stats_summary = {'min': min(cleaned), 'max': max(cleaned)}
    
    return cleaned

def generate_signature(sequence):
    # Unused function - red herring
    return sum(x * (i+1) for i, x in enumerate(sequence)) % 97

def compute_rolling_average(values, window=3):
    # Distractor: computes averages but not used in final path
    averages = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i+window]) / window
        averages.append(round(avg, 1))
    return averages

def analyze_readings(validated, log_output=None):
    # Log setup (irrelevant to result)
    if log_output is None:
        log_output = defaultdict(int)
    
    # Core logic hidden among distractions
    base_offset = 200
    adjustments = []
    
    for reading in validated:
        diff = reading - base_offset
        if diff == 0:
            adjustment = 0
        elif diff > 0:
            # Gradual decay model
            adjustment = int(diff * 0.8) if diff < 25 else int(diff * 0.6)
        else:
            # Negative diffs are clamped
            adjustment = max(-10, diff)
        adjustments.append(adjustment)
    
    # Secondary processing with decoy variables
    magnitude_score = sum(abs(a) for a in adjustments)
    trend_bias = sum(1 if a > 0 else -1 for a in adjustments)
    
    # Critical intermediate (looks important but isn't final)
    diagnostic_vector = [magnitude_score, trend_bias, len(adjustments)]
    
    # Real answer computation buried here
    cumulative_drift = 0
    for i, adj in enumerate(adjustments):
        weight = 1 if i % 2 == 0 else 0.5
        cumulative_drift += adj * weight
    
    # Final diagnostic calculation
    final_diagnostic = int(cumulative_drift * 1.1)  # Final transformation
    
    # Dead assignment (misleads about importance)
    final_diagnostic = final_diagnostic + 0  # No-op
    
    return final_diagnostic

def main():
    # Irrelevant configuration block
    config = {
        'sampling_rate': 10,
        'calibration_factor': 1.05,
        'threshold': 250  # Not directly used
    }
    
    # Actual threshold derived indirectly
    threshold = 240
    
    # Key statement that produces the target variable
    processed_data = filter_anomalies(sensor_data, threshold)
    diagnostics_log = []
    final_diagnostic = analyze_readings(processed_data, diagnostics_log)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Unused post-processing (dead path)
    if len(processed_data) > 10:
        signature = generate_signature(processed_data)
    
    return final_diagnostic

# Execute
main()