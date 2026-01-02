from collections import defaultdict, Counter

# System resource simulation with monitoring and logging

def simulate_workload(phases):
    # Core tracking structure
    usage_tracker = defaultdict(int)
    
    # Irrelevant auxiliary metrics (distractors)
    latency_log = []
    cache_misses = 0
    retry_count = [0] * len(phases)
    temp_snapshot = set()
    baseline_offset = 17

    # Simulated system events with side effects
    event_flags = {'overload': False, 'throttled': True}
    emergency_buffer = [0 for _ in range(5)]

    for i, workload in enumerate(phases):
        stage_load = 0
        
        # Real computation path: process workload components
        for task in workload:
            if isinstance(task, dict) and 'type' in task and 'size' in task:
                if task['type'] == 'compute':
                    stage_load += task['size'] ** 2
                elif task['type'] == 'io':
                    stage_load += task['size'] * 2
                elif task['type'] == 'network':
                    stage_load += int(task['size'] / 2)

        # Update actual tracker (key logic)
        usage_tracker[f'stage_{i+1}'] = stage_load + (5 if i % 2 == 0 else 0)

        # Distractor: complex but unused recursive function
        def analyze_sparsity(data):
            if not data or sum(data) < 10:
                return 1
            return analyze_sparsity(data[:-1]) + 1

        _ = analyze_sparsity([i*2 for i in range(6)])

        # Dead code path - never executed due to flag state
        if event_flags['overload'] and False:  # Always skipped
            fallback_mode = True
            recovery_step = 0
            while recovery_step < cache_misses:
                recovery_step += 1
            usage_tracker['recovery'] = recovery_step

        # Misleading intermediate calculation
        projected_peak = stage_load * 1.5 + baseline_offset
        temp_snapshot.add(projected_peak)  # Not used later

    # Key statement: determine peak capacity from actual usage
    peak_capacity = max(usage_tracker.values()) if usage_tracker else 0
    
    # Additional red herring computations
    summary_stats = Counter(latency_log)
    final_diagnostic = sum(emergency_buffer) - cache_misses

    # Output the target result
    print(f"Result: {peak_capacity}")
    return peak_capacity

# Input data setup
phases_input = [
    [{'type': 'compute', 'size': 3}, {'type': 'io', 'size': 4}],
    [{'type': 'network', 'size': 8}, {'type': 'compute', 'size': 2}],
    [{'type': 'io', 'size': 5}, {'type': 'compute', 'size': 4}, {'type': 'network', 'size': 6}]
]

# Execute simulation
result = simulate_workload(phases_input)