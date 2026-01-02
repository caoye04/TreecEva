def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0

    for day, data in logs.items():
        if 'hours_worked' in data:
            total_hours += data['hours_worked']
            if data['hours_worked'] < 6:
                idle_periods += 1

    if total_hours > 0:
        efficiency_ratio = (total_hours - idle_periods * 2) / total_hours

    return total_hours, efficiency_ratio, idle_periods


def validate_inputs(contributions, thresholds):
    # Irrelevant validation checks with side computations
    anomalies = []
    temp_sum = 0
    for k, v in contributions.items():
        temp_sum += len(k)
        if v < thresholds.get('min_contrib', 0):
            anomalies.append(k)
    scale_factor = temp_sum % 7 if temp_sum > 0 else 1
    return len(anomalies) == 0


def calculate_rating(contributions, penalty_factor):
    base_score = 0
    bonus_tracker = {}
    debug_values = []

    # Real logic mixed with distractions
    for key, value in contributions.items():
        capped_value = min(value, 50)
        if 'feat' in key:
            base_score += capped_value * 1.2
        elif 'bugfix' in key:
            base_score += capped_value * 1.5
            if value > 40:
                bonus_tracker[key] = value * 0.1
        else:
            base_score += capped_value * 0.8

    # Distractor: complex string operations not affecting score
    label = ''.join([k[0] for k in contributions.keys() if k.startswith('feat')])
    checksum = sum(ord(c) for c in label) % 11

    # Actual penalty application
    adjusted_score = base_score * (1 - penalty_factor)

    # More distraction: unused dictionary aggregation
    stats_summary = {
        'entries': len(contributions),
        'checksum_debug': checksum,
        'bonus_count': len(bonus_tracker)
    }

    # Final transformation using modular arithmetic
    final_score = int((adjusted_score + 5) % 97)
    
    return final_score

# Main execution
if __name__ == '__main__':
    activity_logs = {
        'day1': {'hours_worked': 8, 'tasks': ['feat-ui', 'bugfix-login']},
        'day2': {'hours_worked': 4, 'tasks': ['docs-update']},
        'day3': {'hours_worked': 7, 'tasks': ['feat-api', 'perf-opt']}
    }

    # Extract some values (some used, some not)
    hours, efficiency, idle_days = analyze_productivity(activity_logs)
    
    contributions = {
        'feat-auth': 60,
        'bugfix-session': 45,
        'feat-payment': 55,
        'refactor-db': 30,
        'bugfix-ui': 20
    }
    
    config_thresholds = {
        'min_contrib': 10,
        'max_penalty': 0.3
    }
    
    # Validate inputs — result not used but adds interference
    is_valid = validate_inputs(contributions, config_thresholds)
    
    # Noise computation
    shadow_score = 0
    for val in contributions.values():
        shadow_score += (val ** 2) // 100
    
    penalty_factor = 0.15 if efficiency < 0.8 else 0.1
    
    final_score = calculate_rating(contributions, penalty_factor)
    
    print(f"Result: {final_score}")