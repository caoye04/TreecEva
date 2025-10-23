def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

fib_sequence = generate_sequence(8)
eighth_element = fib_sequence[7]
hex_string = hex(eighth_element)[2:]  # Remove '0x' prefix
from collections import Counter
char_counter = Counter(hex_string)
hex_count = char_counter['1']

print(f"Result: {hex_count}")