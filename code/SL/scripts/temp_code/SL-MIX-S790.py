import heapq
import re
from functools import reduce

class EncodingNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
def build_encoding_tree(tokens):
    if len(tokens) == 1:
        return EncodingNode(tokens[0])
    mid = len(tokens) // 2
    left_subtree = build_encoding_tree(tokens[:mid])
    right_subtree = build_encoding_tree(tokens[mid:])
    node_value = left_subtree.value ^ right_subtree.value
    return EncodingNode(node_value, left_subtree, right_subtree)

def tokenize_string(s):
    # Extract alphanumeric tokens and convert to ASCII sums
    tokens = re.findall(r'[A-Z0-9]+', s)
    ascii_sums = [sum(ord(c) for c in token) for token in tokens]
    return ascii_sums

def process_with_heap(values):
    heap = [-v for v in values]  # Max heap using negative values
    heapq.heapify(heap)
    processed_values = []
    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        combined = first ^ second
        processed_values.append(combined)
        heapq.heappush(heap, -combined)
    if heap:
        processed_values.append(-heap[0])
    return processed_values

def calculate_final_hash(tree_root):
    if not tree_root:
        return 0
    if not tree_root.left and not tree_root.right:
        return tree_root.value
    left_hash = calculate_final_hash(tree_root.left)
    right_hash = calculate_final_hash(tree_root.right)
    return left_hash ^ right_hash ^ tree_root.value

# Main processing pipeline
input_data = "SECURE_DATA_2023"
tokens = tokenize_string(input_data)
heap_processed = process_with_heap(tokens)
encoding_tree = build_encoding_tree(heap_processed)
final_hash = calculate_final_hash(encoding_tree)
print(f"Result: {final_hash}")