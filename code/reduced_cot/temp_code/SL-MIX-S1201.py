def calculate_section_score(tray_layout):
    total_score = 0
    for row_index, row in enumerate(tray_layout):
        for col_index, plant_count in enumerate(row):
            if plant_count > 0:
                # Score per plant is (row+1) * (col+1)
                plant_score = (row_index + 1) * (col_index + 1)
                total_score += plant_score * plant_count
    return total_score

# Greenhouse section tray layouts (rows x columns with plant counts)
section_a = [
    [2, 0, 3],
    [1, 4, 0]
]

section_b = [
    [0, 2],
    [3, 1],
    [2, 0]
]

section_c = [
    [1, 1, 1],
    [0, 2, 0]
]

scores = []
scores.append(calculate_section_score(section_a))
scores.append(calculate_section_score(section_b))
scores.append(calculate_section_score(section_c))

# Find section with maximum score
max_score = sorted(scores)[-1]
print(f"Result: {max_score}")