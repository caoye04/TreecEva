def calculate_final_score(records, importance):
    base_total = 0
    bonus_factor = 0.0
    penalty_count = 0
    temp_result = []
    intermediate_sum = 0  # Irrelevant tracking

    for i, (value, weight) in enumerate(zip(records, importance)):
        if i % 2 == 0:
            base_total += value * weight
            temp_result.append(value ** 0.5)
        else:
            adjusted = value + (1 if value > 50 else -1)
            intermediate_sum += adjusted  # Distractor accumulation
            if adjusted > 75:
                bonus_factor += 0.1

    outlier_check = [x for x in records if x > 90]  # Dead code path, not used
    if len(outlier_check) > 2:
        bonus_factor *= 0.5  # Never reached with current data

    compression_ratio = sum(temp_result) / len(temp_result) if temp_result else 1  # Misleading metric

    # Core logic hidden among distractions
    final_score = base_total * (1 + bonus_factor)

    # Additional red herring computations
    normalized_data = [(x - min(records)) / (max(records) - min(records)) for x in records]
    entropy_approx = 0
    for p in normalized_data:
        if p > 0:
            entropy_approx -= p * __import__('math').log(p)  # Complex but irrelevant

    return int(final_score)

# Input data
measurements = [85, 45, 70, 60, 95]
coefficients = [1.2, 0.8, 1.0, 0.9, 1.1]

# Execute main logic
target_result = calculate_final_score(measurements, coefficients)
print(f"Result: {target_result}")