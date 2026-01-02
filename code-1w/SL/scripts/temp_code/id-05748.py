def calculate_final_score():
    scores = [85, 92, 78, 96, 88]
    adjustments = {85: -2, 92: +3, 78: +5, 88: 0}
    
    # Apply adjustments only for scores above 80
    adjusted = []
    for s in scores:
        if s <= 80:
            adjusted.append(s)
            continue
        delta = adjustments.get(s, 0)
        adjusted.append(s + delta)
    
    # Use slicing to consider only last 3 adjusted scores
    relevant = adjusted[-3:]
    
    # Calculate average and round to 2 decimal places
    total = sum(relevant)
    result = round(total / len(relevant), 2)
    return result

# Entry point
result = calculate_final_score()
print(f"Target result: {result}")