from itertools import groupby

def calculate_entropy(counts):
    total = sum(counts)
    entropy = 0
    for count in counts:
        if count > 0:
            probability = count / total
            entropy -= probability * __import__('math').log2(probability)
    return round(entropy, 4)

data_stream = ['A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'A', 'C', 'C']

# Group consecutive elements
consecutive_groups = [list(g) for k, g in groupby(data_stream)]
group_lengths = [len(group) for group in consecutive_groups]

temp_var = "irrelevant_string"
unused_list = [1, 2, 3]

total_entropy = calculate_entropy(group_lengths)
print(f"Result: {total_entropy}")