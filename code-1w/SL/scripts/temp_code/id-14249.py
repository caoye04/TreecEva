from collections import defaultdict

def calculate_performance(op_count, sys_overhead):
    base_score = sum(op_count.values())
    penalty = 0
    for op, count in op_count.items():
        if count > 10:
            penalty += count * 0.1
    adjusted_score = base_score - penalty - sys_overhead
    return round(adjusted_score / (sys_overhead + 1), 3)

# System operation profiling
timestamps = [1.1, 2.5, 3.7, 4.9]
durations = [0.2, 0.3, 0.5, 0.8]

# Operation types and counts
operations = defaultdict(int)
operation_sequence = ['load', 'fetch', 'load', 'store', 'fetch', 'load', 'store', 'fetch', 'fetch', 'load', 'load', 'fetch']
for op in operation_sequence:
    operations[op] += 1

overhead = len(timestamps) * 0.25

# Irrelevant auxiliary calculation (minor distraction)
peak_utilization = max(durations) * len(durations)

efficiency_ratio = calculate_performance(operations, overhead)
Result: {efficiency_ratio}