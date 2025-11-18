def max_non_adjacent_score(scores):
    if not scores:
        return 0
    if len(scores) == 1:
        return scores[0]
    
    prev_prev = scores[0]
    prev = max(scores[0], scores[1])
    
    for i in range(2, len(scores)):
        current = max(prev, prev_prev + scores[i])
        prev_prev = prev
        prev = current
    
    return prev

recipe_scores = [2, 1, 4, 9]
max_score = max_non_adjacent_score(recipe_scores)
print(f'Result: {max_score}')