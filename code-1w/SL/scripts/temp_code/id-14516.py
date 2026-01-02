def analyze_telemetry(data_log):
    base_factor = 1.5
    adjustment = 0.8
    temp_result = 0
    
    for entry in data_log:
        raw_value = entry['value']
        status_flag = entry['flag']
        
        if status_flag == 'ACTIVE':
            temp_result += raw_value * base_factor
        elif status_flag == 'STANDBY':
            temp_result += raw_value * adjustment
        else:
            temp_result -= raw_value * 0.1

    return int(temp_result)


def apply_correction(value, mode='standard'):
    if mode == 'standard':
        return (value + 10) % 7
    else:
        return (value - 5) * 2


def evaluate_performance(metrics, limit):
    score = 0
    penalty_offset = 3
    bonus_tracker = []
    
    corrected_limit = apply_correction(limit)
    
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            adjusted_val = val * (1.1 if val > corrected_limit else 0.9)
            score += int(adjusted_val)
            
            intermediate_check = (val ^ i) & 3  # bitwise analysis (semi-relevant)
            if intermediate_check == 0:
                bonus_tracker.append(val)
        else:
            # Misleading complex expression with no impact
            shadow_calc = (val * 0.5 + 2.1) ** 1.1
            noise_floor = shadow_calc - int(shadow_calc)
            if noise_floor > 0.5:
                pass  # dead code branch

    # Final adjustment using bonus tracker but only if conditions met
    if len(bonus_tracker) >= 2 and sum(bonus_tracker) > 100:
        score += 5
    
    # Irrelevant state tracking
    audit_log = [{'step': i, 'valid': True} for i in range(len(metrics))]
    
    return score

# Main execution
raw_entries = [
    {'value': 12, 'flag': 'ACTIVE'},
    {'value': 8, 'flag': 'STANDBY'},
    {'value': 15, 'flag': 'ACTIVE'},
    {'value': 6, 'flag': 'INACTIVE'},
    {'value': 20, 'flag': 'ACTIVE'}
]

processed_values = [x*3 for x in [2, 5, 7, 11, 13]]  # transformed primes
threshold = 17

# Unused distraction variables
baseline_model = {'alpha': 0.95, 'beta': 1.05}
calibration_matrix = [[i*j for j in range(3)] for i in range(3)]

initial_sum = analyze_telemetry(raw_entries)
evaluation_metrics = [processed_values[i] + (initial_sum % 10) for i in range(5)]

final_score = evaluate_performance(evaluation_metrics, threshold)

print(f"Target result: {final_score}")