def analyze_student_performance(records):
    # Irrelevant summary statistics (distractor)
    total_entries = len(records)
    avg_grade = sum(r['grade'] for r in records) / total_entries
    grade_variance = sum((r['grade'] - avg_grade) ** 2 for r in records) / total_entries

    # Relevant processing: extract passing students and their feedback length
    passing_students = [r for r in records if r['grade'] >= 60]
    feedback_lengths = {s['name']: len(s['feedback'].split()) for s in passing_students}

    # Misleading normalization attempt (not used)
    normalized_scores = {}
    max_len = max(feedback_lengths.values()) if feedback_lengths else 1
    for name, length in feedback_lengths.items():
        normalized_scores[name] = round(length / max_len * 100, 2)

    # Actual scoring logic based on engagement metrics
    engagement_score = 0
    for student in passing_students:
        words = len(student['feedback'].replace('.', '').replace(',', '').split())
        completeness = 1 if student['submitted_on_time'] else 0.5
        depth_factor = 1 + (words // 50)  # bonus per 50 words
        engagement_score += words * completeness * depth_factor

    # Auxiliary computation: letter frequency (irrelevant)
    all_feedback = ' '.join(f['feedback'] for f in records).lower()
    letter_freq = {}
    for char in all_feedback:
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1
    rare_letters = [l for l, c in letter_freq.items() if c < 3]
    penalty = len(rare_letters) * 0.25

    # Final performance calculation
    base_performance = sum(1 for s in passing_students if s['engagement_level'] == 'high')
    time_bonus = sum(5 for s in passing_students if s['submitted_on_time'])
    final_score = int(engagement_score // 10) + base_performance * 2 + time_bonus - int(penalty)

    return final_score

# Dataset with realistic student records
student_records = [
    {'name': 'Alice', 'grade': 85, 'feedback': 'Excellent work with thorough explanations and clear logic.', 'submitted_on_time': True, 'engagement_level': 'high'},
    {'name': 'Bob', 'grade': 45, 'feedback': 'Needs improvement in problem-solving approach.', 'submitted_on_time': False, 'engagement_level': 'low'},
    {'name': 'Charlie', 'grade': 72, 'feedback': 'Good analysis, well-structured code, but missed edge cases in testing. Additional comments about best practices.', 'submitted_on_time': True, 'engagement_level': 'medium'},
    {'name': 'Diana', 'grade': 93, 'feedback': 'Outstanding solution using advanced algorithms and detailed documentation. Clear comments throughout.', 'submitted_on_time': True, 'engagement_level': 'high'},
    {'name': 'Evan', 'grade': 58, 'feedback': 'Incomplete submission with minimal explanation.', 'submitted_on_time': False, 'engagement_level': 'low'}
]

# Key execution point
final_score = analyze_student_performance(student_records)
print(f"Result: {final_score}")