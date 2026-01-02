import itertools

def analyze_workflow(data_points):
    # Irrelevant preprocessing step (distractor)
    filtered_data = [x for x in data_points if x > 0]
    temp_accum = sum(x ** 0.5 for x in filtered_data if x % 2 == 0)
    normalized = [round(x / (temp_accum + 1e-5), 3) for x in filtered_data]
    return normalized

def track_metrics(logs):
    # Another semi-relevant function with dead-end computation
    event_count = {}
    for log in logs:
        key = log.split(':')[0]
        event_count[key] = event_count.get(key, 0) + 1
    
    # Dead code path (never used later)
    redundant_analysis = {k: v * 1.5 for k, v in event_count.items() if 'ERR' in k}
    return len(logs)

def evaluate_performance(hours_worked, bugs_found, cpu_efficiency):
    base_score = 100
    penalty = 0
    
    # Real logic begins here
    if hours_worked < 40:
        penalty += 15
    elif hours_worked > 60:
        overtime_factor = min(hours_worked - 60, 20)
        penalty += overtime_factor * 0.8

    # Bug penalty with threshold logic
    if bugs_found > 5:
        penalty += (bugs_found - 5) * 3
    
    # Efficiency boost using bitwise and comparison
    if cpu_efficiency > 0.85:
        bonus_bits = int(cpu_efficiency * 100) & 15  # Use lower 4 bits
        base_score += bonus_bits
    else:
        base_score -= 10

    # Use set operations to filter irrelevant categories
    performance_tiers = {'excellent', 'good', 'fair', 'poor'}
    current_tier = 'good'
    adjustment_set = {'excellent', 'good'}
    if current_tier in adjustment_set:
        base_score += 5

    # String method distractor (no effect on result)
    status_label = "Performance_Review_Done".replace('_', '').lower()
    status_flag = len(status_label) % 7

    # Critical calculation
    final_score = base_score - penalty
    
    # Additional irrelevant transformation
    encoded_score = ''.join(itertools.chain(*zip(str(final_score), '*')))
    
    return int(final_score)

# Main execution block
productivity = 52
errors = 8
efficiency = 0.92

# Call auxiliary functions with side effects that don't impact final_score
raw_logs = ["INFO:startup", "ERR:disk", "INFO:compute", "ERR:network", "INFO:cleanup"]
data_stream = [16, 25, 36, 49, 64]
analyze_workflow(data_stream)
track_metrics(raw_logs)

# Key statement
final_score = evaluate_performance(productivity, errors, efficiency)

print(f"Result: {final_score}")