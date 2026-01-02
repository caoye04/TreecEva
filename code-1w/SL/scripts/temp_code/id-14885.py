def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    for log in logs:
        entries = log.split(',')
        daily_hours = sum(float(e.split(':')[1]) for e in entries if 'work' in e)
        if daily_hours < 2.0:
            idle_count += 1
        total_hours += daily_hours
    efficiency = total_hours / len(logs) if logs else 0
    return efficiency, idle_count

logs_data = [
    'start:0.5,work:2.5,break:1.0,work:3.2,end:0.3',
    'start:0.4,work:1.8,break:0.5,work:4.0,end:0.2',
    'start:0.6,work:3.0,break:0.7,work:2.1,end:0.1',
    'start:0.3,work:0.9,break:0.5,work:1.5,end:0.4'
]

# Irrelevant preprocessing
processed_logs = [log.replace('start', 'init').replace('end', 'term') for log in logs_data]
dummy_analysis = [len(log.split(',')) for log in processed_logs]

# Real computation begins
base_efficiency, inactive_days = analyze_productivity(logs_data)

# Simulate contribution tracking
contributions = []
for i in range(1, 6):
    trend = (base_efficiency * i) % 2.5
    normalized = round(trend + (5 - i) * 0.3, 2)
    contributions.append(normalized)

# Distractor: unused helper
def smooth_data(seq):
    return [sum(seq[max(0,i-1):i+1])/(i+1) for i in range(len(seq))]

# Simulate performance penalties
penalty_factor = 0.85
if inactive_days > 1:
    penalty_factor -= 0.05 * (inactive_days - 1)

extra_buffer = [x * 0.1 for x in contributions]  # Unused

# Core rating logic
recent_boost = sum(c for c in contributions[-2:]) * 0.5
adjusted_base = sum(contributions) * base_efficiency

# Final calculation
final_score = 0
def calculate_rating(contribs, penalty):
    raw = sum(contribs) * penalty
    bonus = recent_boost * 1.2 if raw > 6 else 0
    return int(raw + bonus)

final_score = calculate_rating(contributions, penalty_factor)
print(f"Target result: {final_score}")