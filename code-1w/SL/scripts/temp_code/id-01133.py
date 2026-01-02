def analyze_component(reading, threshold=75):
    """Irrelevant helper function for sensor analysis."""
    if reading > threshold:
        return (reading - threshold) * 1.5
    else:
        return (threshold - reading) * 0.5


def accumulate_signals(signal_list):
    """Accumulates signal strengths with exponential backoff (unused)."""
    total = 0.0
    for i, val in enumerate(signal_list):
        total += val / (2 ** i)
    return total

def transform_data(entries):
    """Applies logarithmic scaling to data entries."""
    import math
    transformed = []
    for e in entries:
        if e > 0:
            transformed.append(math.log(e) * 1.2)
        else:
            transformed.append(0.0)
    return transformed

def validate_stability(readings):
    """Calculates stability score based on variance (distractor)."""
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return 100 - min(variance, 100)

def extract_key_metrics(data_stream):
    """Extracts peak, average, and anomaly count from stream."""
    peak = max(data_stream)
    avg = sum(data_stream) / len(data_stream)
    anomalies = sum(1 for x in data_stream if x > 90)
    return {'peak': peak, 'average': avg, 'anomalies': anomalies}

def calculate_efficiency_index(values):
    """Computes efficiency using bitwise manipulation (red herring)."""
    index = 0
    for v in values:
        index ^= int(v) & 0xFF
        index = (index << 1) | (index >> 7)
    return index % 100

def evaluate_performance(log, weight_map):
    """Main evaluation logic: computes weighted performance score."""
    base_metrics = extract_key_metrics(log['readings'])
    
    # Distractor: unused transformed data
    _ = transform_data(log['readings'])
    
    # Intermediate irrelevant computation
    temp_diag = [analyze_component(x) for x in log['readings'] if x < 60]
    
    # Real computation begins
    score = 0.0
    if base_metrics['peak'] > 95:
        score += 20
    if base_metrics['average'] > 70:
        score += 30
    
    # Use of enumerate and zip (required)
    adjustments = [0.8, 1.1, 1.3]
    categories = ['peak', 'average', 'anomalies']
    for i, cat in enumerate(categories):
        if cat in weight_map:
            # Only 'peak' and 'average' are actually weighted
            if cat in base_metrics:
                adjustment_factor = adjustments[i] if i < len(adjustments) else 1.0
                score += base_metrics[cat] * weight_map[cat] * adjustment_factor
    
    # Additional distractor: recursive call with dead logic
    def decay_factor(n):
        if n <= 1:
            return n
        return decay_factor(n - 2) + 0.5
    
    _ = decay_factor(7)  # Unused result
    
    # Final irrelevant dictionary operation
    diagnostics = {f'entry_{i}': val for i, val in enumerate(temp_diag)}
    summary = dict(zip(categories, [base_metrics[c] for c in categories]))
    
    return score

# Main execution block
if __name__ == '__main__':
    # Simulated system metrics log
    metrics_log = {
        'timestamp': 1712345678,
        'readings': [88, 76, 92, 64, 96, 81, 94, 68],  # 8 values
        'sensor_id': 'SNSR-ALPHA-7',
        'location': 'Server Room B'
    }
    
    # Weight configuration (only peak and average matter)
    weights = {'peak': 0.6, 'average': 0.4, 'dummy_key': 0.0}  # dummy_key unused
    
    # Irrelevant pre-processing
    raw_signals = [x * 1.1 for x in metrics_log['readings'] if x % 2 == 0]
    _ = accumulate_signals(raw_signals)
    
    # Key statement
    final_score = evaluate_performance(metrics_log, weights)
    
    # Output result
    print(f"Result: {final_score}")