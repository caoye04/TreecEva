def calculate_performance(activate_bonus):
    base_points = 420
    penalties = 25
    level_multiplier = 3

    # Track event statistics using dictionary
    stats = {
        'attempts': 8,
        'successes': 6,
        'failures': 2
    }

    success_rate = stats['successes'] / stats['attempts']
    efficiency = (base_points - penalties) * level_multiplier

    # Conditional expression based on performance threshold
    performance_bonus = 50 if success_rate >= 0.7 else 20

    # Irrelevant string operation (minor distraction)
    status_msg = "Performance review completed".upper()

    # Final calculation with optional bonus
    raw_score = efficiency + performance_bonus
    final_score = raw_score * 1.1 if activate_bonus else raw_score

    return final_score

# Main execution
bonus_active = True
final_score = calculate_performance(bonus_active)
print(f"Result: {final_score}")