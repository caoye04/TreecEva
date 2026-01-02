def calculate_final_score(data):
    segments = data.split(',')
    total = 0
    for segment in segments:
        stripped = segment.strip()
        if stripped.startswith('A'):
            total += len(stripped) * 2
        elif stripped.startswith('B'):
            total += len(stripped) + 5
        else:
            total += 3
    return total

raw_data = "Apple, Banana, Cherry, Avocado, Blueberry"
initial_weight = 1.5  # irrelevant variable (minimal distraction)
correction_factor = 0.9  # irrelevant variable (minimal distraction)
final_score = calculate_final_score(raw_data)
print(f"Result: {final_score}")