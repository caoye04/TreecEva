from collections import defaultdict

# Simulate system benchmark results across multiple test phases
test_phases = ['startup', 'stress', 'recovery', 'idle']
raw_data = [89, 94, 76, 91]

# Populate phase results using dictionary comprehension
detailed_results = {phase: raw_data[i] for i, phase in enumerate(test_phases)}

# Aggregate additional metrics with defaultdict
trend_data = defaultdict(int)
for phase, score in detailed_results.items():
    trend_data[phase] += score // 10

# Secondary calculation to derive adjusted baseline
baseline = sum(detailed_results.values()) / len(detailed_results)
adjustment_factor = 0.9 if baseline > 85 else 1.1

# Conditional expression used in performance calculation
def calculate_performance(results):
    total = sum(results.values())
    penalty = 15 if any(val < 75 for val in results.values()) else 5
    return int((total - penalty) * adjustment_factor)

# Irrelevant utility function (minor distraction)
def log_event(event):
    timestamp = "2023-07-15"
    return f"[{timestamp}] Event: {event}"

# Key computation
final_score = calculate_performance(detailed_results)

# Logging irrelevant event (distractor at LOW level)
log_event('SYSTEM_INIT')

print(f"Result: {final_score}")