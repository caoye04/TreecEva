def analyze_user_activity(logs):
    total_actions = 0
    unique_pages = set()
    idle_time = 0  # Distractor: not used in final calculation
    temp_factor = 1.5  # Distractor variable

    for log in logs:
        action_list = log['actions'].split(',')
        total_actions += len(action_list)
        
        page_visits = log['pages']
        unique_pages.update(page_visits)
        
        # Irrelevant computation (dead-end path)
        if len(action_list) > 5:
            spike_count = 0
            spike_count += 1  # Local variable, no effect

    return total_actions, unique_pages


def calculate_complexity_metric(pages):
    # Semi-relevant transformation
    complexity = 0
    for page in pages:
        complexity += len(page) % 3
    return max(complexity, 1)


def calculate_rating(data, min_threshold):
    base_score = 0
    adjustment = 0.0
    penalty = 0  # Unused distractor

    raw_engagement, distinct_pages = analyze_user_activity(data)
    
    # Core logic begins
    if raw_engagement > min_threshold:
        base_score += 100
        size_factor = len(distinct_pages)
        
        # Additional check with string method
        high_traffic = [p for p in distinct_pages if p.startswith('user')]
        if len(high_traffic) >= 2:
            base_score += 25

        # Use of dictionary operation
        page_freq = {p: data[0]['pages'].count(p) for p in distinct_pages}
        dominant_pages = {k for k, v in page_freq.items() if v > 1}
        adjustment = len(dominant_pages) * 3.5
        
        # Red herring: complex-looking but unused recursion
        def recursive_weight(n):
            if n <= 1:
                return 1
            return n * recursive_weight(n-2)
        
        dummy_tree_depth = recursive_weight(3)  # Evaluates to 3, not used
        
        base_score += int(adjustment)
    else:
        base_score += 50
    
    # Final irrelevant filtering
    filtered_logs = [x for x in data if 'admin' not in x['user_role']]
    scaling_multiplier = 1  # Obvious but distracting

    final_score = base_score + 10  # Key assignment
    return final_score

# Input data
engagement_data = [
    {
        'user_role': 'member',
        'actions': 'click,scroll,hover,click,click',
        'pages': ['home', 'user_profile', 'user_settings', 'dashboard']
    },
    {
        'user_role': 'guest',
        'actions': 'view,click,scroll',
        'pages': ['home', 'about', 'user_profile']
    }
]

threshold = 8

final_score = calculate_rating(engagement_data, threshold)
print(f"Target result: {final_score}")