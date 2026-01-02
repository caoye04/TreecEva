def analyze_efficiency(logs):
    total_chars = sum(map(len, logs))
    entry_count = len(logs)
    avg_length = total_chars / entry_count if entry_count else 0

    # Irrelevant transformation (distractor)
    transformed = list(map(lambda x: x.upper()[::-1], logs))
    dummy_sum = sum(ord(transformed[0][i]) for i in range(len(transformed[0])) if i % 2 == 0) if transformed else 0

    return avg_length

# Simulated system logs (distractor input)
system_logs = ['init: boot', 'proc: running', 'error: disk', 'status: ok']
baseline = analyze_efficiency(system_logs)

# Core productivity data
tasks_completed = [8, 12, 5, 17, 9]
errors = [2, 4, 1, 6, 3]

# Weighted scoring with conditional adjustment
weights = [1.5 if t > 10 else 1.0 for t in tasks_completed]
productivity = sum(t * w for t, w in zip(tasks_completed, weights))

# Secondary metric (semi-relevant but not used directly)
completion_rate = len([t for t in tasks_completed if t >= 5]) / len(tasks_completed)
penalty_factor = 0.9 if completion_rate > 0.6 else 0.7

# Helper function with recursion (simple recursion paradigm)
def recursive_bonus(n):
    return 1 if n <= 1 else n * 0.1 + recursive_bonus(n - 1)

# Apply bonus based on max task (distraction: small effect)
basic_bonus = recursive_bonus(max(tasks_completed))
adjusted_productivity = productivity + basic_bonus

# Core evaluation logic
def evaluate_performance(prod, errs):
    base = prod - sum(errs) * 2.5
    # Conditional expression (required python feature)
    multiplier = 1.2 if any(e >= 5 for e in errs) else 1.4
    return int(base * multiplier)  # Final deterministic integer result

# Key statement
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")