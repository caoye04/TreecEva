def analyze_productivity(log_data, efficiency_caps):
    total_hours = sum(log_data.values())
    idle_time = 0.15 * total_hours
    adjusted_hours = total_hours - idle_time

    saturation_levels = {}
    for key in log_data:
        raw_util = log_data[key] / total_hours
        capped_util = min(raw_util, efficiency_caps.get(key, 0.8))
        saturation_levels[key] = round(capped_util, 3)

    bonus_factor = 1.1 if len(log_data) > 3 else 1.0
    penalty = 0.95 if idle_time > 8 else 1.0

    # Irrelevant aggregation
    temp_aggr = 0
    for v in saturation_levels.values():
        temp_aggr += v ** 0.5
    normalized_temp = temp_aggr / len(saturation_levels)

    return adjusted_hours, bonus_factor, penalty, normalized_temp


def evaluate_performance(metrics_log, base_threshold):
    base_points = 0
    tier_multiplier = 1
    decay_rate = 0.95

    # Simulate multi-step scoring with conditional updates
    for day, data in metrics_log.items():
        daily_score = 0
        if data['output'] > base_threshold:
            daily_score += 10
        if data['errors'] < 3:
            daily_score += 5
        if data['response_time'] < 2.0:
            daily_score += 7

        # Apply diminishing returns
        base_points += daily_score * decay_rate
        decay_rate *= 0.98  # compounding decay

        # Track tier progression (semi-relevant)
        if base_points > 50 and tier_multiplier == 1:
            tier_multiplier = 2
            base_points *= 0.9  # adjustment penalty

    final_tier_boost = base_points * (1.2 if tier_multiplier > 1 else 1.0)
    return int(round(final_tier_boost))

# Main execution
worklog = {
    'day1': {'output': 45, 'errors': 2, 'response_time': 1.8},
    'day2': {'output': 38, 'errors': 4, 'response_time': 2.1},
    'day3': {'output': 52, 'errors': 1, 'response_time': 1.5},
    'day4': {'output': 60, 'errors': 5, 'response_time': 2.3},
    'day5': {'output': 48, 'errors': 0, 'response_time': 1.7}
}

config_caps = {'day1': 0.75, 'day3': 0.82, 'day5': 0.78}
threshold_ref = 40

# Auxiliary analysis with side computations
hours_log = {'day1': 7.5, 'day2': 8.0, 'day3': 9.5, 'day4': 6.5, 'day5': 8.5}
_, boost, penalty, norm_temp = analyze_productivity(hours_log, config_caps)

# Key computation chain
interim_adjustment = len(worklog) * 0.85
reference_baseline = sum([v['output'] for v in worklog.values()]) / len(worklog)

final_score = evaluate_performance(worklog, threshold_ref)

# Dead code path - never executed but looks relevant
if __debug__:
    debug_trace = []
    for k in worklog:
        debug_trace.append(f"{k}_processed")

# Print result as required
print(f"Target result: {final_score}")