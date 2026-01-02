def analyze_workload_efficiency(base_load, scaling_factor, thresholds):
    # Simulate multi-phase system workload with efficiency adjustments
    phases = ['initial', 'rampup', 'peak', 'decline', 'final']
    phase_duration = {p: (i + 1) * 2 for i, p in enumerate(phases)}
    
    # Irrelevant metric - distractor
    theoretical_max = sum([len(p) * 10 for p in phases])
    
    # Generate time-series load profile using combinatorial expansion
    timeline = []
    for phase, duration in phase_duration.items():
        intensity = base_load
        if 'ramp' in phase:
            intensity *= scaling_factor
        elif 'peak' in phase:
            intensity *= (scaling_factor ** 2)
        elif 'decline' in phase:
            intensity *= (scaling_factor * 0.6)
        timeline.extend([intensity] * duration)
    
    # Apply conditional dampening based on threshold crossings (real logic)
    dampened_load = []
    spike_count = 0
    for val in timeline:
        adjusted = val * 0.9
        if val > thresholds['critical']:
            spike_count += 1
            adjusted *= 0.75  # Load shedding
        dampened_load.append(round(adjusted, 2))
    
    # Secondary transformation via list comprehension - relevant
    stabilized_load = [x + 5 for x in dampened_load if x < thresholds['warning']]
    
    # Use of zip and enumerate: align phases with load segments (mostly irrelevant)
    segment_map = {}
    start = 0
    for i, (phase, duration) in enumerate(phase_duration.items()):
        end = start + duration
        segment_map[phase] = dampened_load[start:end]
        start = end
    
    # Compute usage projection with moving average smoothing (key computation)
    window_size = 3
    smoothed = []
    for i in range(len(dampened_load) - window_size + 1):
        window_avg = sum(dampened_load[i:i+window_size]) / window_size
        smoothed.append(round(window_avg, 2))
    
    # Final projection includes stabilization offset
    usage_projection = [val + len(stabilized_load) * 0.01 for val in smoothed]
    
    # Dead code path - misleading control flow
    if len(usage_projection) == 0:
        fallback = [base_load * scaling_factor]
        usage_projection = [x * 0.5 for x in fallback]
    
    # Critical execution point
    peak_capacity = max(usage_projection)
    
    # Unused helper - distractor
    def calculate_headroom(capacity, reserve_margin=0.2):
        return capacity * (1 - reserve_margin)
    
    # Print result as required
    print(f"Result: {peak_capacity}")
    return peak_capacity

# Inputs
base_load = 40
scaling_factor = 2.5
thresholds = {'warning': 75, 'critical': 90}

# Execute
analyze_workload_efficiency(base_load, scaling_factor, thresholds)