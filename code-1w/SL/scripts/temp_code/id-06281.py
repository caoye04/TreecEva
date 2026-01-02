def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    distraction_score = 0

    for entry in logs:
        if 'work' in entry['type']:
            total_hours += entry['duration']
        elif 'idle' in entry['type']:
            idle_count += 1
            distraction_score += len(entry['notes'])

    efficiency = total_hours / (len(logs) or 1)
    return efficiency, distraction_score

logs_data = [
    {'type': 'work', 'duration': 2, 'notes': ''},
    {'type': 'idle', 'duration': 1, 'notes': 'meeting'},
    {'type': 'work', 'duration': 3, 'notes': ''},
    {'type': 'idle', 'duration': 0.5, 'notes': 'email check'},
    {'type': 'work', 'duration': 1.5, 'notes': ''},
    {'type': 'idle', 'duration': 0.25, 'notes': 'distraction'},
]

# Secondary analysis with string processing
title_case_filter = list(map(lambda x: x['type'].title(), logs_data))
valid_titles = [t for t in title_case_filter if 'Work' in t]

# Extract contribution markers from notes
contribution_flags = []
for log in logs_data:
    if log['notes']:
        words = log['notes'].split()
        flagged = list(filter(lambda w: w.lower() in ['urgent', 'priority', 'critical'], words))
        contribution_flags.extend(flagged)

# Simulate legacy system compatibility layer (unused)
legacy_buffer = {}
for i in range(len(logs_data)):
    legacy_buffer[f'entry_{i}'] = str(logs_data[i]).upper().replace(' ', '')

# Real computation begins here
efficiency_ratio, _ = analyze_productivity(logs_data)
contributions = len(contribution_flags)
penalty_factor = idle_count * 0.1

# Distractor: complex dictionary operation not directly affecting result
distraction_map = {f'level_{i}': i**2 for i in range(int(penalty_factor * 10) + 1)}
distraction_map.update({'baseline': 1})

bonus_multiplier = 1.0
if efficiency_ratio > 1.0:
    bonus_multiplier += 0.5

interim_value = contributions * 100

# Misleading intermediate calculation
fake_aggregate = sum([len(v) for v in distraction_map.values() if isinstance(v, int)])

# Key statement
final_score = calculate_rating(contributions, penalty_factor)

# Supporting function defined after use (adds cognitive load)
def calculate_rating(count, penalty):
    base = count * 25
    adjusted = base * (1 - penalty)
    if adjusted > 100:
        adjusted = 95  # Hard cap
    return int(adjusted + bonus_multiplier)

print(f"Result: {final_score}")