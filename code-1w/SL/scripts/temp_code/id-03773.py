def analyze_pattern(sequence):
    if not sequence:
        return 0
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
    return count

# Irrelevant helper function (dead path)
def deprecated_normalization(data):
    return [x / sum(data) for x in data if x > 0]

# Unused but misleading computation
temp_weights = [i**2 for i in range(10)]
weight_sum = sum(temp_weights)  # Distractor variable

baseline = {'threshold': 42, 'tolerance': 0.05}

# Simulated sensor metrics with noise
current_metrics = {
    'throughput': 87.3,
    'latency': 12.8,
    'reliability': 0.987,
    'jitter': 3.4,
    'sequence_pattern': [3, 5, 4, 6, 9, 11, 10],
    'flags': {1, 2, 4, 8},
    'checksum': 255
}

# Decoy transformation chain
transformed = []
for val in current_metrics['sequence_pattern']:
    if val % 2 == 0:
        transformed.append(val << 1)
    else:
        transformed.append(val >> 1)

# Unused set operations (distractor)
expected_flags = {1, 2, 3, 4, 8, 16}
missing_flags = expected_flags - current_metrics['flags']
extra_flags = current_metrics['flags'] - expected_flags
flag_consistency = len(missing_flags) == 0 and len(extra_flags) < 2

# Character analysis red herring
diagnostic_log = "ERR:CHKSUM;WARN:RETRY;INFO:FLOW"
log_parts = diagnostic_log.split(';')
error_count = sum(1 for part in log_parts if part.startswith('ERR'))
warning_count = sum(1 for part in log_parts if part.startswith('WARN'))

# Main evaluation logic disguised among noise
def evaluate_performance(metrics, config):
    score = 0
    
    # Core arithmetic + boolean logic
    if metrics['throughput'] > config['threshold']:
        score += 25
    
    if metrics['latency'] < 15.0:
        score += 20
    
    # Set-based condition (actual use of set operation)
    if 4 in metrics['flags'] and len(metrics['flags']) >= 3:
        score += 15
    
    # Pattern trend analysis (calls external function)
    trend = analyze_pattern(metrics['sequence_pattern'])
    if trend >= 4:
        score += 30
    
    # Final reliability adjustment
    score *= metrics['reliability']
    
    # Jitter penalty only if high jitter and low reliability
    if metrics['jitter'] > 5.0 and metrics['reliability'] < 0.95:
        score -= 10
    
    return int(score)

# Secondary decoy calculation (never used)
shadow_score = 0
for k, v in current_metrics.items():
    if isinstance(v, (int, float)) and k != 'checksum':
        shadow_score += hash(k) % 10

# Key execution point
final_score = evaluate_performance(current_metrics, baseline)

# Output requirement
print(f"Result: {final_score}")