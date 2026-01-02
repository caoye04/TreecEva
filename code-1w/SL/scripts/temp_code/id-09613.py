def aggregate_performance(feedback, metrics):
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}
    adjustment_factor = sum(normalized.values())

    # Core logic begins
    valid_feedback = {f for f in feedback if f.startswith('P')}
    bonus_weights = {k: len(k) * 1.5 for k in metrics.keys()}

    # Misleading intermediate calculation (not used in final result)
    phantom_score = adjustment_factor * 0.7 + len(normalized) ** 2

    # Key computation path
    base_sum = sum(metrics.values())
    feedback_modifier = len(valid_feedback) if len(valid_feedback) > 0 else -1

    # Conditional expression usage
    scaling = 1.2 if feedback_modifier >= 2 else 0.8

    # Set operations: symmetric difference to detect anomalies
    expected_labels = {'P1', 'P2', 'P3', 'P4'}
    missing = expected_labels.symmetric_difference(valid_feedback)
    completeness_bonus = 10 if not missing else -5 * len(missing)

    # Multiple concepts: dict lookup, set logic, conditional scaling
    performance_peak = max(metrics.values())
    stability_penalty = len([v for v in metrics.values() if v < 50]) * 3

    # Final aggregation with irrelevant terms filtered out
    raw_score = base_sum * scaling + feedback_modifier * 7 + completeness_bonus
    final_score = int(raw_score - stability_penalty)  # Deterministic integer result

    # Dead code path (never executed but adds cognitive load)
    if False:
        debug_trace = [phantom_score, adjustment_factor]
        final_score += len(debug_trace)

    return final_score

# Initial data setup
base_metrics = {'throughput': 85, 'latency': 45, 'accuracy': 92, 'energy': 67}
feedback_set = ['P1', 'P3', 'X9', 'P4', 'Z2']

# Execution point of interest
final_score = aggregate_performance(feedback_set, base_metrics)
print(f"Result: {final_score}")