from collections import defaultdict, Counter

def analyze_performance(activities):
    # Track engagement and outcomes
    engagement_log = defaultdict(int)
    outcome_summary = {'success': 0, 'failure': 0}
    temporal_weights = [1.1, 0.9, 1.2, 0.8, 1.0]
    
    base_multiplier = 2
    adjustment_factor = 0.5
    phantom_counter = 0  # Unused distractor
    
    for idx, (activity, details) in enumerate(activities.items()):
        duration = details['duration']
        success_flag = details['success']
        complexity = details.get('complexity', 1)
        
        # Log engagement with time-based weight (only first 5 activities considered)
        if idx < len(temporal_weights):
            weighted_engagement = duration * temporal_weights[idx]
            engagement_log[activity] = int(weighted_engagement)
        else:
            engagement_log[activity] = duration

        # Update outcome summary
        if success_flag:
            outcome_summary['success'] += 1 * complexity
        else:
            outcome_summary['failure'] += 1 * complexity
            
        # Irrelevant side computation (distractor)
        for i in range(3):
            phantom_counter += idx * adjustment_factor

    return engagement_log, outcome_summary

def compute_aggregate(log, summary, threshold=5):
    total_engagement = sum(log.values())
    success_count = summary['success']
    failure_count = summary['failure']
    
    # Apply conditional boost
    boost_modifier = 1.0
    if success_count > failure_count and total_engagement > threshold:
        boost_modifier = 1.4
    elif failure_count > success_count:
        boost_modifier = 0.7

    # Dummy variables for distraction
    dummy_aggregation = 0
    for k, v in log.items():
        dummy_aggregation += len(k) * v % 3
    
    raw_score = (total_engagement + success_count * 10 - failure_count * 5)
    final_score = int(raw_score * boost_modifier)
    
    # Additional irrelevant transformation
    shadow_score = raw_score * 0.5
    shadow_score = (shadow_score + 10) * (1 if shadow_score > 20 else 0.5)
    
    return final_score

# Main execution
if __name__ == '__main__':
    activity_data = {
        'onboarding': {'duration': 12, 'success': True, 'complexity': 2},
        'setup_phase': {'duration': 8, 'success': True, 'complexity': 1},
        'data_import': {'duration': 15, 'success': False, 'complexity': 3},
        'validation': {'duration': 6, 'success': True, 'complexity': 2},
        'export_cycle': {'duration': 10, 'success': False, 'complexity': 1}
    }

    log, summary = analyze_performance(activity_data)
    final_score = compute_aggregate(log, summary, threshold=5)
    
    # Critical point: final_score is now computed
    Result: {final_score}