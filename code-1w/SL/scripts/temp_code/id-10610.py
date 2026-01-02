from itertools import combinations

def main():
    # Simulated dataset of student test results and behavior metrics
    raw_scores = [85, 92, 78, 94, 88]
    attendance_rate = [0.94, 0.98, 0.85, 0.99, 0.91]
    participation_index = [3.7, 4.1, 3.2, 4.5, 3.8]

    # Irrelevant transformation: mapping scores to letter grades (not used in final calculation)
    def to_letter_grade(score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'F'
    letter_grades = [to_letter_grade(s) for s in raw_scores]  # Dead-end list

    # Preprocessing step: normalize scores to 0-1 scale
    normalized_scores = [(s - 70) / 30 for s in raw_scores]  # Stretch logic: base adjustment

    # Distractor computation: pairwise correlation attempt (unused)
    pair_correlations = []
    for i, j in combinations(range(len(raw_scores)), 2):
        corr = (normalized_scores[i] - normalized_scores[j]) ** 2
        pair_correlations.append(corr)  # Computed but never used

    # Weighted combination using enumerate and zip
    processed_data = []
    weights = [0.6, 0.25, 0.15]  # Score, attendance, participation
    for idx, score in enumerate(normalized_scores):
        adjusted = score * weights[0] + attendance_rate[idx] * weights[1]
        # Participation added via lambda for minor complexity
        add_participation = lambda x, y: x * y
        adjusted += add_participation(participation_index[idx] / 5.0, weights[2])
        processed_data.append(round(adjusted, 4))

    # Secondary distractor: sorting in reverse (not used)
    sorted_desc = sorted(processed_data, reverse=True)
    rank_order = [i for i, _ in enumerate(sorted(processed_data))]  # Unused ranking indices

    # Core logic: compute ranking score using processed_data
    def calculate_ranking(data):
        total = 0.0
        for val in data:
            if val > 0.85:
                total += val * 1.1
            elif val > 0.75:
                total += val * 1.05
            else:
                total += val
        return int(total * 10)  # Scale and convert to integer

    final_score = calculate_ranking(processed_data)
    
    # Extraneous post-processing
    validation_check = sum(1 for x in processed_data if x > 0.8)  # Used in no decision
    threshold_met = validation_check >= 3

    print(f"Result: {final_score}")

main()