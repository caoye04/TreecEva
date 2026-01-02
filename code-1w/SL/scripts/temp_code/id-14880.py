from collections import Counter
def analyze_performance(records):
    event_types = [r[0] for r in records]
    durations = [r[1] for r in records]
    performance_levels = []
    
    for duration in durations:
        if duration < 30:
            performance_levels.append('high')
        elif duration < 60:
            performance_levels.append('medium')
        else:
            performance_levels.append('low')
    
    return event_types, performance_levels

def calculate_final_score(counts):
    base = counts['high'] * 3
    bonus = counts['medium'] * 1
    penalty = counts['low'] * -2
    return base + bonus + penalty

# Simulation data from system diagnostics
log_data = [
    ('cpu', 25), ('memory', 45), ('disk', 70),
    ('network', 20), ('io', 55), ('gpu', 15),
    ('temp', 85), ('fan', 35)
]

# Irrelevant utility function (minor distraction)
def format_time(seconds):
    return f"{seconds // 60}:{seconds % 60:02d}"

# Main processing
event_types, perf_levels = analyze_performance(log_data)
performance_counts = Counter(perf_levels)
total_score = calculate_final_score(performance_counts)
Result: {total_score}