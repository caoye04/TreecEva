from itertools import compress

def calculate_final_score(data):
    base_scores = [entry['points'] for entry in data]
    weights = [0.25 if entry['tier'] == 'A' else 0.15 for entry in data]
    
    # Apply conditional scaling based on rank threshold
    scaled_scores = [score * (1.1 if i < 3 else 1.0) for i, score in enumerate(base_scores)]
    
    # Compute final weighted sum
    final_score = sum(scaled_scores[i] * weights[i] for i in range(len(data)))
    
    return final_score

# Irrelevant auxiliary variable (minor distraction)
dummy_flag = True

rank_data = [
    {'name': 'Alpha', 'points': 88, 'tier': 'A'},
    {'name': 'Beta',  'points': 92, 'tier': 'B'},
    {'name': 'Gamma', 'points': 76, 'tier': 'A'},
    {'name': 'Delta', 'points': 81, 'tier': 'A'}
]

final_score = calculate_final_score(rank_data)
print(f"Result: {final_score}")