def analyze_access_pattern(sequence):
    frequency = {}
    for item in sequence:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

# Irrelevant helper function (decoy)
def decrypt_key(token):
    return sum(ord(c) * (i + 1) for i, c in enumerate(token)) % 1000

def evaluate_threshold(values, limit=5):
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count > len(values) // 2

# Misleading data transformation (red herring)
raw_input = [3, 7, 2, 8, 7, 4, 9]
sorted_data = sorted(raw_input)
doubled_values = [x * 2 for x in sorted_data if x % 2 == 1]

# Real processing begins here
user_actions = ['login', 'edit', 'view', 'edit', 'login', 'view', 'view']
action_freq = analyze_access_pattern(user_actions)

priority_weights = {'login': 3, 'edit': 5, 'view': 2}
weighted_sum = 0
for action, freq in action_freq.items():
    weighted_sum += freq * priority_weights.get(action, 1)

# Bit manipulation layer (partially relevant)
shifted_weight = (weighted_sum << 2) ^ 0xA

# Distractor: unused complex structure
token_map = {chr(i): decrypt_key(chr(i)*3) for i in range(97, 105)}

# Conditional masking based on threshold (distractor logic)
if evaluate_threshold([shifted_weight, weighted_sum, len(user_actions)]):
    base_offset = shifted_weight % 17
else:
    base_offset = 11

# Core data structure with zip and enumerate (relevant)
user_data = list(zip(
    [f'user_{i}' for i in range(1, 6)],
    [200, 150, 300, 100, 250],
    ['tier_1', 'tier_2', 'tier_1', 'tier_3', 'tier_2']
))

# Multiple assignment and distractor unpacking
total_users, _, tier_list = zip(*user_data)
unique_tiers = set(tier_list)

# Main aggregation logic
running_scores = []
for idx, (uid, points, tier) in enumerate(user_data):
    bonus = 0
    # Nested conditional with bitwise distraction
    if tier == 'tier_1':
        bonus = 20
    elif tier == 'tier_2':
        bonus = 15
    else:
        bonus = 5
    
    # Complex scoring with irrelevant intermediate
    temp_modifier = (idx + 1) * (points & 0xFF)  # bitwise AND
    temp_modifier = temp_modifier >> 1  # shift right (not fully used)
    final_points = points + bonus + base_offset
    running_scores.append(final_points)

# Decoy loop with no effect
shadow_copy = []
for val in running_scores:
    shadow_copy.append(val ^ 0xFF)  # XOR with 255, never used

# Actual final computation
aggregate_performance = lambda data, offset: (
    sum(score for score in running_scores) + offset
)

# Critical execution point
final_score = aggregate_performance(user_data, base_offset)

print(f"Result: {final_score}")