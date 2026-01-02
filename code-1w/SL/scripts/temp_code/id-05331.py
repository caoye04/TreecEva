def calculate_performance(times, base):
    avg_time = sum(times) / len(times)
    adjusted = list(map(lambda t: t * 0.9 if t > avg_time else t * 1.1, times))
    performance_ratio = base / min(adjusted)
    return round(performance_ratio, 3)

# System run times in milliseconds
run_times = [120, 150, 130, 110, 140]
overhead = 500

# Irrelevant auxiliary data (minor distraction)
data_logs = ['log1', 'log2']
metadata_index = len(data_logs)

# Key computation
efficiency_score = calculate_performance(run_times, overhead)

Result: efficiency_score