baker_scores = [85, 92, 96, 88, 93]
bonus_calculator = lambda score: 10 if score > 90 else 0
total_bonus_points = 0
for score in baker_scores:
    if score > 95:
        break
    total_bonus_points += bonus_calculator(score)
print(f"Result: {total_bonus_points}")