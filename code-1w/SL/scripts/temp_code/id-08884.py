def evaluate_performance(metrics, apply_bonus):
    base_weight = 0.8
    bonus_multiplier = 1.5 if apply_bonus else 1.0
    penalty_factor = 0.9
    temp_adjustment = 0.0

    # Irrelevant temperature simulation (distractor)
    for i in range(3):
        temp_adjustment += 0.1 * (i + 1)
    temp_adjustment = round(temp_adjustment, 2)  # Unused later

    # Real metric processing
    accuracy = metrics.get('accuracy', 0)
    precision = metrics.get('precision', 0)
    recall = metrics.get('recall', 0)
    f1_component = 2 * precision * recall
    f1_denom = (precision + recall) if (precision + recall) != 0 else 1
    computed_f1 = f1_component / f1_denom

    # Secondary distractor: string-based status tracking (semi-relevant)
    status_log = []
    if accuracy > 0.85:
        status_log.append("high_accuracy")
    if computed_f1 > 0.75:
        status_log.append("strong_f1")
    status_summary = "|".join(status_log).upper()  # Not used in score

    # Dictionary transformation (red herring)
    transformed_metrics = {k.upper(): round(v * 100, 1) for k, v in metrics.items()}
    transformed_metrics['F1_SCORE'] = round(computed_f1 * 100, 1)

    # Core scoring logic
    raw_score = base_weight * accuracy + (1 - base_weight) * computed_f1
    if apply_bonus and accuracy > 0.8:
        raw_score *= bonus_multiplier
    if recall < 0.6:
        raw_score *= penalty_factor

    # Final adjustment using integer division and modulus (modular arithmetic)
    signal_strength = len(status_log) * 10 + (hash(status_summary) % 7 if status_summary else 0)
    signal_penalty = 0.05 if signal_strength < 15 else 0.0
    adjusted_score = raw_score - signal_penalty

    # Normalize to percentage-like scale and cap
    final_score = int(adjusted_score * 1000) // 10  # Integer division

    # Additional dead code path (irrelevant function call)
    def debug_prints():
        print(f"Temp Adjustment: {temp_adjustment}")
        print(f"Transformed Metrics: {transformed_metrics}")
        print(f"Signal Strength: {signal_strength}")

    return final_score

# Input data
metric_data = {
    'accuracy': 0.88,
    'precision': 0.78,
    'recall': 0.72
}
bonus_enabled = True

# Execution point
final_score = evaluate_performance(metric_data, bonus_enabled)
print(f"Result: {final_score}")