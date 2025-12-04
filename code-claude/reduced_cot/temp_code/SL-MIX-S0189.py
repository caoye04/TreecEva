# Analysis of overlapping student participation in two academic events

science_fair = ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank']
math_olympiad = ['Bob', 'Diana', 'Eve', 'George', 'Hannah']

# Track event participation points
participation_points = {'science_fair': 5, 'math_olympiad': 7}

# Find students who participated in both events
overlaps = []
for i, student in enumerate(science_fair):
    position = i + 1  # Position in science fair roster
    if student in math_olympiad:
        overlaps.append(1)
    else:
        overlaps.append(0)

# Calculate total number of students in both events
total_overlap = sum(overlaps)

# Calculate some statistics about participation
total_participants = len(set(science_fair + math_olympiad))
average_points = (participation_points['science_fair'] * len(science_fair) + 
                 participation_points['math_olympiad'] * len(math_olympiad)) / total_participants

print(f"Result: {total_overlap}")