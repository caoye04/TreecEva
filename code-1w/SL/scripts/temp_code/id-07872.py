def analyze_feedback(survey_data):
    feedback_set = set()
    duplicates = set()
    char_count = 0

    for entry in survey_data:
        for ch in entry:
            char_count += 1

        if entry in feedback_set:
            duplicates.add(entry)
        else:
            feedback_set.add(entry)

    unique_entries = len(feedback_set)
    total_entries = len(survey_data)
    duplicate_count = len(duplicates)

    # Irrelevant statistical distraction
    avg_length = char_count / total_entries if total_entries else 0

    return feedback_set, unique_entries, avg_length


def process_ratings(rating_list):
    normalized = []
    max_rating = max(rating_list) if rating_list else 1
    for val in rating_list:
        norm_val = (val / max_rating) * 100
        if norm_val > 75:
            normalized.append(int(norm_val))

    # Dead code path - never used
    sorted_desc = sorted(normalized, reverse=True)

    return normalized

def evaluate_performance(feedback, raw_scores):
    score_map = {}
    for i, rating in enumerate(raw_scores):
        score_map[i] = rating * 1.5

    adjustment_factor = 0.9
    cumulative = 0

    # Use of zip to align feedback indices with scores
    feedback_list = list(feedback)
    for idx, (fb, orig_idx) in enumerate(zip(feedback_list, range(len(feedback_list)))):
        temp_key = f"entry_{idx}"
        if idx < len(raw_scores):
            base = score_map[orig_idx] if orig_idx in score_map else 10
            cumulative += base * adjustment_factor

    # Additional distraction: character frequency analysis (unused)
    freq = {}
    for item in feedback:
        first_char = item[0] if item else '?'
        freq[first_char] = freq.get(first_char, 0) + 1

    final_score = int(cumulative - 35)  # Final deterministic computation
    return final_score

# Main execution flow
survey_responses = ['excellent', 'good', 'excellent', 'satisfactory', 'good', 'outstanding']
ratings = [4, 3, 5, 2, 4]

feedback_set, _, _ = analyze_feedback(survey_responses)
normalized_ratings = process_ratings(ratings)
final_score = evaluate_performance(feedback_set, ratings)
print(f"Result: {final_score}")