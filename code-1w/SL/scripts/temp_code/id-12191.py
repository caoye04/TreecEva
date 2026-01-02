from itertools import compress

def analyze_efficiency(logs):
    durations = [len(log.strip()) for log in logs]
    valid_logs = [d > 0 for d in durations]
    filtered = list(compress(durations, valid_logs))
    total_time = sum(filtered)
    entry_count = len(filtered)
    average_time = total_time / entry_count if entry_count else 0
    efficiency_score = (average_time * 1.5) if average_time < 10 else (average_time * 0.8)
    return efficiency_score

logs_data = [
    '   task completed ',
    'error: retrying...',
    'update applied',
    '',
    'finalizing workflow  '
]

raw_string = "performance_metrics_v2"
version_number = int(raw_string[-1])
baseline_offset = version_number * 2.5

productivity = analyze_efficiency(logs_data)

# Simulate risk adjustment with string-based flag
data_sensitivity = "HIGH_SECURITY"
flag_active = "SECURITY" in data_sensitivity and len(data_sensitivity) % 2 == 0
risk_penalty = 15 if flag_active else 7

staging_weight = 0.9
risk_factor = risk_penalty * staging_weight

# Dummy computation - irrelevant to final result
temp_buffer = [x for x in range(1, 10) if x % 3 == 0]
buffer_sum = sum(temp_buffer)
dummy_metric = buffer_sum * 0.1

extra_noise = set([1, 2, 3]) | set([3, 4, 5])
element_count = len(extra_noise)
shadow_factor = element_count * 2.2  # Unused distraction

interim_result = productivity + 5.5
scaling_constant = 3.7
final_score = evaluate_performance(interim_result, risk_factor) if 'evaluate_performance' in globals() else interim_result * 0.5

# Redefine function after usage attempt (correct order now)
def evaluate_performance(efficiency, risk):
    adjusted = efficiency - risk
    bonus = 10 if efficiency >= 8 else 0
    return adjusted + bonus

# Recompute final_score with correct function available
final_score = evaluate_performance(interim_result, risk_factor)

print(f"Result: {final_score}")