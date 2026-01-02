def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency = {}
    for day, records in logs.items():
        daily_total = sum([r[1] for r in records])
        idle_count = len([r for r in records if r[2] < 20])
        total_hours += daily_total
        idle_periods += idle_count
        efficiency[day] = daily_total / (idle_count + 1)
    
    # Distractor: unused metric
    avg_hourly_rate = total_hours / len(logs) if logs else 0
    
    return total_hours, efficiency, idle_periods

logs_data = {
    'monday': [('task1', 4, 85), ('task2', 3, 90), ('break', 1, 5)],
    'tuesday': [('task1', 5, 78), ('task2', 2, 92), ('task3', 2, 88), ('idle', 0.5, 15)],
    'wednesday': [('task1', 3, 95), ('meeting', 2, 10), ('task2', 4, 80)]
}

# Extract only efficiency from analysis
_, raw_efficiency, _ = analyze_productivity(logs_data)

# Normalize efficiency scores using dictionary operations and zip
norm_factor = sum(raw_efficiency.values())
normalized = {k: v / norm_factor for k, v in raw_efficiency.items()}

# Simulate performance bands with string labels (distractor block)
band_labels = []
for score in normalized.values():
    if score > 0.35:
        band_labels.append('high')
    elif score > 0.25:
        band_labels.append('medium')
    else:
        band_labels.append('low')

# Contributions based on original hours (reused logic)
contributions = {}
for day, records in logs_data.items():
    contributions[day] = sum([r[1] * (r[2] / 100) for r in records])

# Secondary distractor: reverse lookup table with enumerate
index_map = {i: d for i, d in enumerate(['monday', 'tuesday', 'wednesday'])}
lookup_check = [key for key, val in index_map.items() if val in normalized]

# Core calculation function combining multiple concepts
def calculate_rating(contribs, eff):
    base = 0
    weights = list(zip(contribs.values(), eff.values()))  # Using zip
    for i, (c, e) in enumerate(weights):  # Using enumerate
        adjustment = (c * e) * (0.1 if i % 2 == 0 else 1.0)  # artificial asymmetry
        base += adjustment
    
    # Introduce irrelevant intermediate transforms
    temp_offsets = [abs(c - e*10) for c, e in weights]
    penalty = sum([x for x in temp_offsets if x > 5]) * 0.05  # minor tweak
    
    return int(base - penalty)  # deterministic integer output

# Final statement
final_score = calculate_rating(contributions, normalized)
print(f"Target result: {final_score}")