import hashlib

def compute_segment_hash(segment):
    return int(hashlib.md5(segment.encode()).hexdigest(), 16) % 10000

def process_geohash_tokens(tokens):
    segment_hashes = [compute_segment_hash(token) for token in tokens]
    transformed_values = [
        (hash_val * 3 + 7) % 1000
        for hash_val in segment_hashes
        if hash_val % 2 == 1
    ]
    even_hash_groups = {
        i: hash_val
        for i, hash_val in enumerate(segment_hashes)
        if hash_val % 2 == 0
    }
    odd_sum = sum(transformed_values)
    grouped_mod_sum = sum(
        (index * val) % 13
        for index, val in even_hash_groups.items()
    )
    aggregated_hash = (odd_sum + grouped_mod_sum) % 997
    return aggregated_hash

tokens = ['locA', 'posB', 'zoneC', 'areaD', 'regionE']
aggregated_hash = process_geohash_tokens(tokens)
print(f'Result: {aggregated_hash}')