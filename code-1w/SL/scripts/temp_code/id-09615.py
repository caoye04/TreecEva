def evaluate_performance(metrics):
    base_score = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0

    # Irrelevant tracking variables (distractors)
    debug_log = []
    temp_result_cache = {}
    cycle_counter = 0

    metric_set = set(metrics)
    essential_metrics = {"latency", "throughput", "accuracy", "energy_efficiency"}
    optional_metrics = {"memory_usage", "cpu_load", "disk_io"}

    # Partial overlap check - only certain combinations matter
    present_essentials = metric_set & essential_metrics
    present_optionals = metric_set & optional_metrics

    # Core scoring logic
    if len(present_essentials) >= 3:
        base_score += 40
        if "accuracy" in present_essentials:
            base_score += 25
            if "latency" in present_essentials and metrics["latency"] < 50:
                bonus_multiplier *= 1.2

    # Complex conditional with early exit red herring
    for opt in present_optionals:
        if opt == "memory_usage" and metrics.get("memory_usage", 100) > 80:
            penalty_adjustment -= 10
        elif opt == "cpu_load" and metrics.get("cpu_load", 0) > 90:
            penalty_adjustment -= 15
        else:
            # Dead code path: never reached due to prior conditions
            temp_result_cache[opt] = "low_risk"

    # Irrelevant computation chain (distractor)
    intermediate_sum = 0
    for i in range(3):
        intermediate_sum += i * 10
        debug_log.append(f"step_{i}: {intermediate_sum}")

    # Secondary evaluation branch with misleading influence
    stability_check = len(present_optionals) >= 2
    if stability_check:
        base_score += 10

    # Final score computed from core logic
    final_score = int((base_score + penalty_adjustment) * bonus_multiplier)

    # Redundant state update (not affecting result)
    cycle_counter += 1
    if cycle_counter == 1:
        debug_log.append("initialization_complete")

    return final_score

# Input data
system_metrics = {
    "latency": 45,
    "throughput": 1200,
    "accuracy": 0.97,
    "energy_efficiency": True,
    "memory_usage": 85,
    "disk_io": 60
}

# Execution point
final_score = evaluate_performance(system_metrics)
print(f"Result: {final_score}")