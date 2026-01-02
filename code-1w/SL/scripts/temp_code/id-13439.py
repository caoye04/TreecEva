from itertools import compress

# Simulate sensor readings with noise filtering
data_stream = [104, 101, 98, 115, 122, 109, 96, 111, 118, 107]
noise_mask = [x % 2 == 0 for x in range(len(data_stream))]
filtered_data = list(compress(data_stream, noise_mask))

# Prime number candidates for hashing modulus
prime_candidates = [x for x in range(11, 20) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

# Secondary buffer (irrelevant to final result)
buff = sum(data_stream[i] for i in range(0, len(data_stream), 3))

# Key computation step
temp = sum(filtered_data) // len(filtered_data)
result = filtered_data[-1] ** 2 % prime_candidates[0]

print(f"Target result: {result}")