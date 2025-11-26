def calculate_quiz_scores():
    raw_scores = [85, 92, 78, 0, 95, 88, 0, 91]
    valid_entries = {score for score in raw_scores if score > 0}
    processed_sum = sum(valid_entries)
    final_score = round(processed_sum / len(valid_entries), 2)
    print(f"Target result: {final_score}")

calculate_quiz_scores()