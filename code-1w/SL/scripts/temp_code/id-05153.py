from collections import defaultdict

# Simulate a manufacturing line with multiple stations and quality checks
stations = ['cutting', 'molding', 'assembly', 'packaging']
data_log = [
    {'station': 'cutting', 'output': 230, 'defects': 12, 'downtime': 5},
    {'station': 'molding', 'output': 215, 'defects': 8, 'downtime': 7},
    {'station': 'assembly', 'output': 190, 'defects': 18, 'downtime': 15},
    {'station': 'packaging', 'output': 185, 'defects': 5, 'downtime': 3}
]

# Tracking variables for performance analysis
station_stats = defaultdict(lambda: {'total_output': 0, 'total_defects': 0})
idle_periods = []
consistency_tracker = []

for entry in data_log:
    station = entry['station']
    output = entry['output']
    defects = entry['defects']
    downtime = entry['downtime']
    
    station_stats[station]['total_output'] += output
    station_stats[station]['total_defects'] += defects
    
    # Record idle periods for later analysis (not used in final score)
    if downtime > 5:
        idle_periods.append((station, downtime))
    
    # Track consistency metric (semi-relevant but not critical)
    yield_rate = (output - defects) / output if output > 0 else 0
    consistency_tracker.append(yield_rate)

# Compute aggregate metrics
raw_outputs = [entry['output'] for entry in data_log]
total_output = sum(raw_outputs)
max_defect_station = max(data_log, key=lambda x: x['defects'])['station']

# Simulated cycle time based on average + adjustments (some distraction logic)
avg_cycle_time = 45.0
adjusted_cycle_time = avg_cycle_time * (1 + len(idle_periods) * 0.05)
dynamic_factor = len(consistency_tracker) * 0.1
final_cycle_adjustment = adjusted_cycle_time + dynamic_factor

# Dummy sorting operation to simulate optimization step (irrelevant)
sorted_stations = sorted(stations, key=lambda s: station_stats[s]['total_output'], reverse=True)
baseline_targets = {'target_output': 800, 'threshold_yield': 0.9}

# Key computation chain
projected_capacity = total_output * 1.1  # hypothetical scaling
maintenance_penalty = 0 if total_output > 700 else 0.05
adjusted_capacity = projected_capacity * (1 - maintenance_penalty)

# Critical statement: efficiency score calculation
cycle_time = final_cycle_adjustment
efficiency_score = total_output / (cycle_time * 0.9)

# Irrelevant transformation (dead code path)
optimized_efficiency = efficiency_score * 1.05 if max_defect_station != 'assembly' else efficiency_score

# Final reporting
Result: {efficiency_score}