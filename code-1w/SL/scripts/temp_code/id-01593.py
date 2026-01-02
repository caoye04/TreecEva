def analyze_readings(readings):
    total = 0
    count = 0
    for r in readings:
        if r < 0:
            continue
        total += r
        count += 1
    return total / count if count > 0 else 0

readings_log = [12, -3, 15, 8, -1, 20, 0, 11]

# Distractor: irrelevant statistics
avg_temp = sum(readings_log) / len(readings_log)
stdev_temp = (sum((x - avg_temp) ** 2 for x in readings_log) / len(readings_log)) ** 0.5

status_codes = {1: 'OK', 0: 'ERROR'}

# Simulate processing stages
processing_stages = ['init', 'validate', 'transform', 'finalize']
stage_weights = {'init': 0.1, 'validate': 0.3, 'transform': 0.4, 'finalize': 0.2}

weighted_progress = 0
for stage in processing_stages:
    if stage == 'validate':
        weighted_progress += stage_weights[stage] * 1.0
    elif stage == 'transform':
        weighted_progress += stage_weights[stage] * 0.8
    else:
        weighted_progress += stage_weights[stage] * 0.9

# Core data used in final calculation
process_data = {
    'input_count': len(readings_log),
    'valid_average': analyze_readings(readings_log),
    'stages_completed': len(processing_stages),
    'progress_weight': weighted_progress
}

# Misleading function that looks important but isn't used
def predict_failure(data):
    return len(data) % 7 == 0

# Auxiliary computation - partially relevant
baseline = 10.0
drift_adjustment = abs(avg_temp - baseline) * 0.1

# Real efficiency formula
def calculate_efficiency(data):
    base_efficiency = data['valid_average'] * data['stages_completed']
    penalty = 0
    if data['progress_weight'] < 0.85:
        penalty = 5
    # Bonus for high input volume
    bonus = 10 if data['input_count'] > 6 else 0
    return base_efficiency - penalty + bonus

# Critical execution point
intermediate_flag = predict_failure(readings_log)
efficiency_score = calculate_efficiency(process_data)

# Distractor: unused transformation tree
transformation_tree = {
    'level1': {'nodes': 2, 'active': True},
    'level2': {'nodes': 4, 'active': False},
    'level3': {'nodes': 8, 'active': True}
}
total_active_nodes = sum(
    v['nodes'] for v in transformation_tree.values() if v['active']
)

# Final output
print(f"Result: {efficiency_score}")