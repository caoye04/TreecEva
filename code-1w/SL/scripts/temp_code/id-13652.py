from collections import defaultdict

# Simulate user activity logs with timestamps and actions
def preprocess_logs(raw_logs):
    action_count = defaultdict(int)
    timestamp_weights = []
    total_entries = 0

    for entry in raw_logs:
        action = entry['action']
        timestamp = entry['time']
        action_count[action] += 1
        total_entries += 1
        
        # Irrelevant computation: weight based on timestamp (not used later)
        weight = (timestamp % 7) + 1
        timestamp_weights.append(weight)

    # Distractor: unused normalization
    normalized_weights = [w / max(timestamp_weights) for w in timestamp_weights] if timestamp_weights else [0]
    
    return dict(action_count), total_entries

def analyze_patterns(actions):
    pattern_score = 0
    keys = list(actions.keys())
    
    # Evaluate action diversity using string length (semi-relevant heuristic)
    for key in keys:
        if len(key) > 4:
            pattern_score += 1
        if 'click' in key:
            pattern_score += actions[key] * 0.5

    # Bitwise distraction: XOR of lengths (not actually impactful)
    xor_len = 0
    for k in keys:
        xor_len ^= len(k)
    dummy_mask = xor_len & 15
    
    # This score is returned but only partially influences final result
    return pattern_score

def calculate_final_score(data_dict):
    base_value = sum(data_dict.values())
    multiplier = 1.0
    
    # Conditional logic chain with nested conditions
    if base_value > 10:
        if 'scroll' in data_dict and data_dict['scroll'] >= 3:
            multiplier *= 1.2
        elif 'hover' in data_dict:
            multiplier *= 0.9
        else:
            multiplier *= 0.8
    
    if 'click_ad' in data_dict:
        bonus = data_dict['click_ad'] ** 2
        multiplier += bonus * 0.1

    # Real computation path
    adjustment = 0
    for act, cnt in data_dict.items():
        if 'exit' in act:
            adjustment -= cnt * 2
        elif 'start' in act:
            adjustment += cnt

    intermediate_result = base_value * multiplier + adjustment
    
    # Final transformation
    final_score = int(intermediate_result + 0.5)  # Round to nearest integer
    
    # Dead code: this doesn't affect anything
    if final_score < 0:
        final_score = 0
        redundant_reset = True

    return final_score

# Main execution
raw_activity_logs = [
    {'action': 'start_session', 'time': 1680001200},
    {'action': 'click_button', 'time': 1680001205},
    {'action': 'scroll_page', 'time': 1680001210},
    {'action': 'hover_menu', 'time': 1680001212},
    {'action': 'click_ad', 'time': 1680001218},
    {'action': 'scroll_page', 'time': 1680001225},
    {'action': 'exit_app', 'time': 1680001230},
    {'action': 'click_link', 'time': 1680001220},
    {'action': 'scroll_page', 'time': 1680001240},
    {'action': 'click_ad', 'time': 1680001250}
]

# Step-by-step processing
processed_counts, total = preprocess_logs(raw_activity_logs)
pattern_metric = analyze_patterns(processed_counts)
final_score = calculate_final_score(processed_counts)
print(f"Result: {final_score}")