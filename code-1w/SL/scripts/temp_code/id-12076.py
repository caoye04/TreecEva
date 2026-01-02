from collections import Counter, defaultdict

# Simulate user interaction logs with action types
log_entries = [
    'click:start', 'hover:menu', 'click:save', 'keypress:submit',
    'click:cancel', 'hover:tooltip', 'click:save', 'click:start',
    'keypress:navigate', 'click:save', 'click:cancel', 'hover:menu'
]

# Parse actions and categorize
actions = [entry.split(':')[0] for entry in log_entries]
action_types = ['click', 'hover', 'keypress']

# Count raw frequencies
raw_counts = {atype: actions.count(atype) for atype in action_types}

distraction_var1 = sum(raw_counts.values()) + 100  # Irrelevant offset
unused_calc = distraction_var1 * 2  # Dead computation

# Build frequency distribution using Counter
action_counter = Counter(actions)

# Compute derived metrics
total_interactions = sum(action_counter.values())
efficiency_ratio = action_counter['click'] / total_interactions if total_interactions else 0

# Simulate multi-user data aggregation with defaultdict
user_actions = defaultdict(list)
for i, entry in enumerate(log_entries):
    user_id = i % 3
    action = entry.split(':')[0]
    user_actions[user_id].append(action)

# Aggregate per-user counts (semi-relevant)
user_counters = {uid: Counter(acts) for uid, acts in user_actions.items()}

# Focus on system-wide pattern: detect repeated 'save' after 'start'
sequence_pattern = []
for i in range(len(actions) - 1):
    if actions[i] == 'click' and log_entries[i].endswith(':start'):
        next_action = actions[i+1]
        sequence_pattern.append(next_action)

# Evaluate success rate based on saving after start
success_followups = [act for act in sequence_pattern if act == 'click']  # All are clicks anyway
valid_saves = sum(1 for i in range(len(log_entries)-1)
                  if log_entries[i].endswith(':start') and log_entries[i+1].endswith(':save'))

# Prepare data for scoring
baseline = action_counter['click'] * efficiency_ratio
data_counter = Counter({
    'valid_transitions': valid_saves,
    'total_starts': log_entries.count('click:start'),
    'redundant_ops': raw_counts['hover']
})

threshold = 0.75

# Misleading intermediate score
temp_score = (data_counter['valid_transitions'] / data_counter['total_starts']) if data_counter['total_starts'] else 0
distraction_var2 = temp_score > threshold  # Boolean red herring

# Core evaluation logic
def evaluate_performance(counter, thresh):
    starts = counter['total_starts']
    saves = counter['valid_transitions']
    hover_penalty = counter['redundant_ops'] * 0.1
    
    if starts == 0:
        return 0
    
    completion_rate = saves / starts
    adjusted_rate = completion_rate - hover_penalty
    
    # Apply non-linear boost for high efficiency
    if completion_rate >= thresh:
        adjusted_rate *= 1.25
    
    return int(adjusted_rate * 100)  # Final integer score

final_score = evaluate_performance(data_counter, threshold)

print(f"Result: {final_score}")