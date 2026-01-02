def analyze_trend(data, base):
    trend = 0
    adjustment = 0
    temp_sum = 0
    for val in data:
        if val > base + 5:
            trend += 1
        elif val < base - 5:
            trend -= 1
        temp_sum += val % 3
    correction = temp_sum / len(data) if data else 0
    return trend, correction

metrics = [12, 15, 9, 6, 14, 11, 8]
baseline = 10
trend_score, noise = analyze_trend(metrics, baseline)

redundant_calc = sum(x ** 0.5 for x in metrics if x % 2 == 0)
buffer_value = (redundant_calc * 0.7) // 1

threshold = 3

secondary_data = [abs(x - baseline) for x in metrics]
outlier_count = 0
for diff in secondary_data:
    if diff > threshold:
        outlier_count += 1

status_flag = 'stable' if trend_score > 0 else 'declining'

hypothetical_shift = [x - 1 if x > baseline else x + 1 for x in metrics]
post_shift_trend, _ = analyze_trend(hypothetical_shift, baseline)

adjusted_outliers = outlier_count - (1 if status_flag == 'declining' else 0)

penalty_factor = 2 if adjusted_outliers > 4 else 1

utility_score = sum(1 for x in metrics if x >= baseline) - penalty_factor * abs(trend_score)

scaling_constant = 1.5 if post_shift_trend > trend_score else 1.0

interim = utility_score * scaling_constant + noise

evaluate_performance = lambda m, t: (
    int(interim * 10) 
    if len([x for x in m if x > t]) > len(m) // 2 + 1 
    else int(interim * 5)
)

final_score = evaluate_performance(metrics, threshold)
print(f"Target result: {final_score}")