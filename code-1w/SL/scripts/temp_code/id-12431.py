def calculate_final_score(students):
    passing_threshold = 50
    bonus_per_high_performer = 3

    # Extract scores and compute average
    scores = [s['score'] for s in students]
    avg_score = sum(scores) / len(scores)

    # Count how many scored above 75
    high_performers = [s for s in students if s['score'] > 75]
    bonus = len(high_performers) * bonus_per_high_performer

    # Apply bonus only if average is above threshold
    if avg_score > passing_threshold:
        adjusted_avg = avg_score + bonus
    else:
        adjusted_avg = avg_score

    return int(adjusted_avg)

# Irrelevant utility function (minor interference)
def format_name(student):
    return f"{student['name'].title()}"

# Dataset
students_data = [
    {'name': 'alice', 'score': 68},
    {'name': 'bob', 'score': 72},
    {'name': 'charlie', 'score': 85},
    {'name': 'diana', 'score': 90},
    {'name': 'eve', 'score': 45}
]

# Computation
final_score = calculate_final_score(students_data)
print(f"Result: {final_score}")