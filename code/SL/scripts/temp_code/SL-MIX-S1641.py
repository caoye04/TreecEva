import math

def fibonacci_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

token_strengths = [2.7, 3.14, 0, -1.5, 4.6, 5.2, 1.0, 6.8]
fib_weights = fibonacci_sequence(len(token_strengths))
valid_tokens = [t for t in token_strengths if t > 0]
weighted_log_scores = [math.log(t) * fib_weights[i] for i, t in enumerate(valid_tokens)]
score_variance = sum((s - sum(weighted_log_scores)/len(weighted_log_scores))**2 for s in weighted_log_scores) / len(weighted_log_scores)
entropy_factor = math.exp(-score_variance)
final_score = round(entropy_factor * sum(weighted_log_scores), 4)
print(f'Result: {final_score}')