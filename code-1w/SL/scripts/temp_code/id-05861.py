def calculate_base_score(data):
    base = 0
    temp_sum = 0  # distractor: used only for debugging trace
    debug_log = []

    for k, v in data.items():
        if len(k) % 2 == 0:
            base += v * 1.5
        else:
            base += v * 0.8
        temp_sum += v
        debug_log.append(f'{k}:{v}')  # irrelevant accumulation

    scaling_factor = 1.2 if temp_sum > 50 else 0.9
    return base * scaling_factor


def apply_threshold(value, limit=75):
    if value < limit:
        return value + 10
    elif value == limit:
        return value * 1.1
    else:
        return value * 0.95


def calculate_adjusted_score(profile, extras):
    score = calculate_base_score(profile)

    # Distractor block: dead code path (never modifies score)
    shadow_copy = profile.copy()
    for key in shadow_copy:
        if 'temp' in key:
            shadow_copy[key] *= 2  # never executed

    # String manipulation distraction
    keys_str = ''.join(sorted(profile.keys()))
    char_sum = sum(ord(c) for c in keys_str if c.islower())
    noise_offset = char_sum % 11

    # Real adjustment
    bonus_total = sum(extras.get(cat, 0) for cat in ['skills', 'experience', 'certs'])
    adjusted = score + bonus_total

    # Early termination based on condition
    if adjusted > 120:
        adjusted = 120  # hard cap

    # Apply threshold logic
    final = apply_threshold(adjusted)

    # Irrelevant list processing
    categories = ['skills', 'experience', 'certs', 'temp']
    weights = {cat: 1.1 if cat in profile else 0.9 for cat in categories}
    weighted_total = sum(weights[cat] * extras.get(cat, 0) for cat in categories)  # unused

    return final

# Main execution
user_data = {
    'skills': 40,
    'experience': 35,
    'certs': 20,
    'prefs': 10
}

bonus_map = {
    'skills': 8,
    'experience': 12,
    'certs': 5,
    'extra_bonus': 100  # not used
}

interim_value = sum(user_data.values()) * 0.5  # red herring computation

final_score = calculate_adjusted_score(user_data, bonus_map)

print(f"Result: {final_score}")