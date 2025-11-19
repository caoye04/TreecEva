from functools import reduce

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

cipher_segments = [x for x in fibonacci_sequence(10)][2:]
transformed_signals = list(map(lambda x: x**2 if x % 2 == 0 else x*3, cipher_segments))
filtered_signals = list(filter(lambda x: x > 10, transformed_signals))
encoded_metadata = {f'sig_{i}': val for i, val in enumerate(filtered_signals)}
decoded_keys = {k: v for k, v in encoded_metadata.items() if 'sig_' in k}
aggregated_value = reduce(lambda acc, kv: acc + kv[1], decoded_keys.items(), 0)
decoded_signal_strength = aggregated_value % 100 + len(decoded_keys) * 7
print(f'Result: {decoded_signal_strength}')