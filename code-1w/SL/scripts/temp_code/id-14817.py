def analyze_system_throughput(inputs, thresholds):
    # Simulate multi-stage signal processing with filtering and amplification
    amplified = [x * 1.75 for x in inputs if x > thresholds[0]]
    filtered = [x for x in amplified if abs(x) % 2 == 1]

    # Misleading intermediate calculations (distractors)
    temp_buffer = []
    running_total = 0
    for val in filtered:
        running_total += val
        temp_buffer.append(running_total * 0.1)  # Not used later

    # Secondary path: statistical summary (semi-relevant)
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    deviation = [abs(f - avg_val) for f in filtered]
    consistency_score = sum(1 for d in deviation if d < 10)

    # Core transformation: prepare flow metrics for recursive analysis
    flow_metrics = [int(f // 3) for f in filtered]
    
    # Irrelevant noise: simulate logging overhead
    log_entries = []
    for i, f in enumerate(flow_metrics):
        log_entries.append(f"Entry_{i}: {f}")
    
    # Key recursive function using lambda-assisted decomposition
    split_and_combine = lambda arr: (arr[:len(arr)//2], arr[len(arr)//2:])

    def calculate_equilibrium(data, start, end):
        if end - start <= 1:
            return data[start] if start < len(data) else 0
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        left_part, right_part = split_and_combine(data[start:end])
        
        # Recursive equilibrium from both halves
        left_eq = calculate_equilibrium(left_part, 0, len(left_part))
        right_eq = calculate_equilibrium(right_part, 0, len(right_part))
        
        # Equilibrium defined as difference amplified by segment length ratio
        length_factor = (len(left_part) / len(right_part)) if len(right_part) > 0 else 1
        return int(abs(left_eq - right_eq) * length_factor)

    # Additional red herring: unused dynamic weighting
    weights = [0.5 ** i for i in range(len(flow_metrics))]
    weighted_sum = sum(w * f for w, f in zip(weights, flow_metrics))

    equilibrium_score = calculate_equilibrium(flow_metrics, 0, len(flow_metrics))
    
    # Final irrelevant transformation
    final_diagnostic = f"System stable: {equilibrium_score < 50}"
    
    print(f"Result: {equilibrium_score}")

# Inputs based on sensor array readings
data_inputs = [12, 15, 9, 22, 18, 31, 42, 17]
thresholds_config = [10, 25, 8]

analyze_system_throughput(data_inputs, thresholds_config)