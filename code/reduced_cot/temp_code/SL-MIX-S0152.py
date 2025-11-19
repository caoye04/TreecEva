from collections import defaultdict, Counter

def tokenize_and_score(text_series):
    token_weights = defaultdict(lambda: 1.0)
    token_weights.update({'python': 2.5, 'optimization': 3.0, 'algorithm': 2.0, 'complexity': 1.5})
    
    all_tokens = []
    cumulative_scores = []
    
    for idx, sentence in enumerate(text_series):
        tokens = sentence.lower().replace(',', '').replace('.', '').split()
        token_count = Counter(tokens)
        
        score = 0.0
        for token, count in token_count.items():
            score += token_weights.get(token, 1.0) * count
        
        all_tokens.append(set(tokens))
        cumulative_scores.append(score if not cumulative_scores else cumulative_scores[-1] + score)
    
    # Dynamic programming: find maximum weighted intersection score
    dp_table = [0.0] * len(all_tokens)
    if all_tokens:
        dp_table[0] = sum(token_weights.get(t, 1.0) for t in all_tokens[0])
    
    for i in range(1, len(all_tokens)):
        intersection = all_tokens[i].intersection(all_tokens[i-1])
        intersection_value = sum(token_weights.get(t, 1.0) for t in intersection)
        dp_table[i] = max(dp_table[i-1], (dp_table[i-1] if i > 1 else 0) + intersection_value)
    
    # Final optimization using set operations
    universal_tokens = set().union(*all_tokens)
    rare_tokens = {t for t, w in token_weights.items() if w > 2.0}
    
    optimized_score = dp_table[-1] if dp_table else 0.0
    optimized_score += len(universal_tokens.intersection(rare_tokens)) * 1.5
    
    return optimized_score

# Process linguistic data
linguistic_corpus = [
    "Python optimization algorithms require complexity analysis",
    "Algorithm complexity in Python demands optimization techniques",
    "Text processing and pattern recognition in Python"
]

final_score = tokenize_and_score(linguistic_corpus)
print(f"Result: {final_score}")