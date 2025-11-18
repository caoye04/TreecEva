from collections import defaultdict
import statistics
import functools

def register_processor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.results.append(result)
        return result
    wrapper.results = []
    return wrapper

class TextAnalyzer:
    def __init__(self):
        self.stop_words = {'the', 'and', 'or', 'but', 'is', 'are'}
        self.word_lengths = defaultdict(list)
    
    @register_processor
    def tokenize(self, sentence):
        tokens = sentence.lower().split()
        filtered_tokens = [word.strip('.,!?') for word in tokens if word.lower() not in self.stop_words]
        return filtered_tokens
    
    @register_processor
    def compute_lengths(self, tokens):
        lengths = [len(token) for token in tokens]
        return lengths
    
    def process_corpus(self, sentences):
        total_variance = 0
        for sentence in sentences:
            tokens = self.tokenize(sentence)
            lengths = self.compute_lengths(tokens)
            if lengths:
                self.word_lengths[sentence].extend(lengths)
                total_variance += statistics.variance(lengths) if len(lengths) > 1 else 0
        return total_variance / len(sentences) if sentences else 0

analyzer = TextAnalyzer()
corpus = [
    "The quick brown fox jumps over the lazy dog.",
    "Machine learning is but a subset of artificial intelligence.",
    "Natural language processing enables computers to understand human language."
]

avg_variance = analyzer.process_corpus(corpus)
lengths_list = list(analyzer.word_lengths.values())
flattened_lengths = [item for sublist in lengths_list for item in sublist]
final_metric = int(avg_variance * 100 + sum(flattened_lengths))
print(f"Result: {final_metric}")