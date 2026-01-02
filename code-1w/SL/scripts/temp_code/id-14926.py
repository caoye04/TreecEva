def process_timestamps(log_entries):
    # Irrelevant helper function – dead code path
    return [entry.split('.')[0] for entry in log_entries if 'DEBUG' not in entry]

# Misleading data structures
temp_cache = {f'key_{i}': i * 1.5 for i in range(100)}
lookup_table = {i: (i ** 2) % 17 for i in range(20)}

# Distractor variables
buffer_size = 1024
retry_limit = 3
error_threshold = 0.05

# Real configuration
benchmark_config = {
    'baseline': 72.5,
    'weight_a': 0.6,
    'weight_b': 0.4,
    'penalty_factor': 1.2,
    'enable_adjustment': True
}

# Simulated metrics log with embedded patterns
raw_logs = [
    '2024-05-01 10:00:01.001 INFO throughput=120 latency=45 status=OK',
    '2024-05-01 10:05:22.017 WARN throughput=95 latency=60 status=DEGRADED',
    '2024-05-01 10:10:43.044 INFO throughput=135 latency=38 status=OK',
    '2024-05-01 10:15:19.091 ERR throughput=70 latency=80 status=FAILED'
]

metrics_log = []
for log in raw_logs:
    parts = log.split(' ')
    if len(parts) < 5:
        continue
    info_str = parts[-1]
    status = info_str.split('=')[1]
    perf_data = parts[-2].split('=')
    metric_type = perf_data[0]
    metric_val = int(perf_data[1])
    
    entry = {'timestamp': parts[0] + ' ' + parts[1], 'status': status}
    
    # Extract relevant metrics using string slicing and conditions
    if metric_type == 'throughput':
        entry['throughput'] = metric_val
        # Add derived score from lookup table (uses dictionary)
        entry['bonus'] = lookup_table.get(metric_val % 20, 0)
    elif metric_type == 'latency':
        entry['latency'] = metric_val
        entry['penalty'] = 1 if metric_val > 75 else 0
    
    metrics_log.append(entry)

# Another decoy function
def validate_checksum(data):
    return sum(ord(c) for c in str(data)) % 256

# Data transformation phase
transformed = []
for item in metrics_log:
    new_item = dict(item)
    if 'throughput' in new_item:
        new_item['normalized_tput'] = round(new_item['throughput'] / benchmark_config['baseline'], 3)
    if 'latency' in new_item:
        new_item['efficiency'] = max(0, (100 - new_item['latency']) / 100)
    transformed.append(new_item)

# Real processing begins here
aggregated = {'valid_count': 0, 'total_score': 0, 'penalty_sum': 0}

for record in transformed:
    if 'throughput' not in record or 'latency' not in record:
        continue
    
    # Scoring logic
    base_score = (record['normalized_tput'] * benchmark_config['weight_a'] + 
                  record['efficiency'] * benchmark_config['weight_b']) * 100
    
    if record.get('penalty', 0) == 1:
        base_score *= 0.8  # 20% penalty
    
    # Bonus application only if status is OK and bonus > 5
    if record['status'] == 'OK' and record.get('bonus', 0) > 5:
        base_score += record['bonus']
    
    aggregated['total_score'] += base_score
    aggregated['valid_count'] += 1
    aggregated['penalty_sum'] += record.get('penalty', 0)

# Final evaluation function
def evaluate_performance(log, config):
    if not log or aggregated['valid_count'] == 0:
        return 0.0
    
    avg_score = aggregated['total_score'] / aggregated['valid_count']
    penalty_correction = aggregated['penalty_sum'] * config['penalty_factor']
    
    # Apply adjustment if enabled
    if config['enable_adjustment']:
        adjustment = (avg_score * 0.05) if avg_score > 80 else (-avg_score * 0.03)
        avg_score += adjustment
    
    return round(avg_score - penalty_correction, 4)

# Critical statement
final_score = evaluate_performance(metrics_log, benchmark_config)

# Output result
print(f"Target result: {final_score}")