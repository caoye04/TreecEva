def analyze_efficiency(metrics):
    adjusted = 0
    base_multiplier = 1.5
    temp_offset = 0.0  # unused variable (distractor)
    for val in metrics:
        if val > 75:
            adjusted += base_multiplier * val
        elif val > 50:
            adjusted += 0.8 * val
    return int(adjusted // 2)


def validate_input(data_str):
    if not isinstance(data_str, str):
        return False
    cleaned = data_str.strip().lower()
    return cleaned.startswith('report') and cleaned.endswith('end')

productivity = [80, 90, 45, 60, 70]
risk_factor = (0.9, 1.1)  # tuple usage
status_log = ['active', 'pending', 'failed']

# Irrelevant data structure (distractor)
project_timeline = {
    'planning': 10,
    'execution': 25,
    'review': 5
}

# Misleading computation (semi-relevant but not used in final logic)
cumulative_risk = 0
for r in risk_factor:
    cumulative_risk += r * 100

indicator_flag = len(status_log) > 2 and len(productivity) == 5

# Core logic with string method usage
def evaluate_performance(efforts, penalties):
    total_effort = sum(efforts)
    penalty_multiplier = penalties[0] if efforts[0] > 70 else penalties[1]
    
    # Simulate adjustment based on string pattern (uses string method)
    dummy_tag = "Report_Finalized_End"
    normalized_tag = dummy_tag.replace('_', '').upper()
    if 'FINALIZED' in normalized_tag:
        total_effort += 10
    
    raw_score = total_effort * penalty_multiplier
    
    # Additional check using comparison and tuple unpacking
    primary, secondary = risk_factor
    if primary < 1.0 and secondary > 1.0:
        raw_score *= 1.05
    
    return int(raw_score)

# Unused helper function (dead code path - distractor)
def calculate_baseline(values):
    return max(values) - min(values)

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")