from collections import Counter

scores = [85, 90, 78, 90, 85, 82, 95, 78]

def process_scores(scores_list):
    count = Counter(scores_list)
    top_score = max(count.keys())
    
    # Filter scores that appear more than once
    duplicates = list(filter(lambda x: count[x] > 1, count))
    
    if len(duplicates) == 0:
        return top_score
    
    # Compute average of duplicate values
    avg_duplicates = sum(duplicates) / len(duplicates)
    
    # Return combined metric only if top score is above 80
    if top_score > 80:
        return top_score + round(avg_duplicates)
    
    return top_score

result = process_scores(scores)
print(f"Result: {result}")