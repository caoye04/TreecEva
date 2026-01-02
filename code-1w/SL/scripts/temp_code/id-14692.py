def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    for log in logs:
        if 'ERROR' in log.upper():
            continue
        cleaned = log.strip().lower()
        if cleaned.startswith('task'):
            valid_count += 1
            length_factor = len(cleaned) % 7
            temp_sum += length_factor
    return temp_sum if valid_count > 0 else 0

logs_data = [
    "  TaskA completed successfully  ",
    "WARNING: minor issue detected",
    "  taskB failed initial check  ",
    "INFO: system running smoothly",
    "  TaskC ready for deployment  ",
    "ERROR: critical failure in module X",
    "  taskD executed without errors  ",
    "debug: variable x has value 42"
]

baseline = sum([len(log) for log in logs_data if ' ' in log]) // 3
redundant_calc = pow(2, 3) * len([l for l in logs_data if l.islower()])
productivity = analyze_efficiency(logs_data)

# Simulate error tracking (some irrelevant filtering)
error_flags = []
for entry in logs_data:
    status = entry.split()[-1].upper()
    if status in ['FAILED', 'FAILURE', 'ERROR']:
        error_flags.append(True)
    else:
        error_flags.append(False)

false_alarms = [not flag for flag in error_flags if flag == False][:2]
errors = sum(error_flags)

# Dummy string processing to increase cognitive load
summary = "Performance summary:\n" + "-"*20
summary_lines = summary.split("\n")
summary_clean = summary.lower().replace("summary", "report")

# Core logic disguised among auxiliary computations
def evaluate_performance(output, faults):
    efficiency_ratio = output / (faults + 1) if faults > 0 else output
    penalty = 0
    if output < 10:
        penalty = 5
    elif output >= 10:
        bonus = 3  # unused dead code path (distractor)
    score = (output * 7) - (penalty * faults)
    return int(score)

intermediate_result = productivity + baseline - redundant_calc
final_score = evaluate_performance(productivity, errors)
print(f"Result: {final_score}")