def analyze_data(logs):
    # Irrelevant preprocessing (distractor)
    cleaned = [x for x in logs if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    stats = {"mean": sum(normalized) / len(normalized), "count": len(normalized)}

    # Decoy function that looks important but isn't used
    def calculate_risk(data):
        return sum((i * val) ** 0.5 for i, val in enumerate(data)) % 7

    # Unused transformation
    transformed = list(map(lambda x: (x * 2) ** 0.3, normalized))

    # Real logic begins — performance metrics from system telemetry
    metrics = [
        len(logs) % 13,                    # metric_0: log count modulo
        sum(x % 3 for x in logs),           # metric_1: residue sum
        max(logs) - min(logs),              # metric_2: range
        sum(1 for x in logs if x & 1),      # metric_3: odd count
        sum(a * b for a, b in zip(logs, logs[1:]))  # metric_4: adjacent product sum
    ]

    # Weight vector with red herring elements
    all_weights = [0.1, 0.25, 0.15, 0.3, 0.2, 0.05, 0.1]
    # Only first 5 are actually used
    weights = all_weights[:5]

    # Misleading intermediate calculation
    temp_result = sum(metrics[i] * all_weights[i+2] for i in range(3))  # uses wrong indices

    # Another decoy structure
    audit_trail = []
    for idx, m in enumerate(metrics):
        if m > 5:
            audit_trail.append(f"Flagged M{idx}")
        else:
            audit_trail.append(f"Normal M{idx}")

    # Core evaluation logic (uses lambda and zip as required)
    def evaluate_performance(mets, wts):
        # Apply weighted scoring with nonlinear boost for high metrics
        boosted = [(m + 1) ** 0.5 for m in mets]
        weighted_sum = sum(w * b for w, b in zip(wts, boosted))
        penalty = 0
        for i, m in enumerate(mets):
            if i % 2 == 1 and m < 4:
                penalty += 2.5
        return int(weighted_sum * 10 - penalty)  # Scale and adjust

    # Dead code path — looks like it might affect result
    if len(metrics) > 10:
        fallback = sum(metrics) // 2
    elif any(w < 0 for w in weights):
        fallback = -999
    else:
        fallback = None  # never used

    # Key assignment statement
    final_score = evaluate_performance(metrics, weights)

    # Print result as required
    print(f"Result: {final_score}")

    # Extra noise: unused list comprehension
    _ = [x for x in range(len(logs)) if x % 4 == 0 and logs[x] % 2 == 1]

    return final_score

# Simulated input data (deterministic)
data_log = [5, 8, 3, 12, 7, 4, 9]

# Execute
analyze_data(data_log)