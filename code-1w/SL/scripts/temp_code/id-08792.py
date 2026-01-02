def process_metrics(entries):
    total = 0
    count = 0
    temp_offset = 0  # unused, distractor
    for entry in entries:
        if 'active' in entry and entry['active']:
            magnitude = entry.get('value', 0) ** 0.5
            adjustment = 1 if magnitude > 3 else -1
            total += magnitude * adjustment
            count += 1
    return total if count > 0 else 0

def validate_integrity(checksums):
    # Irrelevant validation function (dead code path)
    result = 0
    for c in checksums:
        result ^= c
    return result > 50

def calculate_performance(data):
    raw = process_metrics(data)
    baseline = 10
    multiplier = 2.5 if raw > baseline else 1.2
    
    # Complex but partially irrelevant transformation
    shadow_buffer = [x['value'] * 0.1 for x in data if x['value'] < 5]  # not used later
    
    # Conditional expression (required feature)
    penalty = 5 if any(x['value'] < 0 for x in data) else 0
    
    intermediate = (raw * multiplier) - penalty
    
    # Simulate case conversion influence (suggested paradigm)
    mode_flag = 'HIGH' if intermediate > 20 else 'LOW'
    mode_adjust = 3 if mode_flag.lower() == 'high' else 0
    
    final_score = int(intermediate + mode_adjust)
    
    # Additional red herring variables
    debug_log = {'processed': len(data), 'final_raw': raw, 'mode': mode_flag}
    anomaly_count = sum(1 for x in data if x.get('anomaly', False))  # unused
    
    return final_score

# Main execution
benchmark_data = [
    {'value': 4, 'active': True},
    {'value': 9, 'active': True},
    {'value': 2, 'active': False},
    {'value': 16, 'active': True},
    {'value': 1, 'active': True}
]

# Irrelevant pre-computations
checksums = [sum(d['value'] for d in benchmark_data), len(benchmark_data)]
_ = validate_integrity(checksums)  # call with no effect

result_value = calculate_performance(benchmark_data)
final_score = result_value
print(f"Result: {final_score}")