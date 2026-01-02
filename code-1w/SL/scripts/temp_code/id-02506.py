def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for entry in logs:
        hours = entry['duration']
        status = entry['status']
        total_hours += hours
        if status == 'idle':
            idle_periods += 1
    efficiency = total_hours - (idle_periods * 0.5) if idle_periods > 0 else total_hours
    return efficiency

logs_data = [
    {'duration': 8, 'status': 'active'},
    {'duration': 1, 'status': 'idle'},
    {'duration': 5, 'status': 'active'},
    {'duration': 2, 'status': 'idle'},
    {'duration': 6, 'status': 'active'}
]

productivity_index = analyze_productivity(logs_data)

contributions = [4, 7, 2, 9, 5, 8]
impact_levels = [3, 8, 1, 7, 4, 6]
weights = [0.2, 0.8, 0.3, 0.5, 0.7, 0.4]

# Begin distraction: irrelevant aggregation
aggregate = 0
for i, val in enumerate(contributions):
    aggregate += val * weights[i % len(weights)]

normalized_aggregate = round(aggregate / len(contributions), 3)

# More red herring: mock progression tracking
progress_tracker = []
for idx, (c, i) in enumerate(zip(contributions, impact_levels)):
    if c > i:
        progress_tracker.append((idx, c - i))
    else:
        progress_tracker.append((idx, 0))

# Distractor: unused helper
def adjust_for_bias(x, factor=1.1):
    return [item * factor for item in x]

# Real computation begins
weighted_impact = 0
for c, i in zip(contributions, impact_levels):
    weighted_impact += c * i

average_contribution = sum(contributions) / len(contributions)
penalty = 0
for w in weights:
    if w < 0.5:
        penalty += 0.1  # minor penalty for low weights

adjusted_impact = weighted_impact - (penalty * 10)

scaling_factor = productivity_index / 20.0

intermediate_result = adjusted_impact * scaling_factor

# Final rating calculation
final_score = 0
def calculate_rating(contribs, impacts):
    base = 0
    for i, (c, p) in enumerate(zip(contribs, impacts)):
        if i % 2 == 0:
            base += c + p
        else:
            base += c * 0.5
    return int(base * 1.2)

final_score = calculate_rating(contributions, impact_levels)

# Irrelevant list transformation
transformed = [x**2 for x in contributions if x % 2 == 0]
sum_transformed = sum(transformed)

# Output target result
Result: {final_score}