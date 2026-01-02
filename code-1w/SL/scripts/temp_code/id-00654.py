from collections import defaultdict

# Simulate a coding competition ranking system with complex scoring logic
def main():
    participants = ['Alice', 'Bob', 'Charlie', 'Diana']
    submissions = [5, 3, 7, 4]
    errors = [2, 1, 3, 0]
    times = [6500, 4200, 8900, 3800]
    active_days = [12, 14, 10, 15]

    # Irrelevant stats (distractors)
    total_submissions = sum(submissions)
    avg_errors = sum(errors) / len(errors)
    peak_performance = max(submissions[i] - errors[i] for i in range(len(submissions)))

    # Scoring mechanism with multiple steps
    base_points = []
    for i in range(len(participants)):
        score = submissions[i] * 10 - errors[i] * 5
        if times[i] < 5000:
            score += 15
        elif times[i] < 7500:
            score += 8
        base_points.append(score)

    # Penalty calculation based on time and consistency
    penalties = []
    consistency_tracker = defaultdict(int)
    for idx, (sub, err) in enumerate(zip(submissions, errors)):
        ratio = err / sub if sub > 0 else 0
        penalty = 0
        if ratio > 0.3:
            penalty += 10
        if times[idx] > 8000:
            penalty += 8
        penalties.append(penalty)

        # Tracking for irrelevant metric
        day_efficiency = sub / max(active_days[idx], 1)
        consistency_tracker[participants[idx]] = round(day_efficiency, 2)

    # Another distraction: analyze submission patterns
    pattern_analysis = {}
    for name, sub in zip(participants, submissions):
        if sub > 4:
            pattern_analysis[name] = 'high_volume'
        elif sub > 2:
            pattern_analysis[name] = 'moderate'
        else:
            pattern_analysis[name] = 'low'

    # Core computation chain
    adjusted_scores = []
    for p, pen in zip(base_points, penalties):
        adjusted = p - pen
        if adjusted > 40:
            adjusted += 5  # bonus for high performance
        adjusted_scores.append(adjusted)

    points = [max(0, s) for s in adjusted_scores]  # ensure non-negative

    # Final ranking calculation (key intervention point)
    def calculate_ranking(pts, pen):
        rank_score = 0
        temp_history = []
        for i, (p, q) in enumerate(zip(pts, pen)):
            contribution = p - q
            if i % 2 == 0:
                contribution *= 1.1
            temp_history.append(round(contribution, 2))
        rank_score = int(sum(temp_history))
        # Normalize by participant count (but not really needed)
        rank_score = rank_score // len(pts)
        return rank_score + 10  # final adjustment

    final_score = calculate_ranking(points, penalties)

    # Dead code path (misleading)
    if False:
        fallback = sum(base_points) // len(base_points)
        final_score = fallback

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()