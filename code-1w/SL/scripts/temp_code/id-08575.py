from collections import defaultdict

# Simulated user interaction data with noise
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_inputs = ['click', 'scroll', 'click', 'hover', 'click']
durations = [1.2, 0.8, 2.1, 1.5, 3.0]

# Irrelevant auxiliary metrics (distractors)
system_load = [0.7, 0.85, 0.67, 0.92, 0.78]
memory_usage = [1024, 1056, 1030, 1070, 1040]

# Data preprocessing with red herrings
event_counter = defaultdict(int)
duration_sum = 0.0
for i, action in enumerate(raw_inputs):
    event_counter[action] += 1
    duration_sum += durations[i]
    # Misleading cumulative calculation (not used later)
    avg_duration = duration_sum / (i + 1)

# Redundant transformation (dead path)
temp_map = {}
for idx, val in enumerate(timestamps):
    temp_map[idx] = val * 0.001

# Core logic disguised among distractions
def analyze_engagement(data_list, mode='strict'):
    score = 0
    click_count = 0
    for entry in data_list:
        if entry == 'click':
            click_count += 1
            score += 3
        elif entry == 'scroll':
            score += 2
        elif entry == 'hover':
            score += 1
    if mode == 'strict' and click_count >= 2:
        score += 2  # Bonus for repeated engagement
    return score

# Another distraction: unused helper function
def calculate_entropy(seq):
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * p  # Simplified pseudo-entropy
    return round(entropy, 4)

# Real threshold logic obscured by irrelevant defaults
thresholds = {
    'min_clicks': 2,
    'bonus_eligible': True,
    'penalty_factor': 0.0,  # Unused parameter
    'scale': 1.0
}

user_data = []
for idx, (action, dur) in enumerate(zip(raw_inputs, durations)):
    entry = {
        'id': idx,
        'type': action,
        'time_spent': dur,
        'valid': True
    }
    # Conditional flag with misleading logic
    if dur < 1.0 and action != 'click':
        entry['valid'] = False
    user_data.append(entry)

# Actual processing chain
base_points = 0
engagement_multiplier = 1
invalid_count = 0

for record in user_data:
    if not record['valid']:
        invalid_count += 1
        continue
    if record['type'] == 'click':
        base_points += 5
    elif record['type'] == 'scroll':
        base_points += 3
    elif record['type'] == 'hover':
        base_points += 2

if invalid_count == 0:
    engagement_multiplier += 0.5

interim_score = base_points * engagement_multiplier

# Secondary analysis with tuple unpacking (semi-relevant)
action_summary = []
for i, inp in enumerate(raw_inputs):
    action_summary.append((i, inp, durations[i]))

click_durations = []
for _, act, dur in action_summary:
    if act == 'click':
        click_durations.append(dur)

avg_click_time = sum(click_durations) / len(click_durations) if click_durations else 0

# Final computation buried in conditional layers
def process_results(data, config):
    raw_score = 0
    bonus_applied = False
    
    # First pass: count valid clicks
    valid_clicks = 0
    for item in data:
        if item['type'] == 'click' and item['valid']:
            valid_clicks += 1
    
    # Apply tiered scoring
    if valid_clicks >= config['min_clicks']:
        raw_score += 10 * valid_clicks
        if config['bonus_eligible']:
            raw_score += 5
            bonus_applied = True
    
    # Incorporate hover events only if no invalid entries
    invalid_exists = any(not item['valid'] for item in data)
    if not invalid_exists:
        hover_count = sum(1 for item in data if item['type'] == 'hover')
        raw_score += hover_count * 3
    
    # Final scaling (despite 'scale' being 1.0)
    final = raw_score * config['scale']
    
    # Dead branch based on unused metric
    if avg_click_time > 1.0 and system_load[-1] > 0.9:
        final -= 2
        
    return int(final)

# Key execution point
final_score = process_results(user_data, thresholds)
print(f"Result: {final_score}")