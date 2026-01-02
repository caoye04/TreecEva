from collections import Counter
import math

def calculate_symbol_info(freq, total):
    if freq == 0:
        return 0.0
    probability = freq / total
    return -probability * math.log2(probability) if probability > 0 else 0.0

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'E', 'A', 'B', 'F']

# Step 1: Count frequencies
symbol_counts = Counter(data_stream)
total_symbols = len(data_stream)

# Irrelevant distraction: counting vowels in symbol names (not used in final logic)
vowel_count = 0
for symbol in symbol_counts.keys():
    if symbol in 'AEIOU':
        vowel_count += 1

# Step 2: Compute total information entropy
total_info = 0.0
for count in symbol_counts.values():
    total_info += calculate_symbol_info(count, total_symbols)

# Step 3: Identify redundancy (symbols appearing more than once)
redundant_symbols = [sym for sym, cnt in symbol_counts.items() if cnt > 1]
redundancy_count = 0
for symbol in redundant_symbols:
    redundancy_count += symbol_counts[symbol] - 1  # excess occurrences

# Step 4: Compute net entropy (information adjusted by redundancy penalty)
net_entropy = total_info - redundancy_count

# Distractor computation: hypothetical compression ratio (not used)
compression_estimate = (total_symbols - redundancy_count) / total_symbols if total_symbols > 0 else 0

# Dead code path: never executed but looks relevant
if False:
    backup_entropy = sum([x * x for x in symbol_counts.values()])

# Final result output
print(f"Result: {net_entropy}")