def main():
    # Employee performance data: name -> score
    performance_map = {
        'alice': 85,
        'bob': 90,
        'carol': 78,
        'dave': 92
    }

    # Bonus rules based on performance thresholds
    threshold_rule = lambda x: 1.1 if x >= 90 else (1.05 if x >= 80 else 1.0)

    base_multiplier = 1.0
    bonus_multiplier = {}  
    for name, score in performance_map.items():
        bonus_multiplier[name] = threshold_rule(score)

    extra_buffer = [0] * 5  # Irrelevant preallocation (minor distraction)

    def calculate_total(scores, multipliers):
        total = 0.0
        for name, score in scores.items():
            total += score * multipliers[name]
        return int(total)  # Aggregate boosted scores

    final_score = calculate_total(performance_map, bonus_multiplier)

    # Debug print (not interfering with logic)
    temp_sum = sum(performance_map.values())  # Secondary unused metric

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()