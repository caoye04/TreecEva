from collections import defaultdict
import itertools

def hex_to_binary_mask(hex_char):
    return bin(int(hex_char, 16))[2:].zfill(4)

def count_transitions(binary_str):
    return sum(1 for i in range(len(binary_str)-1) if binary_str[i] != binary_str[i+1])

markers = ['A', '3', 'F', '1', 'C']
stability_map = defaultdict(int)
transition_counts = []

for marker in markers:
    binary_repr = hex_to_binary_mask(marker)
    transitions = count_transitions(binary_repr)
    transition_counts.append(transitions)
    stability_map[marker] ^= transitions

unique_transitions = frozenset(transition_counts)
sorted_unique = sorted(list(unique_transitions))

if len(sorted_unique) >= 3:
    selected = sorted_unique[1:3]
else:
    selected = sorted_unique

stability_index = 0
for val in selected:
    match val:
        case 1:
            stability_index += 10
        case 2:
            stability_index += 20
        case 3:
            stability_index += 30
        case _:
            stability_index += 5

print(f"Result: {stability_index}")