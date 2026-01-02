def analyze_performance(metrics):
    baseline = sum(m * 0.8 for m in metrics if m > 50)
    adjusted = [m * 1.2 for m in metrics if m < 75]
    return baseline, len(adjusted)

metrics_data = [65, 40, 80, 30, 90, 70, 25]

# Irrelevant transformation chain
temp_scores = list(map(lambda x: x ** 0.5 * 2.5, metrics_data))
filtered_scores = [s for s in temp_scores if s > 10]
score_offset = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0

# Distractor: unused performance counters
high_perf_count = 0
for i, val in enumerate(metrics_data):
    if val > 70:
        high_perf_count += 1

# Real computation begins: system unit analysis
units = [(1, 'A', 200), (2, 'B', 150), (3, 'C', 300), (4, 'D', 100)]
available_types = ['A', 'B', 'C']

def calculate_unit_contribution(u):
    _, t, base = u
    factor = 1.0
    if t == 'A':
        factor = 1.2
    elif t == 'B':
        factor = 0.9
    elif t == 'C':
        factor = 1.1
    return base * factor

def calculate_system_capacity(unit_list):
    total = 0.0
    bonuses = {t: 0 for t in available_types}
    
    for idx, (uid, utype, cap) in enumerate(unit_list):
        if utype not in available_types:
            continue
        
        # Secondary filtering based on index parity (semi-relevant)
        index_bonus = 1.1 if idx % 2 == 0 else 1.0
        
        # Calculate base contribution with type factor
        contrib = calculate_unit_contribution((uid, utype, cap))
        
        # Apply index-based bonus
        total += contrib * index_bonus
        
        # Track per-type bonus (not used later, minor distraction)
        bonuses[utype] += contrib * 0.05
    
    # Distractor: unused sorted list
    sorted_units = sorted(unit_list, key=lambda x: x[2], reverse=True)
    stability_factor = 0.98 ** len([u for u in sorted_units if u[2] > 150])
    
    # Final adjustment based on metric correlation
    metric_sum = sum(m for m in metrics_data if m > 60)
    calibration = metric_sum / 100.0
    
    # Actual final capacity
    final = total * (calibration / 15.0)
    
    # Dead code: irrelevant logging
    log_entry = f"Processed {len(unit_list)} units with calibration {calibration:.2f}"
    
    return int(final)

# Execution point of interest
baseline_perf, active_count = analyze_performance(metrics_data)
calibration_shift = max(metrics_data) - min(metrics_data)

# Key statement
final_capacity = calculate_system_capacity(units)

print(f"Result: {final_capacity}")