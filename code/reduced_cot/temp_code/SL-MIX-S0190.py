from itertools import permutations
from statistics import variance
from heapq import heappush, heappop

def encode_string(s):
    encoded = 0
    for char in s:
        encoded = (encoded * 31 + ord(char)) & 0xFFFFFFFF
    return encoded

def decode_string(val, length):
    chars = []
    for _ in range(length):
        chars.append(chr(val % 31))
        val //= 31
    return ''.join(reversed(chars))

input_string = "abc"
unique_perms = set([''.join(p) for p in permutations(input_string)])
encoded_heap = []

for perm in unique_perms:
    encoded_val = encode_string(perm)
    heappush(encoded_heap, encoded_val)

encoded_values = []
while encoded_heap:
    encoded_values.append(heappop(encoded_heap))

final_variance = variance(encoded_values)
print(f"Result: {final_variance}")