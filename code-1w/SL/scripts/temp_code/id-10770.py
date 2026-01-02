import math

# Simulated system log with diagnostic codes and signal strengths
def generate_system_log():
    raw_signals = [2.3, 4.1, 0.9, 5.5, 3.2, 1.8, 6.7, 2.9]
    processed = [(i, round(math.log(s ** 1.5 + 1), 3)) for i, s in enumerate(raw_signals)]
    labels = ['ERR', 'OK', 'WARN', 'OK', 'ERR', 'WARN', 'OK', 'OK']
    return [(idx, val, lbl) for (idx, val), lbl in zip(processed, labels)]

def extract_critical_indices(log):
    # Irrelevant filtering - only collects OK statuses but not used in final path
    return [idx for idx, val, lbl in log if lbl == 'OK']

def compute_entropy(values):
    # Dead function: computes entropy but unused in main logic
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def filter_anomalies(log_entry_list):
    # Misleading preprocessing: removes low values but not actually used
    filtered = [entry for entry in log_entry_list if entry[1] > 2.0]
    temp_result = [e for e in filtered if e[2] != 'ERR']
    return temp_result

def rolling_window_avg(data, window=3):
    # Distractor: calculates moving average but not used in critical path
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        averages.append(round(avg, 3))
    return averages

def evaluate_stability_index(log):
    # Semi-relevant transformation - used to distract from actual calculation
    indices = [i for i, _, _ in log]
    values = [v for _, v, _ in log]
    stability = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            stability += 0.1
        else:
            stability -= 0.05
    return round(stability, 3)

def aggregate_diagnostics(log):
    # Key distractor: looks important but output not used
    stats = {
        'total': len(log),
        'errors': len([1 for _, _, lbl in log if lbl == 'ERR']),
        'warnings': len([1 for _, _, lbl in log if lbl == 'WARN'])
    }
    stats['ratio'] = round(stats['errors'] / stats['total'], 3)
    return stats

def analyze_metrics(log, threshold):
    # Core relevant logic buried among distractions
    
    # Step 1: Extract numeric values
    values = [val for _, val, _ in log]
    
    # Step 2: Apply nonlinear transformation
    transformed = [math.sin(v * 0.5) ** 2 for v in values]
    
    # Step 3: Weight by position index
    weighted = [w * (i + 1) for i, w in enumerate(transformed)]
    
    # Step 4: Compute cumulative interference score
    interference_score = 0
    for i, w in enumerate(weighted):
        if i % 2 == 0:
            interference_score += w * 0.7
        else:
            interference_score -= w * 0.3
    
    # Step 5: Normalize using hyperbolic tangent
    normalized_score = math.tanh(abs(interference_score))
    
    # Step 6: Compare against threshold and encode as integer
    diagnostic_flag = 1 if normalized_score >= threshold else 0
    
    # Step 7: Combine with checksum of original indices
    indices = [idx for idx, _, _ in log]
    checksum = sum(indices[i] * (i + 1) for i in range(len(indices))) % 100
    
    # Step 8: Final diagnostic is weighted combination
    final_value = int(normalized_score * 1000) + checksum * diagnostic_flag
    
    # Critical red herring: unused intermediate that looks essential
    anomaly_cluster = [v for v in values if v > 3.0]
    cluster_entropy = compute_entropy(anomaly_cluster) if anomaly_cluster else 0
    
    return final_value

# Main execution flow
system_log = generate_system_log()

# Irrelevant data transformations
unused_indices = extract_critical_indices(system_log)
anomaly_free_log = filter_anomalies(system_log)
raw_values_only = [val for _, val, _ in system_log]
moving_avgs = rolling_window_avg(raw_values_only)
stability_metric = evaluate_stability_index(system_log)
diag_stats = aggregate_diagnostics(system_log)

# Key statement containing the answer
final_diagnostic = analyze_metrics(system_log, threshold=0.85)

# Print result
print(f"Result: {final_diagnostic}")