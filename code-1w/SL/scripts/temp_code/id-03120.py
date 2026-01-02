from itertools import compress

def calculate_final_score(raw_scores, deductions):
    # Filter scores above threshold
    passing = [s for s in raw_scores if s >= 70]
    
    # Apply penalty mapping using index alignment
    adjusted = []
    for i, score in enumerate(passing):
        factor = 1 - (deductions[i % len(deductions)] / 100)
        adjusted.append(score * factor)
    
    # Compute mean using slicing to exclude potential outliers on edges
    trimmed = sorted(adjusted)[1:-1] if len(adjusted) > 2 else adjusted
    average = sum(trimmed) / len(trimmed) if trimmed else 0
    
    # Bonus logic based on performance consistency
    if len(trimmed) >= 3 and max(trimmed) - min(trimmed) <= 15:
        average += 5  # Consistency bonus
    
    return round(average, 2)

# Input data
scores = [85, 90, 65, 78, 92, 88]
penalties = [10, 20, 5]
extra_noise_value = 42  # Irrelevant variable (minimal distraction)

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")