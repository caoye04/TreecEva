from functools import reduce

def custom_hash(token):
    return reduce(lambda acc, char: (acc * 31 + ord(char)) & 0xFFFFFFFF, token, 0)

tokens = ['def', 'class', 'import', 'lambda', 'return']
filtered_tokens = list(filter(lambda t: len(t) > 4, tokens))
mapped_hashes = list(map(custom_hash, filtered_tokens))
transformed_values = [
    hash_val if hash_val % 2 == 0 else (hash_val >> 2) & 0xFFFFFFFF
    for hash_val in mapped_hashes
]
checksum_components = [
    val if val < 0x80000000 else (val ^ 0xDEADBEEF)
    for val in transformed_values
]
final_checksum = reduce(lambda x, y: (x + y) & 0xFFFFFFFF, checksum_components, 0) if checksum_components else 0
print(f"Result: {final_checksum}")