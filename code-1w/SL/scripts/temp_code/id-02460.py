def main():
    # Initial dataset representing student test scores and attendance
    raw_scores = [85, 90, 78, 92, 88]
    attendance_rate = [0.95, 0.87, 0.90, 0.93, 0.82]

    # Thresholds for performance evaluation
    passing_score = 80
    min_attendance = 0.85

    # Irrelevant transformation: reverse and scale (not used in final logic)
    reversed_scaled = [x * 1.1 for x in reversed(raw_scores)]
    temp_analysis = sum(reversed_scaled) / len(reversed_scaled)

    # Mapping function to normalize scores to 0-1 scale
    normalize = lambda x: x / 100.0
    normalized_scores = list(map(normalize, raw_scores))

    # Simulating data corruption check (distractor)
    checksum = sum([int(s * 100) for s in normalized_scores]) % 7

    # Combine score and attendance into tuples
    student_data = [(s, a) for s, a in zip(normalized_scores, attendance_rate)]

    # Apply filter to find students who pass on both criteria
    eligible_students = []
    for score, att in student_data:
        if score >= passing_score / 100 and att >= min_attendance:
            bonus = 0.05 if att >= 0.92 else 0.02
            adjusted_score = min(1.0, score + bonus)
            eligible_students.append(adjusted_score)

    # Map adjusted scores back to percentage-like values
    mapped_data = [int(score * 100) for score in eligible_students]

    # Additional distraction: calculate entropy of original scores (unused)
    import math
    entropy = -sum([p/len(raw_scores) * math.log2(p/len(raw_scores)) for p in raw_scores])

    # Thresholds for final tiered categorization
    thresholds = {'bronze': 85, 'silver': 90, 'gold': 95}

    def process_results(data, limits):
        count_gold = 0
        count_silver = 0
        total = 0
        for val in data:
            total += val
            if val >= limits['gold']:
                count_gold += 1
            elif val >= limits['silver']:
                count_silver += 1
        # Final scoring formula: weighted combination
        return total + 5 * count_gold + 2 * count_silver

    final_score = process_results(mapped_data, thresholds)

    # Dead code branch - never executed but adds cognitive load
    if len(mapped_data) > 10:
        fallback = sum(mapped_data) // len(mapped_data)
        final_score = fallback

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()