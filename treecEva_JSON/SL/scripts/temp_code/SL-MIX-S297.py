import hashlib
from collections import defaultdict

tokens = ['lambda', 'yield', 'async', 'await', 'global']
node_weights = defaultdict(int)

# Tree construction with hash-based node IDs
def compute_node_id(token, level):
    hash_obj = hashlib.md5((token + str(level)).encode())
    return int(hash_obj.hexdigest(), 16) % 100

def calculate_leaf_score(token):
    score = 0
    for char in token:
        char_code = ord(char)
        # Bitwise operations for score computation
        score ^= (char_code << 2) & 0xFF
        score |= char_code >> 1
    return score

# Build 3-level tree
for token in tokens:
    level1_id = compute_node_id(token, 1)
    level2_id = compute_node_id(token, 2)
    level3_id = compute_node_id(token, 3)
    
    # Ternary operator to determine if node is leaf
    is_leaf = True if level3_id % 3 == 0 else False
    
    if is_leaf:
        leaf_score = calculate_leaf_score(token)
        node_weights[level3_id] += leaf_score
    else:
        node_weights[level2_id] += len(token)

# Final aggregation using set operations
unique_weights = frozenset(node_weights.values())
final_score = sum(unique_weights) if len(unique_weights) > 3 else 0

print(f"Result: {final_score}")