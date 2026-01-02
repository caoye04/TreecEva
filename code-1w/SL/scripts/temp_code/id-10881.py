def analyze_system_load(base_threshold, input_stream):
    temp_buffer = [x ^ 2 for x in input_stream if x % 3 == 0]
    temp_buffer = [x for x in temp_buffer if x > base_threshold]

    # Irrelevant signal processing branch (dead path)
    if len(temp_buffer) > 100:
        moving_avg = sum(temp_buffer[-5:]) / 5
        normalized = [val / moving_avg for val in temp_buffer]
    else:
        normalized = temp_buffer.copy()

    # Distractor: complex but unused transformation chain
    transform_key = lambda a: (a << 2) ^ 15
    encrypted_stream = list(map(transform_key, input_stream))
    checksum = sum(encrypted_stream) % 1000

    # Real computation begins — masked by prior noise
    critical_values = [x for x in input_stream if x & 1]  # filter odd numbers
    filtered_set = set(critical_values)

    metric_set = set()
    for val in filtered_set:
        if val % 5 == 0:
            metric_set.add(val)
        elif val % 7 == 0:
            metric_set.discard(val - 1)  # harmless but misleading

    # Secondary red herring: unused recursive function
    def compute_depth(n):
        return 1 + compute_depth(n // 2) if n > 1 else 1

    size_factor = len(metric_set) * 17
    sum_factor = sum(metric_set) // max(len(metric_set), 1)

    adjustment = 0
    for i in range(len(input_stream)):
        if i % 4 == 0 and input_stream[i] in filtered_set:
            adjustment += 1

    # Actual answer derivation (well-hidden among distractors)
    def evaluate_performance(metrics):
        base = sum(metrics)
        penalty = len([x for x in metrics if x < 50]) * 5
        bonus = len([x for x in metrics if x > 100]) * 3
        return base - penalty + bonus + size_factor

    final_score = evaluate_performance(metric_set)
    
    # Additional distraction: unused data structure merging
    backup_log = {'size': size_factor, 'check': checksum}
    audit_trail = {**backup_log, 'final': final_score if final_score > 0 else -1}

    # Output required result
    print(f"Result: {final_score}")

# Inputs
input_data = [i * 4 + 1 for i in range(1, 26)]  # generates: 5, 9, 13, ..., 101
input_data.extend([35, 77, 105, 119])  # add some multiples
analyze_system_load(40, input_data)
