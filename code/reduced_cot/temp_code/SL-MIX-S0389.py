from itertools import combinations

def count_nucleotides(subseq):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nuc in subseq:
        if nuc in counts:
            counts[nuc] += 1
    return counts['A'] == counts['T'] and counts['C'] == counts['G']

def stability_score_memo(seq, memo):
    if seq in memo:
        return memo[seq]
    if len(seq) < 2:
        memo[seq] = 0
        return 0
    score = 0
    if count_nucleotides(seq):
        score = len(seq)
    else:
        score = max(
            stability_score_memo(seq[1:], memo),
            stability_score_memo(seq[:-1], memo)
        )
    memo[seq] = score
    return score

# Main computation
fragment = "ATCGATCG"
memoization_table = {}
stability_metric = stability_score_memo(fragment, memoization_table)
print(f"Result: {stability_metric}")