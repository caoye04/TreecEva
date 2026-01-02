def calculate_system_capacity():
    base_levels = [12, 15, 18, 21, 24]
    thresholds = [16, 14, 20, 19, 25]
    mode_flag = True

    # Adjust levels based on threshold comparison using conditional expressions
    adjusted_levels = [
        level * 1.1 if level > threshold else level * 0.9
        for idx, (level, threshold) in enumerate(zip(base_levels, thresholds))
    ]

    # Irrelevant tracking variable (mild distraction)
    status_codes = [200 if lvl > 15 else 404 for lvl in base_levels]

    total_capacity = sum(adjusted_levels)

    # Additional unrelated computation (minor interference)
    avg_status = sum(status_codes) / len(status_codes) if status_codes else 0

    print(f"Result: {total_capacity}")

    return total_capacity

# Execute function
result = calculate_system_capacity()