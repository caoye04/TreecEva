import hashlib
from functools import reduce

def encode_fragment(fragment, position):
    combined = f"{fragment}:{position}".encode('utf-8')
    return hashlib.sha256(combined).hexdigest()[:8]

def filter_valid_fragments(fragments):
    return [f for f in fragments if 'N' not in f]

def map_to_indices(fragments):
    return [(frag, sum(ord(c) for c in frag) % 100) for frag in fragments]

def sort_by_hashed_index(data_tuples):
    return sorted(data_tuples, key=lambda x: encode_fragment(x[0], x[1]))

# Initial DNA sequence fragments
raw_fragments = ['ATCG', 'GCAT', 'NNNN', 'CCGG', 'TAGC', 'AAAA']

# Step 1: Filter out invalid fragments containing 'N'
valid_fragments = filter_valid_fragments(raw_fragments)

# Step 2: Map fragments to index values based on ASCII sum
indexed_fragments = map_to_indices(valid_fragments)

# Step 3: Sort by custom hash of fragment and index
sorted_data = sort_by_hashed_index(indexed_fragments)

# Step 4: Generate signature from sorted hashes
hash_chain = [encode_fragment(frag, idx) for frag, idx in sorted_data]
final_index_signature = reduce(lambda acc, h: acc ^ int(h, 16), hash_chain, 0)

print(f"Result: {final_index_signature}")