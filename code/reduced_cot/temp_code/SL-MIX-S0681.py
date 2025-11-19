import hashlib
import base64

class TreeNode:
    def __init__(self, encoded_data, left=None, right=None):
        self.encoded_data = encoded_data
        self.left = left
        self.right = right
    
    def decode_payload(self):
        # Custom decoding: reverse, then base64 decode, then take ASCII sum
        reversed_data = self.encoded_data[::-1]
        try:
            decoded_bytes = base64.b64decode(reversed_data)
            return sum(decoded_bytes)
        except:
            return 0

def calculate_subtree_hash(node):
    if not node:
        return 0
    left_hash = calculate_subtree_hash(node.left)
    right_hash = calculate_subtree_hash(node.right)
    node_value = node.decode_payload()
    # Combine with floating point arithmetic
    combined = (left_hash * 1.5) + (right_hash * 2.5) + (node_value * 0.7)
    return int(combined)

# Manuscript tree construction
manuscript_leaf_a = TreeNode("==QkVUUw==")  # Decodes to "STUB"
manuscript_leaf_b = TreeNode("==VFRJTQ==")  # Decodes to "MITT"
manuscript_leaf_c = TreeNode("==U1RBUg==")  # Decodes to "RATS"
manuscript_leaf_d = TreeNode("==VEVORQ==")  # Decodes to "ENET"

manuscript_internal_1 = TreeNode("==SEFS")  # Decodes to "RAFH"
manuscript_internal_1.left = manuscript_leaf_a
manuscript_internal_1.right = manuscript_leaf_b

manuscript_internal_2 = TreeNode("==VE9P")  # Decodes to "OORT"
manuscript_internal_2.left = manuscript_leaf_c
manuscript_internal_2.right = manuscript_leaf_d

manuscript_root = TreeNode("==SEFOTQ==")  # Decodes to "MNATH"
manuscript_root.left = manuscript_internal_1
manuscript_root.right = manuscript_internal_2

# Hash computation using dictionary comprehension for weight mapping
subtree_weights = {"left": 1.2, "right": 1.8}
raw_hashes = {
    'left': calculate_subtree_hash(manuscript_root.left),
    'right': calculate_subtree_hash(manuscript_root.right),
    'root': manuscript_root.decode_payload()
}

weighted_hash_components = {k: v * subtree_weights.get(k, 1.0) for k, v in raw_hashes.items() if k != 'root'}
combined_weighted_hash = sum(weighted_hash_components.values())

# Final checksum incorporates root node and matrix transformation
transformation_matrix = [
    [1.1, 2.2],
    [3.3, 4.4]
]
matrix_product = transformation_matrix[0][0] * transformation_matrix[1][1] - transformation_matrix[0][1] * transformation_matrix[1][0]

final_checksum = int((combined_weighted_hash + raw_hashes['root']) * matrix_product)

print(f"Result: {final_checksum}")