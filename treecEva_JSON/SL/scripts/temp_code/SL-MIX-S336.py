from collections import defaultdict
from itertools import combinations

genomic_sequences = [
    [1, 2, 3, 2, 4],
    [2, 1, 3, 4, 2],
    [1, 3, 2, 4, 1],
    [3, 2, 1, 4, 2]
]

pair_window_counts = defaultdict(int)

for seq in genomic_sequences:
    seen_in_this_seq = set()
    for i in range(len(seq)):
        window_end = min(i + 3, len(seq))
        for j in range(i + 1, window_end):
            if seq[i] != seq[j]:
                pair = tuple(sorted((seq[i], seq[j])))
                if pair not in seen_in_this_seq:
                    pair_window_counts[pair] += 1
                    seen_in_this_seq.add(pair)

significant_pairs_count = sum(1 for count in pair_window_counts.values() if count >= 2)

print(f"Result: {significant_pairs_count}")