from collections import defaultdict

def calculate_final_score():
    # Simulate student quiz scores with bonus logic
    scores = [78, 85, 92, 67, 88]
    bonus_awarded = [True, False, True, False, True]
    
    # Default dictionary to handle missing categories
    score_map = defaultdict(int)
    
    total = 0
    bonus_count = 0
    
    for i, score in enumerate(scores):
        if bonus_awarded[i]:
            adjusted_score = score * 1.1
        else:
            adjusted_score = score
        
        category = 'high' if adjusted_score >= 80 else 'medium'
        score_map[category] += 1
        
        total += adjusted_score
        bonus_count += 1 if bonus_awarded[i] else 0
    
    avg_score = total / len(scores)
    
    # Apply final adjustment based on performance distribution
    if score_map['high'] > 2:
        result = avg_score + 5
    else:
        result = avg_score + 2
    
    return result

# Irrelevant utility function (minimal interference)
def unused_helper():
    return sum(x**2 for x in range(3))

result = calculate_final_score()
print(f"Result: {result}")