from collections import Counter

# Simulate user interaction logs with redundant metadata
timestamps = [100, 105, 110, 115, 120, 125]
user_actions = ['click', 'scroll', 'click', 'keypress', 'click', 'scroll']
redundant_flags = [False, True, False, True, False, True]

# Extract action frequency (relevant)
action_counter = Counter(user_actions)
click_count = action_counter.get('click', 0)
scroll_count = action_counter.get('scroll', 0)
keypress_count = action_counter.get('keypress', 0)

# Simulated performance metrics (some irrelevant)
efficiency_ratio = (click_count * 1.5 + scroll_count * 0.8) / len(user_actions)
dummy_metric_x = sum(redundant_flags) * 0.3

# Feedback analysis with string processing
raw_feedback = ["verY gooD", "excellent!", "poor performancE", "Good job", "average"]
cleaned_feedback = [fb.strip("!.").lower() for fb in raw_feedback]
positive_indicators = ["good", "excellent", "great", "awesome", "job"]
negative_indicators = ["poor", "bad", "terrible", "awful", "average"]

feedback_counter = Counter()
for fb in cleaned_feedback:
    if any(pos in fb for pos in positive_indicators):
        feedback_counter['positive'] += 1
    elif any(neg in fb for neg in negative_indicators):
        feedback_counter['negative'] += 1
    else:
        feedback_counter['neutral'] += 1

# Efficiency rating based on action patterns (uses lambda)
action_efficiency_fn = lambda c, s, k: (c * 2 + s * 1 + k * 3) / (len(user_actions) or 1)
efficiency_rating = action_efficiency_fn(click_count, scroll_count, keypress_count)

# Dummy sort operation (irrelevant but adds complexity)
sorted_actions = sorted(action_counter.items(), key=lambda x: x[1], reverse=True)

# Red herring calculation
phantom_score = (dummy_metric_x + len(sorted_actions)) * 10

# Core evaluation logic
def evaluate_performance(feedback_counts, base_efficiency):
    positivity_rate = feedback_counts['positive'] / len(raw_feedback)
    negativity_rate = feedback_counts['negative'] / len(raw_feedback)
    
    # Apply weighted adjustment
    adjustment_factor = (positivity_rate * 1.8) - (negativity_rate * 1.2)
    adjusted_score = base_efficiency + adjustment_factor
    
    # Clamp and scale
    final = max(0, min(adjusted_score, 5)) * 10
    return int(final)

# Key assignment statement
final_score = evaluate_performance(feedback_counter, efficiency_rating)

# Irrelevant state tracking
current_state = {'score_updated': True, 'version': '2.1'}
previous_score = final_score - 5  # distractor

# Output result
print(f"Result: {final_score}")