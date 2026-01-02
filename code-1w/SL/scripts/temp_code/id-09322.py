from collections import defaultdict

# Simulate developer contribution analysis with noise and filtering
def analyze_contributions(logs):
    contribution_count = defaultdict(int)
    file_types = []
c    total_lines = 0
    large_files = 0  # distractor: counts files over 500 lines

    for entry in logs:
        filename = entry['file']
        lines = entry['lines']
        contribution_count[filename.split('.')[0]] += 1
        file_types.append(filename.split('.')[-1])
        total_lines += lines

        if lines > 500:
            large_files += 1  # irrelevant to final result

    # Misleading intermediate computation
    avg_file_size = total_lines / len(logs) if logs else 0
    dominant_type = max(set(file_types), key=file_types.count) if file_types else ''

    return dict(contribution_count), avg_file_size, dominant_type


def calculate_rating(contributions, penalty_factor):
    base_score = 0
    tier_bonus = 0

    for module, count in contributions.items():
        if count >= 5:
            tier_bonus += 3
        elif count >= 3:
            tier_bonus += 1

        # Core scoring logic
        base_score += (count * 7) // 2

    raw_score = base_score + tier_bonus

    # Apply penalty smoothing (only affects result once)
    adjusted = raw_score * (1 - penalty_factor)
    rounded = round(adjusted)

    # Dead code branch - never executed due to input constraints
    if penalty_factor > 1.0:
        fallback = sum(len(x) for x in contributions.keys())
        return fallback

    return rounded

# Log data with realistic structure
activity_log = [
    {'file': 'auth.service.ts', 'lines': 120},
    {'file': 'auth.middleware.py', 'lines': 85},
    {'file': 'auth.utils.py', 'lines': 67},
    {'file': 'db.manager.ts', 'lines': 203},
    {'file': 'db.schema.sql', 'lines': 344},
    {'file': 'db.migration.py', 'lines': 156},
    {'file': 'api.routes.py', 'lines': 94},
    {'file': 'api.validation.py', 'lines': 78},
    {'file': 'api.docs.ts', 'lines': 134}
]

# Extract components
contribution_data, mean_size, primary_ext = analyze_contributions(activity_log)

# Secondary processing: filter noisy modules
filtered_modules = {k: v for k, v in contribution_data.items() if k not in ['temp', 'backup']}

# Red herring calculation
complexity_metric = sum(
    len(name) * cnt for name, cnt in filtered_modules.items() if 'auth' in name
) / len(filtered_modules) if filtered_modules else 0

# Key control flow with early exit red herring
threshold = 10
if complexity_metric > threshold:
    final_score = -1
else:
    penalty_factor = 0.15
    final_score = calculate_rating(filtered_modules, penalty_factor)

print(f"Result: {final_score}")