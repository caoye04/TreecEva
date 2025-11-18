from statistics import median

daily_steps = [8000, 12000, 5000, 10000, 7500, 9000, 11000]
avg_steps = sum(daily_steps) / len(daily_steps)

performance_score = lambda steps: steps - avg_steps
scores = [performance_score(steps) for steps in daily_steps]
scores.sort()

median_score = median(scores)
filtered_scores = list(filter(lambda x: x > median_score, scores))

final_count = len(filtered_scores)
print(f'Result: {final_count}')