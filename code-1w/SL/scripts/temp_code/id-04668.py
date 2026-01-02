from collections import defaultdict

# Simulate system diagnostics with performance metrics
def analyze_system_logs(log_entries):
    stats = defaultdict(int)
    error_flags = []
    efficiency = 0.0
    total_ops = 0
    failed_ops = 0

    for entry in log_entries:
        parts = entry.split('|')
        level = parts[1].strip()
        message = parts[2].strip()

        stats[level] += 1

        if 'ERROR' in level:
            failed_ops += 1
            error_flags.append(message)
        elif 'WARNING' in level:
            stats['issues_resolved'] += 1  # semi-relevant tracking

        if 'CPU' in message or 'MEMORY' in message:
            total_ops += 1

    # Irrelevant summary computation (distractor)
    summary_code = len(error_flags) * 3 + sum(1 for s in stats if 'ERR' in s)

    # Core efficiency calculation
    if total_ops > 0:
        efficiency = (total_ops - failed_ops) / total_ops
    else:
        efficiency = 0.5

    # Dummy transformation (distraction)
    adjusted_efficiency = efficiency * 1.1 if efficiency < 0.8 else efficiency
    adjusted_efficiency = min(adjusted_efficiency, 1.0)

    return efficiency, stats, error_flags

# Evaluate human-readable performance tier
def evaluate_performance(eff, errs, warns):
    base_score = int(eff * 100)
    penalty = len(errs) * 5 + len(warns) // 3
    bonus = 0

    if eff > 0.85:
        bonus += 10
    elif eff > 0.7:
        bonus += 5

    # Complex conditional bonus logic (partially dead code)
    if len(errs) == 0 and eff > 0.9:
        bonus += 7
    else:
        shadow_buffer = [i**2 for i in range(len(warns))]  # unused list

    return base_score + bonus - penalty

# Main execution
log_data = [
    "ID1|ERROR  | Disk failure detected",
    "ID2|INFO   | System startup",
    "ID3|WARNING| High CPU load",
    "ID4|ERROR  | Timeout on request",
    "ID5|INFO   | User login",
    "ID6|WARNING| Memory threshold exceeded",
    "ID7|INFO   | CPU temperature stable",
    "ID8|INFO   | Network connected"
]

# Analyze logs
efficiency_metric, log_stats, error_list = analyze_system_logs(log_data)
warning_count = log_stats['WARNING']

# Compute final score (target execution point)
final_score = evaluate_performance(efficiency_metric, error_list, warning_count)

# Print result
print(f"Result: {final_score}")