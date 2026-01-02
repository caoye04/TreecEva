from collections import defaultdict, Counter

# Simulate user interaction logs with action types and durations
def generate_logs():
    return [
        ('click', 120), ('scroll', 30), ('hover', 45), ('click', 200),
        ('keypress', 5), ('scroll', 60), ('click', 90), ('hover', 40),
        ('click', 180), ('keypress', 10), ('scroll', 90), ('hover', 50)
    ]

# Analyze engagement based on action type and cumulative duration
def analyze_engagement(logs):
    total_duration = 0
    action_count = defaultdict(int)
    duration_by_action = defaultdict(float)
    
    for action, duration in logs:
        action_count[action] += 1
        duration_by_action[action] += duration
        total_duration += duration

    avg_duration_per_action = {
        k: v / action_count[k] for k, v in duration_by_action.items()
    }
    
    # Misleading distraction: entropy calculation (not used later)
    from math import log
    entropy = 0
    for count in action_count.values():
        prob = count / len(logs)
        entropy -= prob * log(prob) if prob > 0 else 0
    
    # Normalize scores using max duration as baseline
    max_duration = max(duration_by_action.values())
    normalized_scores = {
        k: (v / max_duration) * 100 for k, v in duration_by_action.items()
    }
    
    return normalized_scores, total_duration, avg_duration_per_action

# Process data through multiple filtering and scoring stages
def filter_and_score(normalized, avg_durations, threshold=75.0):
    filtered = {k: v for k, v in normalized.items() if v >= threshold}
    bonus_points = 0
    
    # Apply bonus logic based on average behavior
    if avg_durations.get('click', 0) > 100:
        bonus_points += 15
    if len(filtered) >= 2:
        bonus_points += 10
    
    # Distraction: unused transformation
    inverted = {k: 100 - v for k, v in normalized.items()}  
    temp_sum = sum(inverted.values())  # Dead computation
    
    return filtered, bonus_points

# Calculate final score with weighted components
def calculate_final_score(data_dict):
    base = sum(data_dict.values())
    multiplier = len(data_dict) if len(data_dict) > 0 else 1
    
    # Extra distraction: case conversion on keys (irrelevant to result)
    upper_keys = [k.upper() for k in data_dict.keys()]
    key_lengths = [len(k) for k in upper_keys]  # Computed but unused
    
    raw_score = base * multiplier
    
    # Apply cap logic
    if raw_score > 300:
        raw_score = 300 + (raw_score - 300) / 10  # Diminishing returns
    
    return int(raw_score)

# Main execution flow
if __name__ == '__main__':
    logs = generate_logs()
    
    # Step 1: Analyze raw logs
    norm_scores, total_time, averages = analyze_engagement(logs)
    
    # Step 2: Filter actions and compute bonus
    relevant_actions, extra_pts = filter_and_score(norm_scores, averages)
    
    # Step 3: Prepare processed data (only relevant actions passed)
    processed_data = {
        k: v + extra_pts for k, v in relevant_actions.items()
    }
    
    # Step 4: Compute final score — KEY STATEMENT
    final_score = calculate_final_score(processed_data)
    
    # Print result for extraction
    print(f"Result: {final_score}")