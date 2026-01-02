from math import log2

def calculate_symbol_entropy(count, total):
    if count == 0:
        return 0
    probability = count / total
    return -probability * log2(probability)

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'A']
symbol_counts = {symbol: data_stream.count(symbol) for symbol in set(data_stream)}
total_symbols = len(data_stream)
entropies = [calculate_symbol_entropy(count, total_symbols) for symbol in symbol_counts.values()]

total_entropy = sum(entropies)
# Irrelevant auxiliary variable (minor distraction)
redundant_copy = data_stream[:]

print(f"Result: {total_entropy}")