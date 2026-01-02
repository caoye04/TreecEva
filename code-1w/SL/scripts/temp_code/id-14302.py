from itertools import cycle

# Simulate daily work metrics over a 5-day week
daily_hours = [8.5, 7.2, 9.0, 6.5, 10.0]
tasks_completed = [4, 3, 5, 2, 6]
error_count = [1, 0, 2, 1, 3]

# Irrelevant distractor: unused metric
unused_buffer = sum(h ** 0.5 for h in daily_hours if h > 8)

# Helper function to compute efficiency ratio
def calculate_efficiency(hours, tasks):
    if hours == 0:
        return 0
    base_efficiency = tasks / hours
    penalty = 0.1 * sum(1 for t in tasks_completed if t < 3)
    return round(base_efficiency - penalty, 4)

# Compute daily efficiencies
efficiencies = [calculate_efficiency(h, t) for h, t in zip(daily_hours, tasks_completed)]

# Track days with high workload (heuristic)
high_workload_days = 0
for i, hours in enumerate(daily_hours):
    if hours >= 9 and tasks_completed[i] >= 5:
        high_workload_days += 1

# Distractor: complex but unused computation using itertools
cyclic_pattern = cycle([1, -1])
phantom_adjustment = sum(next(cyclic_pattern) * e for i, e in enumerate(efficiencies) if i % 2 == 0)

# Determine productivity score based on trends
productivity = 0
if efficiencies[-1] > efficiencies[0]:
    productivity += 10
if sum(1 for e in efficiencies if e > 0.6) >= 3:
    productivity += 15
if high_workload_days >= 2:
    productivity += 5

# Risk factor from error trends and low-efficiency days
low_efficiency_days = sum(1 for e in efficiencies if e < 0.4)
risk_factor = 0
if error_count[-1] > 2:
    risk_factor += 8
if low_efficiency_days >= 2:
    risk_factor += 12

# Evaluate final performance score
baseline = 100
adjustment = productivity - risk_factor
final_score = baseline + adjustment

# Distractor: redundant transformation
temp_data = [(i, round(e * 10)) for i, e in enumerate(efficiencies)]
sorted_temp = sorted(temp_data, key=lambda x: x[1], reverse=True)

# Final irrelevant operation
cleanup_phase = [x for x in range(len(sorted_temp)) if sorted_temp[x][1] > 4]

print(f"Target result: {final_score}")