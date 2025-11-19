from collections import defaultdict
from statistics import mean, variance
import hashlib

class SectionAnalyzer:
    def __init__(self):
        self.word_freq = defaultdict(int)
        self.section_count = 0
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def process_fragment(self, text):
        tokens = text.lower().replace(',', '').split()
        for token in tokens:
            self.word_freq[token] += 1
        self.section_count += 1
        
    def get_stats(self):
        frequencies = list(self.word_freq.values())
        return mean(frequencies), variance(frequencies) if len(frequencies) > 1 else 0

def fibonacci_hash(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return hash(str(b)) % 1000

text_fragments = [
    "machine learning algorithms optimize performance",
    "performance metrics evaluate machine efficiency",
    "algorithm optimization requires careful analysis"
]

with SectionAnalyzer() as analyzer:
    hash_values = []
    for i, fragment in enumerate(text_fragments):
        analyzer.process_fragment(fragment)
        mean_freq, var_freq = analyzer.get_stats()
        condition = mean_freq > 1.5 and var_freq > 0
        hash_val = fibonacci_hash(i) if condition else hash(fragment) % 1000
        hash_values.append(hash_val)
    
    # Critical computation point
    aggregate_hash_score = sum(hash_values) if any(h > 500 for h in hash_values) else 0
    
    # Ternary operator with short-circuit evaluation
    final_adjustment = (lambda x: x * 2 if x > 1000 else x // 2)(sum(hash_values)) or 42
    
    aggregate_hash_score += final_adjustment

print(f"Result: {aggregate_hash_score}")