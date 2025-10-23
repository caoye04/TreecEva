from functools import reduce

def palindrome_contributions(seq):
    n = len(seq)
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i, n):
            substr = seq[i:j+1]
            if substr == substr[::-1]:
                dp[j+1] = max(dp[j+1], dp[i] + (j-i+1))
    return dp

@lambda f: lambda x: 2 * f(x) - 1
def transform_score(value):
    return value + 3

sequences = ['ATGCA', 'CGTAC', 'TACGT']
scores = []
for seq in sequences:
    raw_scores = palindrome_contributions(seq)
    max_raw = max(raw_scores)
    transformed = transform_score(max_raw)
    scores.append(transformed)

sorted_scores = sorted(scores)
regulatory_score = reduce(lambda acc, x: acc + x if x > 10 else acc, sorted_scores, 0)
print(f"Result: {regulatory_score}")