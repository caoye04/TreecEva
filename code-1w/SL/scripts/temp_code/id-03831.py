def analyze_text(text):
    words = text.split()
    word_length_sum = sum(len(word) for word in words)
    avg_word_length = word_length_sum / len(words) if words else 0
    unique_chars = len(set(text))
    char_frequency = {c: text.count(c) for c in set(text)}
    entropy = 0
    for count in char_frequency.values():
        prob = count / len(text)
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return avg_word_length, unique_chars, entropy


def transform_sequence(seq):
    if not seq:
        return []
    transformed = [seq[0]]
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            transformed.append(seq[i] * 2)
        else:
            transformed.append(seq[i] // 2)
    return sorted(transformed, reverse=True)


def dummy_processor(data):
    # Irrelevant function - dead code path
    result = 0
    for item in data:
        if isinstance(item, int):
            result ^= item << 2
    return result

# Decoy variables and irrelevant computations
text_corpus = "The quick brown fox jumps over the lazy dog multiple times daily"
dummy_metric_1 = len(text_corpus) * 3 + 7
dummy_metric_2 = sum(ord(c) for c in text_corpus if c in 'aeiou')

# Bit manipulation red herring
bitmask = 0b10101010
shifted_mask = bitmask << 3
masked_value = shifted_mask & 0xFF

# Unused data structure
historical_logs = [
    {'event': 'start', 'code': 100, 'flag': False},
    {'event': 'retry', 'code': 101, 'flag': True},
    {'event': 'fail', 'code': 202, 'flag': False}
]

# Relevant input data
metric_data = [85, 92, 78, 96, 88]

# Distractor: fake aggregation
fake_aggregate = 0
for val in metric_data:
    if val % 2 == 0:
        fake_aggregate += val ^ 5

# Conditional expression with misleading branch
data_valid = True if sum(metric_data) > 300 else False

# Another decoy function that is never called
def deprecated_scoring(arr):
    total = 0
    for x in arr:
        total += x ** 0.5
    return total // len(arr)

# Core logic buried among noise
def evaluate_performance(scores):
    normalized = [s / 100.0 for s in scores]
    weighted = [n * (i + 1) for i, n in enumerate(normalized)]
    base_score = sum(weighted)
    
    # Simulate dependency on string analysis
    simulated_text = "x" * int(base_score * 10)
    _, _, entropy_component = analyze_text(simulated_text)
    
    # Real but hidden use of recursion
    def recursive_boost(n):
        return n if n <= 1 else n + recursive_boost(n - 2)
    
    adjustment = recursive_boost(len(scores))
    
    # Critical calculation
    temp_result = base_score * 100 + adjustment * entropy_component
    
    # Final transformation using conditional expression
    final_modifier = 1.5 if len(scores) >= 4 and data_valid else 0.8
    return int(temp_result * final_modifier)

# Key execution point
final_score = evaluate_performance(metric_data)
print(f"Target result: {final_score}")