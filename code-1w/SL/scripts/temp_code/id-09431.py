def main():
    base_scores = [85, 90, 78, 92]
    weight_factor = 1.1
    adjustment = 5

    # Irrelevant distraction: unused variable
    temp_offset = 3.5

    bonus_fn = lambda x: x * 0.1 if x >= 90 else 0

    def calculate_total(bonus_func, scores):
        total = 0
        for score in scores:
            if score >= 80:
                raw_bonus = bonus_func(score)
                total += score + raw_bonus
        return int(total * weight_factor)

    final_score = calculate_total(bonus_fn, base_scores)
    print(f"Result: {final_score}")

main()