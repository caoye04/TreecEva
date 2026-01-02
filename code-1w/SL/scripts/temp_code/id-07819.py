def analyze_user_session():
    # Simulated user interaction metrics over time
    raw_inputs = [12, 15, 14, 18, 22, 25, 20, 19, 23, 27]
    response_times = [3.2, 2.8, 3.5, 2.1, 1.9, 2.0, 2.4, 2.7, 1.8, 1.6]
    errors = [1, 0, 1, 0, 0, 1, 0, 0, 1, 0]

    # Irrelevant preprocessing: normalize inputs (not used later)
    normalized_inputs = [x / max(raw_inputs) for x in raw_inputs]
    avg_response = sum(response_times) / len(response_times)

    # Key data structures
    metrics_log = {}
    for i in range(len(raw_inputs)):
        key = f"step_{i+1}"
        metrics_log[key] = {
            'input_val': raw_inputs[i],
            'response_time': response_times[i],
            'error': errors[i],
            'efficiency': raw_inputs[i] // (response_times[i] + 0.5)
        }

    # Distractor: unused function
    def calculate_entropy(data):
        from math import log
        total = sum(data)
        probabilities = [x / total for x in data]
        entropy = -sum(p * log(p) for p in probabilities if p > 0)
        return entropy  # Never called

    # Difficulty scaling curve (simulates increasing task complexity)
    difficulty_curve = []
    base_difficulty = 1.0
    for i in range(len(raw_inputs)):
        if i % 3 == 0:
            base_difficulty *= 1.1
        difficulty_curve.append(round(base_difficulty, 2))

    # Auxiliary computation: peak detection (semi-relevant)
    peaks = []
    for i in range(1, len(raw_inputs) - 1):
        if raw_inputs[i] > raw_inputs[i-1] and raw_inputs[i] > raw_inputs[i+1]:
            peaks.append(i)

    # State tracking with tuple unpacking
    total_correct = len(raw_inputs) - sum(errors)
    total_efficiency = sum(rt <= 2.5 for rt in response_times)
    accuracy_rate = total_correct / len(raw_inputs)

    # Core aggregation logic
    def aggregate_performance(log, difficulty_levels):
        scores = []
        adjustment_factor = 0.85

        for step_key, data in log.items():
            base_score = data['input_val'] * (1 - data['error'] * 0.5)
            time_bonus = 5 if data['response_time'] < 2.0 else 2 if data['response_time'] < 3.0 else 0
            efficiency_penalty = data['efficiency'] // 4

            # Apply difficulty scaling
            idx = int(step_key.split('_')[1]) - 1
            scaled_score = (base_score + time_bonus - efficiency_penalty) * difficulty_levels[idx]
            scores.append(scaled_score)

        # Final computation
        raw_sum = sum(scores)
        count = len(scores)
        average_score = raw_sum / count

        # Final non-linear transformation
        final_modifier = 1.1 if accuracy_rate >= 0.7 else 0.9
        return int(average_score * final_modifier)  # Deterministic integer output

    # Dead code path (never executed)
    if False:
        fallback_value = sum(normalized_inputs)
        return fallback_value

    # Critical execution point
    final_score = aggregate_performance(metrics_log, difficulty_curve)
    print(f"Result: {final_score}")
    return final_score

# Execute and capture result
analyze_user_session()