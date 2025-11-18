from collections import defaultdict

def calculate_batch_score(batch_id):
    hash_val = hash(batch_id) % 100
    if hash_val < 25:
        return hash_val * 2 + 5
    elif hash_val < 50:
        return hash_val + 15
    elif hash_val < 75:
        return hash_val // 2 + 30
    else:
        return hash_val - 10

batches = ['FAB2023A', 'TEX99B', 'MATX456C', 'YARN78D']
scores = defaultdict(int)

for batch in batches:
    base_score = calculate_batch_score(batch)
    adjustment = len(batch) * 3
    scores[batch] = base_score + adjustment

final_score = sum(scores.values())
if final_score > 200:
    final_score -= 10
else:
    final_score += 5

print(f'Result: {final_score}')