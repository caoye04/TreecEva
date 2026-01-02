def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for log in logs:
        entries = log.split(',')
        daily_hours = 0
        for entry in entries:
            cleaned = entry.strip().lower()
            if 'work' in cleaned:
                minutes = int(cleaned.replace('work_', ''))
                daily_hours += minutes / 60
            elif 'break' in cleaned:
                idle_periods += 1
        total_hours += daily_hours
    efficiency = total_hours / (len(logs) + 1)
    return efficiency, idle_periods

logs_data = [
    'work_45,break,work_60,work_30',
    'work_90,break,work_45',
    'work_30,work_75,break'
]

# Irrelevant aggregation
idle_time = sum(1 for log in logs_data for e in log.split(',') if 'break' in e)
efficiency_rate, _ = analyze_productivity(logs_data)

contributions = [8, 12, 5, 17, 9]
impact_levels = [3, 5, 2, 4, 3]
baseline = {'threshold': 6, 'weight': 0.7}

# Misleading pre-processing
temp_weights = []
for c in contributions:
    if c > baseline['threshold']:
        temp_weights.append(c * baseline['weight'])
    else:
        temp_weights.append(c * 0.3)

# Real computation hidden among distractions
def calculate_rating(contribs, impacts):
    weighted_sum = 0
    adjustment = 0
    for i in range(len(contribs)):
        weighted_sum += contribs[i] * impacts[i]
        if impacts[i] >= 4:
            adjustment += contribs[i] * 0.1
    
    # Distractor: unused loop with string operations
    categories = ['high', 'medium', 'low']
    category_map = {cat: cat.upper() + '_PERF' for cat in categories}
    for k in category_map:
        category_map[k] = category_map[k].replace('_PERF', '_RATING')
    
    # Another distractor: dictionary reshaping
    stats = {i: contribs[i] for i in range(len(contribs))}
    avg_contrib = sum(stats.values()) / len(stats)
    
    # Actual logic
    base_rating = weighted_sum / (sum(impacts) + 1e-8)
    final_rating = base_rating + adjustment - avg_contrib * 0.2
    
    # Red herring: modifying dict not used later
    stats['adjustment'] = adjustment
    
    return int(final_rating)

# Key statement
final_score = calculate_rating(contributions, impact_levels)

# Result output
print(f"Result: {final_score}")