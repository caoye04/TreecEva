from collections import defaultdict

# Simulate system performance metrics over time
def analyze_system_metrics(log_entries):
    efficiency = 0
    errors = 0
    temp_buffer = []
    state_tracker = defaultdict(int)
    total_entries = len(log_entries)
    
    for entry in log_entries:
        # Extract operation type and outcome
        parts = entry.strip().split(' ')
        op_type = parts[0]
        status = parts[-1]
        
        # Track various states (some are red herrings)
        state_tracker[op_type] += 1
        if 'read' in op_type:
            state_tracker['reads_processed'] += 1
        elif 'write' in op_type:
            state_tracker['writes_attempted'] += 1

        # Relevant logic: compute efficiency from successful ops
        if status == 'OK':
            efficiency += 1
        else:
            errors += 1
            temp_buffer.append(entry)  # Dead-end storage

        # Distractor computation: irrelevant average
        fake_metric = sum([len(p) for p in parts]) / len(parts)
        adjustment = fake_metric * 0.1
        efficiency -= int(adjustment) if adjustment > 1 else 0

    # More distraction: unused nested loop
    validation_check = 0
    for i in range(2):
        for j in range(3):
            validation_check += i * j
    # Result unused

    # Semi-relevant transformation
    normalized_errors = max(errors, 1)
    efficiency_ratio = efficiency / total_entries
    
    # Final evaluation function
    def evaluate_performance(eff, err):
        base = eff * 10
        penalty = (err ** 2) * 5
        bonus = 10 if eff > err * 2 else 0
        return base - penalty + bonus
    
    final_score = evaluate_performance(efficiency, errors)
    
    # Extra unrelated string processing (slicing and methods)
    summary_log = ''.join(log_entries)[:50].upper().replace(' ', '_')
    checksum = sum(ord(c) for c in summary_log) % 100
    
    # Output only the required result
    print(f"Result: {final_score}")
    return final_score

# Input data
logs = [
    "read_cache OK", "write_disk FAIL", "read_cache OK", "network_tx OK",
    "read_cache FAIL", "read_cache OK", "write_disk OK", "network_tx FAIL",
    "read_cache OK", "read_cache OK"
]

analyze_system_metrics(logs)