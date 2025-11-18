import itertools
import statistics

cipher_hex = 'a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3'
pair_generator = (cipher_hex[i:i+2] for i in range(len(cipher_hex)-1))
pair_frequencies = {}
for pair in pair_generator:
    pair_frequencies[pair] = pair_frequencies.get(pair, 0) + 1

unique_pairs_count = len(pair_frequencies)
frequency_values = list(pair_frequencies.values())
mean_frequency = statistics.mean(frequency_values)
variance = statistics.variance(frequency_values) if len(frequency_values) > 1 else 0

high_freq_pairs = list(filter(lambda item: item[1] > mean_frequency, pair_frequencies.items()))
high_freq_count = len(high_freq_pairs)

security_index = int(variance * unique_pairs_count + high_freq_count)
print(f"Result: {security_index}")