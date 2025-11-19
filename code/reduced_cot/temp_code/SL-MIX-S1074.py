import heapq
from functools import reduce

def tokenize(sentence):
    return sentence.lower().split()

def word_frequency_heap(tokens):
    freq_map = {}
    for token in tokens:
        freq_map[token] = freq_map.get(token, 0) + 1
    heap = []
    for word, count in freq_map.items():
        heapq.heappush(heap, (count, word))
    return heap

def semantic_backtrack(freq_heap, depth=0):
    if not freq_heap or depth > 3:
        return 0
    count, word = heapq.heappop(freq_heap)
    # Recursive exploration with adjusted weights
    base_value = len(word) * count
    recursive_value = semantic_backtrack(freq_heap, depth + 1)
    return base_value + recursive_value // 2

class CoherenceDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        # Apply normalization using set operations
        unique_chars = set(reduce(lambda x, y: x + y, args[0]))
        return result / len(unique_chars) if unique_chars else 0

@CoherenceDecorator
def calculate_coherence(tokens):
    freq_heap = word_frequency_heap(tokens)
    return semantic_backtrack(freq_heap)

# Main processing
input_sentence = "The quick brown fox jumps over the lazy dog"
tokens = tokenize(input_sentence)
final_coherence_score = calculate_coherence(tokens)
print(f"Result: {int(final_coherence_score)}")