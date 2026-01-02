from collections import defaultdict

# Simulate a system diagnostic tool that analyzes resource usage over time

def collect_metrics(data_points):
    readings = defaultdict(list)
    temp_cache = []
    total_entries = 0

    for entry in data_points:
        timestamp, resource, value = entry
        readings[resource].append(value)
        temp_cache.append(value * 0.95)  # Simulated normalized cache (not used later)
        total_entries += 1

    # Irrelevant transformation
    scaled_cache = [x ** 0.5 for x in temp_cache if x > 50]
    average_load = sum(temp_cache) / len(temp_cache) if temp_cache else 0

    return readings, average_load

def compute_fragments(readings):
    fragments = {}
    noise_floor = 10
    for resource, values in readings.items():
        filtered = [v for v in values if v > noise_floor]
        if filtered:
            fragment_score = (max(filtered) - min(filtered)) * len(filtered)
            fragments[resource] = fragment_score
        else:
            fragments[resource] = 0
    
    # Dummy computation
    aggregate_noise = sum([len(seq) for seq in readings.values()]) * 0.1
    return fragments, aggregate_noise

def evaluate_stress_pattern(fragments):
    stress_levels = {}
    baseline = 100
    adjustment_factor = 0.85

    for res, score in fragments.items():
        if score > baseline:
            level = "HIGH"
        elif score > baseline * 0.5:
            level = "MODERATE"
        else:
            level = "LOW"
        stress_levels[res] = (level, score * adjustment_factor)
    
    # Red herring variable
    max_theoretical_score = max([s[1] for s in stress_levels.values()], default=0)
    return stress_levels

def system_diagnostic(log_input):
    # Step 1: Collect raw metrics
    metric_map, avg_load = collect_metrics(log_input)
    
    # Step 2: Compute variation fragments
    frag_scores, noise_metric = compute_fragments(metric_map)
    
    # Step 3: Evaluate stress patterns
    stress_profile = evaluate_stress_pattern(frag_scores)
    
    # Step 4: Determine peak capacity based on CPU and memory stress
    cpu_score = frag_scores.get('CPU', 0)
    mem_score = frag_scores.get('MEMORY', 0)
    io_score = frag_scores.get('IO', 0)  # Not directly used
    
    # Secondary distraction
    avg_stress = sum([s[1] for s in stress_profile.values()]) / len(stress_profile) if stress_profile else 0
    
    # Core logic: peak capacity is derived from CPU and memory interaction
    if cpu_score > 200 and mem_score > 150:
        base_capacity = 850
    elif cpu_score > 100 or mem_score > 100:
        base_capacity = 620
    else:
        base_capacity = 300
    
    # Adjustment based on combined factor
    multiplier = 1.1 if cpu_score + mem_score > 400 else 1.0
    adjusted_capacity = base_capacity * multiplier
    
    # Final safety cap
    peak_capacity = min(adjusted_capacity, 900)
    
    # Dead code branch (never executed due to logic above)
    if peak_capacity > 2000:
        peak_capacity = 2000 + (peak_capacity - 2000) // 100
    
    # Output target result
    print(f"Result: {peak_capacity}")
    return locals()

data_log = [
    (1001, 'CPU', 120),
    (1002, 'MEMORY', 95),
    (1003, 'CPU', 210),
    (1004, 'MEMORY', 160),
    (1005, 'IO', 80),
    (1006, 'CPU', 180),
    (1007, 'MEMORY', 140),
    (1008, 'IO', 200)
]

final_analysis = system_diagnostic(data_log)
