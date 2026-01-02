def process_results(grades, limits):
    scaled = [g * 1.1 for g in grades if g >= limits[0]]
    filtered = scaled[:3] if len(scaled) > 2 else scaled
    adjusted = [f + 0.5 if f < limits[1] else f - 0.3 for f in filtered]
    return int(sum(adjusted))

# Irrelevant auxiliary data (minor distraction)
student_ids = [101, 102, 103, 104]
subject = "Mathematics"

# Core input data
grades = [78, 85, 62, 91, 73]
thresholds = [70, 80]

# Key computation
final_score = process_results(grades, thresholds)

print(f"Result: {final_score}")