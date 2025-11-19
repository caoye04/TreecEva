from collections import defaultdict
import math

token_stream = [0x001F00A0, 0x002A0085, 0x001F0090, 0x003C0070, 0x002A0085]
category_scores = defaultdict(int)

for token in token_stream:
    category_id = (token >> 16) & 0xFFFF
    relevance_score = token & 0xFFFF
    if relevance_score > 100:
        adjusted_score = relevance_score * 2
    else:
        adjusted_score = relevance_score
    category_scores[category_id] += adjusted_score

max_score = max(category_scores.values())
weighted_sum = sum(score * math.log(cat_id + 1) for cat_id, score in category_scores.items() if score > 150)
dominance_metric = int(weighted_sum / max_score * 1000) if max_score != 0 else 0

print(f"Result: {dominance_metric}")