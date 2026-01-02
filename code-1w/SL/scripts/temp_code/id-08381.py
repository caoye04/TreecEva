def analyze_frequency(text):
    # Irrelevant character frequency analysis (distractor)
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:5]  # Only top 5 used, not impacting main logic


def validate_bounds(value, lower=0, upper=100):
    # Semi-relevant validation function (only some calls matter)
    if value < lower:
        return lower
    elif value > upper:
        return upper
    return value

# Main computation setup
raw_data = [85, 90, 78, 92, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Distractor: Weight normalization (not actually needed due to pre-defined values)
total_weight = sum(weights)
normalized_weights = [w / total_weight for w in weights]

# Primary data structure: student performance stats
stats = {
    'exam': raw_data[0],
    'project': raw_data[1],
    'homework': raw_data[2],
    'participation': raw_data[3],
    'quiz': raw_data[4]
}

# Modifier dictionary with red herring entries
modifiers = {
    'curve': 1.05,
    'penalty': 0.98,
    'bonus_eligible': True,
    'attendance_factor': 1.02,
    'irrelevant_threshold': 42.5,  # unused field
    'hidden_multiplier': 1.0       # placeholder
}

# Auxiliary calculation: average with dropped lowest quiz (semi-relevant)
dropped_quiz_avg = (sum(raw_data) - min(raw_data)) / (len(raw_data) - 1)

# Distraction block: simulate historical trend comparison
historical_high = 91.2
projected_growth = (stats['exam'] + dropped_quiz_avg) / 2 * 0.015
adjusted_reference = validate_bounds(historical_high + projected_growth)

# Core scoring logic
base_total = 0
for key, value in stats.items():
    if key == 'exam':
        base_total += value * 0.3
    elif key == 'project':
        base_total += value * 0.3
    elif key == 'homework':
        base_total += value * 0.2
    else:
        base_total += value * 0.1

# Apply curve and bonus logic (uses dictionary)
final_score = base_total * modifiers['curve']

if modifiers['bonus_eligible']:
    extra = stats['project'] * 0.02
    final_score += extra

final_score *= modifiers['attendance_factor']

# Final capping via helper function
final_score = validate_bounds(final_score, 0, 100)

# Side computation: entropy-like measure on digits (completely irrelevant)
digits = [int(d) for d in str(int(final_score * 100))]
unique_digits = set(digits)
entropy_approx = sum(d * d for d in unique_digits) / len(unique_digits) if unique_digits else 0

# Critical execution point
final_score = calculate_final_score(stats, modifiers)

# Simulate function that was already logically resolved above
def calculate_final_score(s, m):
    temp = 0
    temp += s['exam'] * 0.3
    temp += s['project'] * 0.3
    temp += s['homework'] * 0.2
    temp += (s['participation'] + s['quiz']) * 0.1
    temp *= m['curve']
    if m['bonus_eligible']:
        temp += s['project'] * 0.02
    temp *= m['attendance_factor']
    return validate_bounds(temp)

print(f"Result: {final_score}")