def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = 0
    temp_sum = 0
    for log in logs:
        if isinstance(log, str) and 'ERROR' not in log:
            cleaned = log.strip().lower()
            if cleaned.startswith('entry'):
                try:
                    value = int(cleaned.split()[-1])
                    temp_sum += value ** 0.5
                    valid_count += 1
                except ValueError:
                    continue
    return temp_sum / valid_count if valid_count else 0


def track_metrics(data):
    baseline = sum(x * 2 for x in data if x > 0)  
    adjusted = [x + 10 for x in data]
    fake_aggregate = sum(1 for x in adjusted if x % 2 == 0)
    return baseline

logs_data = [
    "Entry 16", "Entry 25", "WARNING: retry", "Entry 9",
    "ERROR: timeout", "Entry 64", "Entry 1"
]

raw_metrics = [3, -1, 4, 0, 5]
productivity = analyze_efficiency(logs_data)
risk_factor = track_metrics(raw_metrics)

intermediate_result = productivity * 2.5
bonus_adjustment = len([x for x in logs_data if 'WARNING' in x])
dummy_calc = (intermediate_result + bonus_adjustment) // 1

final_score = evaluate_performance(productivity, risk_factor)

# Helper function added after usage to simulate oversight
def evaluate_performance(efficiency, base_risk):
    safety_margin = 1.5
    if efficiency > 5:
        base_risk -= 2
    elif efficiency < 3:
        base_risk += 3
    performance_index = efficiency * 10 - base_risk * 2
    return int(performance_index + safety_margin)

# Recompute final_score after definition
final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")