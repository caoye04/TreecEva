from collections import defaultdict, Counter

# Simulate employee performance analytics with multiple distractions
def analyze_productivity(logs):
    activity_count = defaultdict(int)
    idle_periods = 0
    total_actions = 0

    for entry in logs:
        if entry['status'] == 'active':
            activity_count[entry['task']] += 1
            total_actions += 1
        elif entry['status'] == 'idle':
            idle_periods += 1

    efficiency = total_actions / (total_actions + idle_periods + 1)
    return dict(activity_count), efficiency

def calculate_risk_profile(history):
    # Irrelevant risk calculation (dead-end function)
    risk_factors = Counter()
    for h in history:
        if h['incident']:
            risk_factors[h['type']] += 1
    return sum(risk_factors.values()) * 0.5

def adjust_for_bias(data, bias_factor=1.05):
    # Distractor: looks important but not used in final result
    adjusted = {}
    for k, v in data.items():
        adjusted[k] = v * bias_factor if v > 2 else v * 0.9
    return adjusted

def compute_baseline(performance_map):
    # Another decoy function that calculates something unused
    values = list(performance_map.values())
    if len(values) < 3:
        return sum(values)
    sorted_vals = sorted(values, reverse=True)[:3]
    return sum(sorted_vals) / 3

def process_performance(metrics, adjustments):
    base_metric = sum(metrics.values())
    adjustment_sum = sum(a for a in adjustments if a > 0)
    penalty = sum(a for a in adjustments if a < 0)

    # Misleading intermediate calculation
    shadow_score = base_metric * 0.8 + adjustment_sum ** 0.5

    # Key logic hidden among noise
    raw_score = base_metric + adjustment_sum - abs(penalty)

    # Apply non-linear scaling based on thresholds
    if raw_score < 50:
        scale = 1.2
    elif raw_score < 100:
        scale = 1.0
    else:
        scale = 0.9 + (150 - raw_score) * 0.002  # Diminishing returns

    normalized = raw_score * scale

    # Secondary correction using bit manipulation (obscure but deterministic)
    temp = int(normalized)
    temp = temp ^ 0b1101  # XOR with binary constant
    temp = (temp << 1) | (temp >> 2)  # Shift and combine
    final_score = temp & 0xFFFF  # Mask to 16 bits

    # Red herring: complex structure that isn't used
    audit_trail = {
        'shadow': shadow_score,
        'raw': raw_score,
        'scale_factor': scale,
        'bit_op_input': int(normalized),
        'post_xor': temp ^ 0b1101,
        'post_shift': temp >> 2
    }

    return final_score

# Main execution with fake data
if __name__ == '__main__':
    # Real input data
    user_logs = [
        {'task': 'coding', 'status': 'active'},
        {'task': 'review', 'status': 'active'},
        {'task': None, 'status': 'idle'},
        {'task': 'debug', 'status': 'active'},
        {'task': 'meeting', 'status': 'idle'},
        {'task': 'design', 'status': 'active'},
        {'task': 'testing', 'status': 'active'}
    ]

    # Fake historical data for irrelevant function
    incident_history = [
        {'incident': True, 'type': 'lateness'},
        {'incident': False, 'type': 'none'},
        {'incident': True, 'type': 'error'}
    ]

    # Extract meaningful metrics
    metrics_dict, efficiency_ratio = analyze_productivity(user_logs)

    # Generate fake adjustments with red herrings
    adjustment_list = [2.5, -1.0, 3.0, 0.0, -0.5, 4.0]
    adjustment_list.append(efficiency_ratio * 10)  # Slight relevance

    # Call decoy functions to increase distraction
    risk_level = calculate_risk_profile(incident_history)
    baseline = compute_baseline(metrics_dict)
    biased_metrics = adjust_for_bias(metrics_dict, 1.02)

    # Core computation chain
    intermediate = efficiency_ratio * 100
    if intermediate > 50:
        adjustment_list.append(1.5)

    aggregated = sum(adjustment_list) * 10
    dummy_check = aggregated > 100

    # Critical statement
    final_score = process_performance(metrics_dict, adjustment_list)

    print(f"Result: {final_score}")