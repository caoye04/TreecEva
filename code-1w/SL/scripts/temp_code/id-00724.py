def assess_system_state():
    status_codes = [1, 0, 1, 1, 0, 1]
    diagnostic_scores = [32, 45, 67, 89, 56, 74, 38]
    system_active = sum(status_codes) > 3

    # Irrelevant auxiliary calculation (distractor)
    baseline = len(diagnostic_scores) // 2
    temp_factor = diagnostic_scores[baseline] * 0.5

    # Key logic with conditional expression and slicing
    energy_level = sum(diagnostic_scores[i] for i in range(0, len(diagnostic_scores), 2))
    energy_threshold = max(diagnostic_scores[2:5]) if system_active else sum(diagnostic_scores[:3])

    # Additional benign operation (minimal interference)
    adjustment = 1 if energy_level & 1 else -1
    energy_threshold += adjustment

    print(f"Result: {energy_threshold}")

assess_system_state()