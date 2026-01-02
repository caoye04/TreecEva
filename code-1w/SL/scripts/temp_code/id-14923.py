def transform_values(arr, factor):
    # Irrelevant transformation function (dead code path)
    return [x * factor + 2 for x in arr if x % 2 == 0]


def compute_hash(text):
    # Distractor: computes a hash but never used in critical path
    return sum(ord(c) for c in text) % 1000


def adjust_threshold(base, mode=True):
    # Misleading intermediate calculation
    if mode:
        return base * 1.5
    else:
        return base * 0.7


def recursive_weight(n):
    # Relevant but obscured recursive function
    if n <= 1:
        return 1
    return n * 0.9 + recursive_weight(n - 2)


def validate_entry(record):
    # Decoy validation logic that looks important but isn't on main path
    if not record.get('active'):
        return False
    if record['level'] < 0:
        return False
    return True

# Simulated metric data from system logs
metric_data = {
    'raw': [3, 7, 14, 21, 28],
    'weights': {k: k*0.5 for k in range(1, 6)},
    'flags': ['A', 'C', 'D'],
    'active_index': 3
}

# Irrelevant data structure (distractor)
user_profile = {
    'id': 'USR-7812',
    'access_level': 'admin',
    'permissions': ['read', 'write', 'execute'],
    'last_login_hash': compute_hash('2023-11-05T14:30:00Z')
}

# Bonus rules with red herring conditions
bonus_rules = [
    {'condition': 'streak > 5', 'multiplier': 2.0},
    {'condition': 'accuracy >= 0.9', 'multiplier': 1.75},
    {'condition': 'timely', 'multiplier': 1.5}
]

# Hidden but relevant parameters
base_factor = 4
shift_correction = adjust_threshold(8)  # Returns 12.0, distractor

# Critical computation chain begins here
filtered_metrics = metric_data['raw'][1:4]  # slicing operation
weighted_sum = 0
for i, val in enumerate(filtered_metrics):
    weight = metric_data['weights'][i+1]
    weighted_sum += val * weight

# Conditional expression with logical operations
penalty = 0 if all(x > 5 for x in filtered_metrics) and len(metric_data['flags']) != 2 else 100

# Bit manipulation decoy
debug_flag = (0b1010 >> 2) ^ 0b1101 & 0b0010  # evaluates to 1, unused

# Recursive component in scoring
recursion_anchor = int(recursive_weight(5))  # evaluates to 9 (5*0.9 + 3*0.9 + 1 = 4.5+2.7+1=8.2→9)

# Tuple unpacking (distraction)
config_keys = ['mode', 'level', 'role']
a, b, c = config_keys

# Main scoring logic buried in context
bonus_multiplier = 1.25
if metric_data['active_index'] in metric_data['weights']:
    bonus_multiplier *= 1.4

# Case conversion decoy
mode_flag = user_profile['access_level'].upper()  # 'ADMIN'

# Final evaluation using dictionary lookup and arithmetic
def evaluate_performance(data, mult):
    base_score = weighted_sum - penalty
    adjustment = data['weights'][data['active_index']]  # uses active_index=3 → weight=1.5
    adjusted = base_score * adjustment
    final = adjusted * mult + recursion_anchor
    return final

# Execution point of interest
final_score = evaluate_performance(metric_data, bonus_multiplier)

# Output result as required
print(f"Result: {final_score}")