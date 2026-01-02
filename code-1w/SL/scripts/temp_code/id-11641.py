students = [
    {'name': 'Alice', 'grades': [85, 90, 78], 'active': True},
    {'name': 'Bob', 'grades': [70, 68, 72], 'active': True},
    {'name': 'Charlie', 'grades': [95, 98, 92], 'active': False},
    {'name': 'Diana', 'grades': [88, 85, 90], 'active': True}
]

# Calculate average grade for each active student
averages = [
    sum(s['grades']) / len(s['grades']) for s in students if s['active']
]

# Threshold performance: students with average >= 85
filtered_performance = [avg for avg in averages if avg >= 85]

# Final score computation
bonus = 5
base_total = sum(averages)
total_score = sum(filtered_performance)

print(f"Result: {total_score}")