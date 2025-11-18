from functools import reduce

def get_kmers(sequence, k):
    return [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

def count_kmers(kmers):
    freq_dict = {}
    for kmer in kmers:
        freq_dict[kmer] = freq_dict.get(kmer, 0) + 1
    return freq_dict

dna_segment_1 = "ATGCGATACGTAAGCTAGCTAGCTAACGTAGCTAGCTA"
dna_segment_2 = "CGATACGTAAGCTAGCTAACGTAGCTAGCTAACGTAGC"

kmer_length = 4

kmers_1 = get_kmers(dna_segment_1, kmer_length)
kmers_2 = get_kmers(dna_segment_2, kmer_length)

freq_dict_1 = count_kmers(kmers_1)
freq_dict_2 = count_kmers(kmers_2)

# Merge dictionaries with addition for common keys
merged_freq = {key: freq_dict_1.get(key, 0) + freq_dict_2.get(key, 0) 
               for key in set(freq_dict_1) | set(freq_dict_2)}

# Greedy selection of maximum frequency
max_frequency = reduce(lambda x, y: x if x > y else y, merged_freq.values())

# Normalize frequencies using a lambda function
normalize = lambda freq, max_freq: round((freq / max_freq) * 100, 2)

# Apply normalization to all frequencies
normalized_freq_dict = {k: normalize(v, max_frequency) for k, v in merged_freq.items()}

# Find the normalized value of the maximum frequency
normalized_max_frequency = normalized_freq_dict[max(normalized_freq_dict, key=normalized_freq_dict.get)]

print(f"Result: {int(normalized_max_frequency)}")