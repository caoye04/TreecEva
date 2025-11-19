import re
from collections import Counter
from statistics import mean, variance
text_corpus = """Efficient algorithms optimize performance. Data structures facilitate organization. Programming languages enable implementation. Software engineering principles guide development."""
word_list = re.findall(r'\b\w+\b', text_corpus.lower())
length_map = {word: len(word) for word in word_list}
unique_lengths = list(set(length_map.values()))
sorted_lengths = sorted(unique_lengths)
fib_cache = {0: 0, 1: 1}
def fibonacci(n):
    if n not in fib_cache:
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_cache[n]
transformed_lengths = [fibonacci(length) for length in sorted_lengths]
length_freq = Counter([length_map[word] for word in length_map])
weighted_values = {k: k * v for k, v in length_freq.items()}
stats_dict = {
    'mean_length': mean(sorted_lengths),
    'variance_length': variance(sorted_lengths) if len(sorted_lengths) > 1 else 0,
    'total_weight': sum(weighted_values.values()),
    'max_transformed': max(transformed_lengths)
}
aggregated_score = stats_dict['mean_length'] * stats_dict['max_transformed']
final_metric = round(aggregated_score + stats_dict['variance_length'], 2)
print(f'Result: {final_metric}')