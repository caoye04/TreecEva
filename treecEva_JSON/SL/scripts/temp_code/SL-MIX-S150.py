from collections import Counter

def transform_token(token):
    return ''.join(sorted(token.lower()))

def aggregate_scores(scores):
    if not scores:
        return 0
    n = len(scores)
    if n == 1:
        return scores[0]
    mid = n // 2
    left = aggregate_scores(scores[:mid])
    right = aggregate_scores(scores[mid:])
    return (left + right) / 2 + abs(left - right) * 0.1

@staticmethod
def calculate_base(token_count):
    return sum(count ** 2 for count in token_count.values())

class TextAnalyzer:
    def __init__(self, text):
        self.tokens = text.split()
        self.transformed_tokens = [transform_token(t) for t in self.tokens]
        self.token_counter = Counter(self.transformed_tokens)
    
    def compute_complexity(self):
        base_score = calculate_base(self.token_counter)
        frequency_list = list(self.token_counter.values())
        aggregated = aggregate_scores(frequency_list)
        return base_score * aggregated

# Execution point Y
analyzer = TextAnalyzer("Data data DATA dAtA structure Structure algorithm Algorithm")
final_complexity_score = int(analyzer.compute_complexity())
print(f"Result: {final_complexity_score}")