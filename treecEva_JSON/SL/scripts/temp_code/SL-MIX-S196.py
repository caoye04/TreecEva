import re
from collections import defaultdict

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Generate Fibonacci numbers up to length 20 (reasonable word length limit)
fib_set = {fibonacci(i) for i in range(20)}
text_corpus = "The quick brown fox jumps over the lazy dog while analyzing linguistic structures"
word_lengths = [len(word) for word in re.findall(r'\b\w+\b', text_corpus)]
fibonacci_matched_count = sum(1 for length in word_lengths if length in fib_set)
print(f'Result: {fibonacci_matched_count}')