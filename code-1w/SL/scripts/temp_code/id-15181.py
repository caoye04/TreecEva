from itertools import groupby

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * __import__('math').log2(probability)
    return round(entropy, 4)

text_stream = 'abacabadabacaba'
# Irrelevant preprocessing: count character transitions
transitions = 0
for i in range(len(text_stream) - 1):
    if text_stream[i] != text_stream[i + 1]:
        transitions += 1

# Main computation: frequency analysis using groupby
sorted_chars = sorted(text_stream)
grouped = {k: len(list(g)) for k, g in groupby(sorted_chars)}
frequency_data = grouped

# Secondary distraction: calculate average char position
positions = [text_stream.index(c) for c in set(text_stream)]
avg_position = sum(positions) / len(positions)

# Key statement
total_entropy = calculate_entropy(frequency_data)

print(f"Result: {total_entropy}")