from collections import defaultdict
import re

def tokenize(transactions):
    tokens = []
    for txn in transactions:
        parts = re.split(r'[:]', txn)
        tokens.append((parts[0], int(parts[1]), float(parts[2])))
    return tokens

scoring_fn = lambda category, count, amount: (count * 3 + int(amount)) & ~(1 << 2)

raw_txns = [
    "grocery:5:49.99",
    "utility:2:120.75",
    "entertainment:7:85.40",
    "grocery:3:22.30",
    "utility:1:95.00"
]

scores = defaultdict(int)
tokenized = tokenize(raw_txns)

for cat, cnt, amt in tokenized:
    score = scoring_fn(cat, cnt, amt)
    scores[cat] += score

score_list = [(k, v) for k, v in scores.items()]
score_list.sort(key=lambda x: x[1], reverse=True)

weighted_scores = [value * (i + 1) for i, (key, value) in enumerate(score_list)]
aggregated_score = sum(weighted_scores) // len(weighted_scores)

print(f"Result: {aggregated_score}")