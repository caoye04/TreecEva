from collections import defaultdict

# Simulate employee performance analytics with noise and distractors
def analyze_productivity(logs):
    counts = defaultdict(int)
    total_entries = 0
    invalid_flag = False

    for entry in logs:
        action, duration = entry.split(':')
        time_val = int(duration)
        counts[action] += time_val
        total_entries += 1

        if time_val < 0:
            invalid_flag = True

    # Distractor computation: irrelevant to final score
    avg_entry_length = sum(len(entry) for entry in logs) / len(logs) if logs else 0
    complexity_proxy = avg_entry_length ** 0.5

    return dict(counts), total_entries, complexity_proxy


def calculate_risk(metrics):
    base_risk = metrics.get('errors', 0) * 1.5
    latency_penalty = metrics.get('latency', 0) * 0.1
    temp_debug = base_risk + latency_penalty + 5  # red herring

    # Conditional expression used (required feature)
    adjustment = 2.0 if metrics.get('stability', 10) < 5 else 0.5

    final_risk = (base_risk + latency_penalty) * adjustment

    # Dead code path (distractor)
    if False:
        final_risk -= temp_debug % 7

    return final_risk


def evaluate_performance(stats, risk):
    focus_time = stats.get('focus', 0)
    meetings = stats.get('meeting', 0)
    breaks = stats.get('break', 0)

    # Real logic: productivity score based on focused work minus risk factor
    raw_score = focus_time - meetings * 0.5 - breaks * 0.3
    normalized = max(raw_score, 0)

    # Key formula
    performance_index = normalized * (100 / (1 + risk))

    # Intermediate irrelevant transformation
    capped_index = min(performance_index, 95) if risk > 1 else performance_index

    return int(capped_index)

# Main execution
if __name__ == "__main__":
    # Input data: simulated work log entries
    work_log = [
        "focus:45", "meeting:30", "focus:60", "break:15",
        "focus:30", "errors:5", "latency:200"
    ]

    # Parse logs (only some fields are relevant)
    parsed_stats, total, proxy = analyze_productivity(
        [e for e in work_log if ':' in e and e.split(':')[0] in ['focus', 'meeting', 'break']]
    )

    # Build metrics for risk (distractor keys included)
    telemetry = {
        'errors': 5,
        'latency': 200,
        'stability': 7,
        'memory_usage': 450,  # irrelevant
        'cpu_spike_count': 3   # irrelevant
    }

    risk_factor = calculate_risk(telemetry)

    # Core evaluation point
    final_score = evaluate_performance(parsed_stats, risk_factor)

    # Additional noise
    audit_trail = []
    audit_trail.append(f'Score computed at {final_score}')
    metadata_summary = {"entries": total, "risk": round(risk_factor, 2)}

    # Output result as required
    print(f"Result: {final_score}")