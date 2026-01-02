def analyze_phase(readings):
    adjusted = [x * 0.95 + 2 for x in readings]
    anomalies = [i for i, v in enumerate(adjusted) if v > 90]
    return sum(adjusted) / len(adjusted), anomalies

baseline = [88, 72, 91, 85, 76]
phase_one = [84, 90, 87, 92, 81]
phase_two = [78, 85, 88, 94, 89]

# Misleading computation with dead-end variables
temp_weights = [0.1, 0.2, 0.3, 0.25, 0.15]
dummy_metric = sum(w * idx for idx, w in enumerate(temp_weights))
scaling_factor = dummy_metric * 1.5  # Not actually used later

all_phases = zip(phase_one, phase_two, baseline)
aggregated = []
for idx, (p1, p2, base) in enumerate(all_phases):
    avg_val = (p1 + p2 + base) / 3
    if idx % 2 == 0:
        avg_val *= 1.1
    else:
        avg_val *= 0.95
    aggregated.append(avg_val)

# Simulate noise filtering
filtered_aggregated = [val for val in aggregated if val > 80]

# Secondary distraction: unused transformation chain
transformed = [x ** 0.5 for x in baseline]
normalized = [t / sum(transformed) for t in transformed]
entropy_proxy = sum(-n * n for n in normalized)  # Dead-end calculation

benchmark_data = filtered_aggregated[:]

# Additional irrelevant slicing and manipulation
decoy_slice = benchmark_data[1:3] + [sum(benchmark_data) * 0.1]
shadow_copy = benchmark_data[::-1]

interim_result = 0
for i, val in enumerate(benchmark_data):
    if i == 0:
        interim_result += val * 1.05
    elif i == len(benchmark_data) - 1:
        interim_result += val * 0.95
    else:
        interim_result += val

mean_input = sum(benchmark_data) / len(benchmark_data)
variance = sum((x - mean_input) ** 2 for x in benchmark_data) / len(benchmark_data)
std_dev = variance ** 0.5

z_scores = [(x - mean_input) / std_dev for x in benchmark_data]
valid_z = [z for z in z_scores if abs(z) < 1.5]

# Core logic disguised among distractions
def calculate_performance(data):
    raw_total = sum(data)
    bonus = 10 if len(data) >= 3 else 5
    penalty = 0
    for v in data:
        if v > 90:
            penalty += 2
    return int(raw_total + bonus - penalty)

# Critical execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")