from collections import defaultdict, Counter

# Simulated user interaction log with various actions
event_log = [
    'click:header', 'hover:sidebar', 'click:button_A', 'keypress:enter',
    'click:button_B', 'hover:tooltip', 'click:button_A', 'click:header',
    'keypress:esc', 'click:button_C', 'hover:sidebar', 'click:button_B'
]

# Misleading irrelevant counters
aux_counter_1 = 0
aux_counter_2 = 0
temp_accumulator = 0

# Track event frequencies
event_freq = defaultdict(int)
for event in event_log:
    aux_counter_1 += len(event) % 3  # Distractor computation
    if 'hover' in event:
        temp_accumulator += 1
    event_type = event.split(':')[0]
    event_freq[event_type] += 1

# Extract counts for key actions
click_count = event_freq['click']
keypress_count = event_freq['keypress']
hover_count = event_freq['hover']

# Secondary distractor: process string patterns
unique_actions = set()
action_length_sum = 0
for event in event_log:
    action = event.split(':')[1]
    unique_actions.add(action)
    action_length_sum += len(action)
    if action.startswith('b'):
        aux_counter_2 += 1  # Red herring

# Compute derived metrics
avg_action_length = action_length_sum / len(event_log)
unique_click_targets = len([e for e in event_log if e.startswith('click:')])

# Normalize click distribution
click_distribution = Counter([e.split(':')[1] for e in event_log if e.startswith('click:')])
normalized_scores = {k: v / click_count for k, v in click_distribution.items()}

# Apply weighting scheme based on interaction type
raw_weights = {
    'click': 2.5,
    'keypress': 4.0,
    'hover': 0.8
}

weighted_score = (
    raw_weights['click'] * click_count + 
    raw_weights['keypress'] * keypress_count + 
    raw_weights['hover'] * hover_count
)

# Adjustment factor based on uniqueness and balance
balance_factor = 1.0
if len(unique_actions) > 3:
    balance_factor += 0.3
if click_distribution['button_A'] == click_distribution['button_B']:
    balance_factor += 0.2

# Final processing function
def calculate_final_score(data):
    base = data.get('weighted', 0)
    adjustment = data.get('bonus', 0)
    penalty = data.get('penalty', 0)
    return int((base * adjustment) - penalty)

# Prepare processed data with some redundant fields
processed_data = {
    'weighted': weighted_score,
    'bonus': balance_factor,
    'penalty': avg_action_length,
    'meta': {
        'total_events': len(event_log),
        'distinct_types': len(event_freq),
        'max_freq': max(click_distribution.values())
    },
    'debug_info': f"Events: {len(event_log)}"
}

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")