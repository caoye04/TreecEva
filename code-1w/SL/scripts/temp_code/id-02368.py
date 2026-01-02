def analyze_efficiency(logs):
    durations = [entry['time'] for entry in logs if entry['active']]
    total_time = sum(durations)
    idle_count = len([entry for entry in logs if not entry['active']])
    efficiency = total_time / (total_time + idle_count * 2) if total_time > 0 else 0
    return efficiency


def evaluate_complexity(items):
    complexity_map = {i: len(str(i)) * 2 for i in range(1, 101)}
    weighted_sum = sum(complexity_map.get(x, 0) for x in items)
    average_complexity = weighted_sum / len(items) if items else 0
    return average_complexity

# Simulated dataset representing task logs and item processing
log_data = [
    {'time': 5, 'active': True},
    {'time': 3, 'active': False},
    {'time': 8, 'active': True},
    {'time': 1, 'active': False},
    {'time': 7, 'active': True}
]

item_list = [12, 45, 67, 89, 23, 34, 56, 78]

# Misleading distraction: unused function
def calculate_latency(peaks):
    if not peaks:
        return 0
    peak_diffs = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    return sum(peak_diffs) / len(peak_diffs)

# Irrelevant preprocessing
processed_items = [x for x in item_list if x % 2 == 0]  # Only evens
item_squares = {x: x**2 for x in processed_items}

# Core variables
productivity = analyze_efficiency(log_data)
sample_peaks = [10, 20, 30]
useless_metric = calculate_latency(sample_peaks)  # Dead-end computation

errors = len([x for x in log_data if not x['active']])
complexity_factor = evaluate_complexity(item_list)

# Key statement with distractors around it
intermediate_result = productivity * (1 + complexity_factor / 10)
adjustment = 0.95 if errors < 3 else 0.85
final_score = evaluate_performance(productivity, errors)

# Another irrelevant block
if adjustment < 0.9:
    buffer_zone = [i for i in range(errors * 2)]
    buffer_sum = sum(buffer_zone)

print(f"Result: {final_score}")

def evaluate_performance(output_rate, defect_count):
    base = output_rate * 100
    penalty = defect_count * 8.5
    bonus = 5 if defect_count == 0 else 0
    return base - penalty + bonus