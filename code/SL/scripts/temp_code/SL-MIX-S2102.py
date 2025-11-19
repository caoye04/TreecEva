import itertools

def generate_modular_hash(key, modulus=256):
    return sum(ord(c) * (i + 1) for i, c in enumerate(key)) % modulus

def decode_signal(signal_map, hash_key):
    return signal_map.get(hash_key, 0)

# Initialize observation data
observatory_signals = {
    "alpha": "PulseA",
    "beta": "PulseB",
    "gamma": "PulseC",
    "delta": "PulseD"
}

# Create hash map using dictionary comprehension
signal_hashes = {name: generate_modular_hash(code) for name, code in observatory_signals.items()}

# Process signal combinations
combined_signals = list(itertools.combinations(signal_hashes.keys(), 2))
processed_values = []

for pair in combined_signals:
    hash_sum = signal_hashes[pair[0]] + signal_hashes[pair[1]]
    mod_value = hash_sum % 17
    processed_values.append(mod_value)

# Apply decoding lookup
lookup_table = {i: val * 3 + 1 for i, val in enumerate(processed_values)}

# Calculate final code using nested modular operations
final_code = 0
for i, val in enumerate(processed_values):
    if i % 2 == 0:
        nested_mod = (val * 2 + lookup_table[i]) % 13
    else:
        nested_mod = (val * 3 - lookup_table[i]) % 11
    final_code = (final_code + nested_mod * (i + 1)) % 19

print(f"Result: {final_code}")