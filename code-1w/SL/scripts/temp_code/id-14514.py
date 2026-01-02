def analyze_metrics(data):
    base = sum(data) // len(data) if data else 0
    offset = max(data) - min(data) if len(data) > 1 else 0
    
    # Distractor: irrelevant transformation
    temp_map = {i: (val ** 2) % 17 for i, val in enumerate(data)}
    magic_factor = 0
    for k, v in temp_map.items():
        if k % 3 == 0 and v > 10:
            magic_factor += v

    # Semi-relevant adjustment
    adjustment = len([x for x in data if x > base]) * 0.5
    return base + adjustment


def validate_entry(record):
    # String processing distraction
    status = record.get('status', '').strip().lower()
    is_valid = status in ['active', 'verified'] and record.get('enabled', False)
    
    # Dead computation path (no effect on output)
    if 'meta' in record:
        checksum = sum(ord(c) for c in str(record['meta'])) % 100
        _ = [checksum * i for i in range(3)]  # unused list

    confidence = 1 if is_valid else -1
    return confidence

# Main data
benchmark_data = [12, 15, 10, 8, 20, 13]

# Irrelevant preprocessing
shadow_copy = [x + 2 for x in benchmark_data]
shadow_copy = [x for x in shadow_copy if x % 2 == 0]

# State tracking with partial relevance
consistency_flags = []
for i in range(len(benchmark_data)):
    if i > 0 and benchmark_data[i] >= benchmark_data[i-1]:
        consistency_flags.append(True)
    else:
        consistency_flags.append(False)

# Mock validation records (only one used)
validation_pool = [
    {'status': ' Active ', 'enabled': True},
    {'status': 'inactive', 'enabled': False, 'meta': 'xyz'},
    {'status': 'verified', 'enabled': True, 'meta': 'abc'}
]

primary_confidence = validate_entry(validation_pool[0])

# Core calculation chain
base_metric = analyze_metrics(benchmark_data)

# Conditional expression usage
scaling_factor = 2.5 if all(consistency_flags[i] for i in range(-3, 0)) else 1.8

# Composite score with string-based switch
mode_flag = 'high' if sum(benchmark_data) > 50 else 'low'
boost = 7 if mode_flag.startswith('h') else 0

# Final performance calculation
final_score = int(base_metric * scaling_factor + boost * primary_confidence)

# Output required format
print(f"Result: {final_score}")