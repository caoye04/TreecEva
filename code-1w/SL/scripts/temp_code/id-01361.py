def analyze_system_performance(log_entries):
    # Irrelevant counters (distractors)
    total_errors = 0
    retry_count = 0
    timeout_flags = []
    
    # Core data structures
    timestamps = [entry[0] for entry in log_entries]
    cpu_loads = [entry[1] for entry in log_entries]
    temp_readings = [entry[2] for entry in log_entries]
    
    # Misleading transformation (not used in final result)
    normalized_loads = [round((x - min(cpu_loads)) / (max(cpu_loads) - min(cpu_loads)), 3) for x in cpu_loads]
    
    # Real processing path
    thermal_weights = []
    for i, temp in enumerate(temp_readings):
        if temp < 60:
            weight = 1.0
        elif temp < 80:
            weight = 0.75
        elif temp < 90:
            weight = 0.5
        else:
            weight = 0.2  # Severe throttling
        thermal_weights.append(weight)
    
    # Simulate efficiency decay under load and heat
    efficiencies = []
    for i, load in enumerate(cpu_loads):
        base_efficiency = 100 * (1 - (load / 100))
        thermally_adjusted = base_efficiency * thermal_weights[i]
        time_decay = 0.98 ** (i // 5)  # Gradual performance decay over time
        final_eff = thermally_adjusted * time_decay
        efficiencies.append(round(final_eff, 4))
    
    # Dead code path - looks important but unused
    def calculate_health_score():
        return sum(1 for t in temp_readings if t > 75)
    
    # Red herring variables
    avg_cpu = sum(cpu_loads) / len(cpu_loads)
    peak_temp = max(temp_readings)
    stability_index = min(efficiencies) / max(efficiencies)
    
    # Key computation with distractor comments
    # Efficiency peaks are critical for optimization
    peak_efficiency = max(efficiencies)
    
    # Unused tuple unpacking (distractor)
    for idx, (ts, _) in enumerate(zip(timestamps, cpu_loads)):
        if ts % 1000 == 0:
            retry_count += 1  # Rare condition, irrelevant

    # Decoy operation
    _ = [x * 1.1 for x in normalized_loads if x < 0.5]  # No assignment, no effect

    # Final output
    print(f"Result: {peak_efficiency}")
    return peak_efficiency

# Simulated sensor log data (timestamp, cpu%, temperature)
log_data = [
    (1623450000, 45, 58),
    (1623450010, 60, 65),
    (1623450020, 70, 73),
    (1623450030, 75, 79),
    (1623450040, 80, 82),
    (1623450050, 85, 88),
    (1623450060, 90, 91),
    (1623450070, 92, 93),
    (1623450080, 87, 89),
    (1623450090, 83, 85)
]

result = analyze_system_performance(log_data)