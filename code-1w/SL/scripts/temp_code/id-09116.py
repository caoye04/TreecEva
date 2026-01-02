def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0

    for day in logs:
        daily_total = sum(day['work_blocks'])
        daily_idle = len([x for x in day['breaks'] if x > 30])
        total_hours += daily_total
        idle_periods += daily_idle

    if total_hours > 0:
        efficiency_ratio = (total_hours - idle_periods * 0.5) / total_hours
    
    return total_hours, efficiency_ratio


def calculate_rating(contributions, penalties):
    base_score = 0
    tier_bonus = 0
    penalty_deduction = 0
    compliance_check = set()
    
    # Evaluate contribution quality
    high_quality = {k for k, v in contributions.items() if v['quality'] >= 8}
    mid_quality = {k for k, v in contributions.items() if 5 <= v['quality'] < 8}
    compliance_check.update(high_quality)
    compliance_check.update(mid_quality)
    
    for item_id, data in contributions.items():
        base_score += data['complexity'] * data['quality']
        if data['review_status'] == 'approved':
            compliance_check.add(item_id)
    
    # Apply tier-based bonuses
    if len(high_quality) >= 5:
        tier_bonus = 25
    elif len(high_quality) >= 3:
        tier_bonus = 15
    else:
        tier_bonus = 5
    
    # Process penalty deductions
    severity_map = {'minor': 2, 'major': 8, 'critical': 20}
    temp_penalty = 0
    for p in penalties:
        temp_penalty += severity_map.get(p['level'], 0)
        if p['resolved']:
            temp_penalty -= 1  # small credit for resolution
    
    penalty_deduction = max(0, temp_penalty)
    
    final_score = int(base_score + tier_bonus - penalty_deduction)
    
    # Irrelevant post-processing (distractor)
    summary_report = {
        'entries': len(contributions),
        'coverage': len(compliance_check) / len(contributions) if contributions else 0,
        'idle_warnings': [i for i in range(3) if i % 2 == 0]  # dummy list
    }
    
    return final_score

# Simulated input data
activity_logs = [
    {'work_blocks': [2.5, 1.0, 3.0], 'breaks': [15, 45, 10]},
    {'work_blocks': [4.0, 2.0], 'breaks': [60, 20]},
    {'work_blocks': [1.5, 1.5, 1.5, 1.5], 'breaks': [5, 5, 5, 5]}
]

contrib_data = {
    'feat_auth': {'quality': 9, 'complexity': 4, 'review_status': 'approved'},
    'feat_cache': {'quality': 7, 'complexity': 3, 'review_status': 'approved'},
    'fix_memory': {'quality': 8, 'complexity': 5, 'review_status': 'pending'},
    'ui_dashboard': {'quality': 6, 'complexity': 2, 'review_status': 'approved'},
    'api_migration': {'quality': 9, 'complexity': 6, 'review_status': 'approved'},
    'logging_infra': {'quality': 5, 'complexity': 3, 'review_status': 'approved'}
}

penalty_list = [
    {'level': 'minor', 'resolved': True},
    {'level': 'major', 'resolved': False},
    {'level': 'minor', 'resolved': False},
    {'level': 'critical', 'resolved': False},
    {'level': 'minor', 'resolved': True}
]

# Execute core analysis (distraction)
total_hrs, efficiency = analyze_productivity(activity_logs)

# Key computation
final_score = calculate_rating(contrib_data, penalty_list)

# Output result
print(f"Result: {final_score}")