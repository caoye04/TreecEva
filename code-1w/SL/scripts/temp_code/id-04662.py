def main():
    # Simulate student assessment scoring with adaptive difficulty
    raw_scores = [85, 92, 78, 96, 88]
    max_possible = 100
    difficulty_levels = [1.0, 1.1, 0.9, 1.3, 1.05]
    time_spent_seconds = [450, 500, 400, 600, 520]
    penalties = [0, 5, 0, 10, 0]  # Late submission penalties

    # Irrelevant distraction: Normalize time spent (not used in final score)
    total_time = sum(time_spent_seconds)
    normalized_times = [t / total_time for t in time_spent_seconds]
    avg_time = total_time / len(time_spent_seconds)

    # Distractor: Compute efficiency ratio (unused)
    efficiency_ratio = list(map(lambda x: x[0]/x[1], zip(raw_scores, time_spent_seconds)))

    # Actual core data
    assessments = []
    for i in range(len(raw_scores)):
        adjusted = (raw_scores[i] - penalties[i]) / max_possible
        scaled_score = adjusted * difficulty_levels[i]
        assessments.append(scaled_score)

    # More distraction: simulate confidence levels (unused)
    confidence_levels = []
    for s in raw_scores:
        if s > 90:
            conf = 0.95
        elif s > 80:
            conf = 0.85
        else:
            conf = 0.7
        confidence_levels.append(conf)

    baseline_confidence = sum(confidence_levels) / len(confidence_levels)

    # Difficulty curve transformation (only some points affect final)
    def difficulty_curve(x):
        if x < 1.0:
            return x * 1.1
        elif x >= 1.3:
            return x * 0.9
        else:
            return x

    # Core logic: aggregate performance
    def aggregate_performance(scores, curve_func):
        transformed = [curve_func(s) for s in scores]
        filtered = [s for s in transformed if s >= 0.8]  # Only strong performances count
        if len(filtered) == 0:
            return 0.0
        # Final score is the average of filtered, scaled back to 100-point scale
        return round((sum(filtered) / len(filtered)) * 100, 2)

    intermediate_avg = sum(assessments) / len(assessments)  # distractor

    # Key computation point
    final_score = aggregate_performance(assessments, difficulty_curve)

    # Additional red herring: unused bonus calculation
    peak_score = max(assessments)
    bonus_awarded = peak_score > 1.0
    multiplier = 1.05 if bonus_awarded else 1.0

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()