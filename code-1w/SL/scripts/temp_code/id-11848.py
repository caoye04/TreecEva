def analyze_performance(scores, thresholds):
    above_threshold = [s for s in scores if s >= thresholds[0]]
    below_floor = [s for s in scores if s < thresholds[1]]
    count_high = len(above_threshold)
    count_low = len(below_floor)

    base_score = sum(scores) // len(scores)
    bonus = count_high * 3
    penalty = count_low * 2

    intermediate = base_score + bonus - penalty

    adjustments = []
    for idx, val in enumerate(above_threshold):
        if val % 2 == 0:
            adjustments.append(val // (idx + 1) if idx != 0 else val)
    net_adjustment = sum(adjustments)

    total_score = intermediate + net_adjustment

    def final_adjustment(score):
        return score + (score % 11) // 2

    total_score = final_adjustment(total_score)

    # Irrelevant tracking variable (minor distraction)
    status_flags = {"valid": True, "reviewed": False}
    return total_score

scores_input = [85, 92, 78, 64, 90, 50, 88]
thresholds_input = (80, 60)
result = analyze_performance(scores_input, thresholds_input)
print(f"Result: {result}")