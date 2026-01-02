def analyze_metrics(data, threshold=5):
    if len(data) < threshold:
        return False
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return variance < 10

# Irrelevant utility function (decoy)
def encrypt_key(s: str) -> str:
    return ''.join(chr((ord(c) + 3) % 90) for c in s.upper())

# Unused but plausible-looking transformation
def transform_sequence(seq):
    return [seq[i] * (i + 1) for i in range(len(seq))] if seq else []

# Real logic starts here
def calculate_rank_value(level, multiplier):
    base = 100
    adjustment = 0
    
    if level > 8:
        adjustment += 25
    elif level > 5:
        adjustment += 10
    else:
        adjustment -= 5
    
    temp_result = base + adjustment  # Red herring variable
    return int((base + adjustment) * multiplier)

# Complex conditional expression and dictionary use
def get_penalty_config(category):
    config_map = {
        'alpha': {'penalty': 0.1, 'active': True},
        'beta': {'penalty': 0.25, 'active': False},
        'gamma': {'penalty': 0.4, 'active': True}
    }
    return config_map.get(category, {'penalty': 0.15, 'active': True})

# Heavily distracted main computation
def evaluate_performance(rank, points, factor_override=None):
    # Distractor variables
    shadow_points = points * 0.85
    dummy_tracker = {"stage1": 0, "stage2": None, "flag": False}
    
    # Real calculation embedded in noise
    base_component = points // 2
    rank_bonus = 0
    
    if rank >= 10:
        rank_bonus = 50
    elif rank >= 7:
        rank_bonus = 30
    elif rank >= 4:
        rank_bonus = 15
    else:
        rank_bonus = 5
    
    # Conditional expression with string method distraction
    status_tag = "PREMIUM" if points > 200 else "STANDARD"
    tag_modifier = len(status_tag.lower().replace("a", ""))  # Irrelevant transformation
    
    # Actual performance score before penalty
    raw_score = base_component + rank_bonus
    
    # Penalty application using dictionary lookup
    category = "gamma"
    penalty_info = get_penalty_config(category)
    
    if penalty_info['active']:
        applied_factor = factor_override or penalty_info['penalty']
        deduction = raw_score * applied_factor
        final_score = raw_score - deduction
    else:
        final_score = raw_score  # Dead branch (misleading)
    
    # More distractions below
    audit_log = []
    for i in range(3):
        audit_log.append(f"Step {i}: processed")  # Side-effect free logging
    
    # Unused list comprehension with bitwise red herring
    _ = [(raw_score >> 1) & i for i in [1, 2, 4] if i != 3]
    
    # Final override check (never triggers due to logic)
    if 'X' in [chr(ord('A') + 23), 'Y', 'Z'] and False:
        final_score = 999
    
    return int(final_score)

# Irrelevant data structure initialization
dataset = [12, 15, 18, 22, 7]
encryption_keys = ['KEY1', 'KEY2']
key_pool = {k: encrypt_key(k) for k in encryption_keys}

# Triggering transformation that isn't used
temp_seq = transform_sequence([1, 2, 3])

# Main execution path
rank = 9
base_points = 240
penalty_factor = None

# Critical statement
final_score = evaluate_performance(rank, base_points, penalty_factor)

# Output result
print(f"Result: {final_score}")