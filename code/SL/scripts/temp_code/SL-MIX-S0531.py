import heapq
from collections import defaultdict

def tokenize(expr):
    return expr.split()

def process_operators(token_stream):
    freq_map = defaultdict(int)
    for token in token_stream:
        if token in '+-*/^':
            freq_map[token] += 1
    return freq_map

def get_top_three(heap_data):
    heap = []
    for op, count in heap_data.items():
        heapq.heappush(heap, (count, op))
        if len(heap) > 3:
            heapq.heappop(heap)
    return [op for count, op in heap]

def validate_heap_content(top_ops):
    has_plus = '+' in top_ops
    has_mult = '*' in top_ops
    exceeds_threshold = len([op for op in top_ops if op in '+*']) >= 2
    return (has_plus and has_mult) or (not exceeds_threshold and '-' in top_ops)

token_sequence = tokenize("+ * - / + + * ^ - + * * + ^ ^ ^")
frequency_map = process_operators(token_sequence)
top_operators = get_top_three(frequency_map)
validation_result = validate_heap_content(top_operators)
print(f"Result: {int(validation_result)}")