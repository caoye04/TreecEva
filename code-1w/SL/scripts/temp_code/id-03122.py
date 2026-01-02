def calculate_final_score(records):
    base_scores = {k: v for k, v in records.items() if v > 0}
    adjustments = set(range(len(records)))
    offset = sum(base_scores.values()) // len(base_scores)
    temp_result = [v * (k.count('a') + 1) for k, v in base_scores.items()]
    
    if len(temp_result) > 2:
        temp_result = temp_result[1:-1]  # slice middle elements
    
    aggregated = sum(temp_result) + offset
    penalty = len(adjustments.intersection({2, 3, 5, 7}))  # prime index check
    final_score = aggregated - penalty * 2
    return final_score

# Simulated dataset
data = {'alice': 8, 'bob': -2, 'charlie': 12, 'diana': 6}
final_score = calculate_final_score(data)
print(f"Result: {final_score}")