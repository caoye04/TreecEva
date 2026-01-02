def calculate_resilience():
    base_defense = 17
    threat_level = 8
    adaptation_sets = {1, 3, 5, 7, 9, 11}
    vulnerability_exposure = {2, 4, 6, 8, 10}

    active_adaptations = adaptation_sets - vulnerability_exposure
    adaptation_bonus = len(active_adaptations) % 7

    raw_defense = base_defense * 2 - threat_level
    recovery_factor = (raw_defense % 5) ** 2

    interim_defense = raw_defense + adaptation_bonus
    decay_correction = interim_defense // 10
    final_defense = interim_defense - decay_correction * 3

    resilience_score = final_defense if final_defense > 0 else base_defense + recovery_factor
    
    print(f"Target result: {resilience_score}")

calculate_resilience()