from collections import defaultdict

token_stream = ['alpha', 'beta', 'gamma', 'delta', 'alpha', 'epsilon', 'beta', 'zeta']
anomaly_score = 0
seen_tokens = set()
token_frequency = defaultdict(int)

for idx, token in enumerate(token_stream):
    if token in seen_tokens:
        anomaly_score += 5
        if token_frequency[token] >= 2:
            anomaly_score *= 2
        else:
            anomaly_score -= 1
    else:
        seen_tokens.add(token)
    
    token_frequency[token] += 1
    
    if idx == 4:
        if 'gamma' not in seen_tokens:
            anomaly_score += 3
        elif token_frequency['alpha'] == 2:
            anomaly_score -= 2
    
    if anomaly_score > 15:
        break

print(f"Result: {anomaly_score}")