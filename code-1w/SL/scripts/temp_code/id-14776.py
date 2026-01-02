def main():
    # Simulated health monitoring system
    heart_rate = [72, 75, 80, 68, 90, 95, 88, 77]
    activity_levels = [3000, 5000, 7000, 2000, 1000, 800, 4500, 6000]
    sleep_hours = [7.2, 6.5, 5.8, 8.0, 6.7, 5.5, 7.0, 6.3]

    # Irrelevant derived metrics (distractors)
    avg_heart_rate = sum(heart_rate) / len(heart_rate)
    total_steps = sum(activity_levels)
    max_sleep = max(sleep_hours)
    min_activity = min(activity_levels)

    # More distractions: unused transformation
    normalized_rates = [round((hr - 60) / 30, 2) for hr in heart_rate if hr > 60]
    sleep_efficiency = list(map(lambda x: round(x * 0.95 + 0.2, 2), sleep_hours))

    # Key data structure
    health_data = {
        'rates': heart_rate,
        'activity': activity_levels,
        'sleep': sleep_hours
    }

    # Threshold logic with lambda
    threshold_func = lambda x: x > 70

    # Unused helper function (dead code path)
    def analyze_risk(data):
        high_risk = 0
        for val in data['rates']:
            if val > 90:
                high_risk += 1
        return high_risk  # never called

    # Secondary distraction: intermediate aggregation
    activity_sum = 0
    for i, act in enumerate(activity_levels):
        if act > 4000:
            activity_sum += (i + 1) * 100  # position-weighted sum, not used

    # Core logic chain
    valid_days = 0
    for i in range(len(health_data['rates'])):
        hr_condition = health_data['rates'][i] > 70
        act_condition = health_data['activity'][i] > 4000
        sleep_condition = health_data['sleep'][i] >= 6.0

        if hr_condition and act_condition and sleep_condition:
            valid_days += 1

    # Process metrics uses lambda and combines conditions
    def process_metrics(data, func):
        score = 0
        bonus = 0
        for i in range(len(data['rates'])):
            if func(data['rates'][i]):
                score += 1
            if data['sleep'][i] < 6.0:
                score -= 0.5
            if i % 2 == 0 and data['activity'][i] > 5000:
                bonus += 1
        return int(score + bonus)

    final_score = process_metrics(health_data, threshold_func)

    # Additional irrelevant computation
    daily_variability = [abs(heart_rate[i] - heart_rate[i-1]) for i in range(1, len(heart_rate))]
    stability_index = 100 - sum(daily_variability)

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()