from collections import defaultdict
import math

def build_tree_from_tokens(tokens):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    
    if not tokens:
        return None
    
    root_val = tokens[0]
    root = Node(root_val)
    queue = [root]
    i = 1
    
    while i < len(tokens) and queue:
        current = queue.pop(0)
        if i < len(tokens):
            current.left = Node(tokens[i])
            queue.append(current.left)
            i += 1
        if i < len(tokens):
            current.right = Node(tokens[i])
            queue.append(current.right)
            i += 1
    return root

def traverse_sum(node):
    if not node:
        return 0
    return node.val + traverse_sum(node.left) + traverse_sum(node.right)

class SentenceEncoder:
    def __init__(self):
        chars = '0123456789abcdefghijklmnopqrstuvwxyz '
        self.char_to_num = {c: i for i, c in enumerate(chars)}
    
    def encode_word(self, word):
        total = 0
        for char in word.lower():
            if char in self.char_to_num:
                total = total * 37 + self.char_to_num[char]
        return total % 1000000

encoder = SentenceEncoder()
sentence = "data structures and algorithms"
tokens = sentence.split()

encoded_values = [encoder.encode_word(token) for token in tokens]
matrix = [[0] * len(encoded_values) for _ in range(len(encoded_values))]
for i in range(len(encoded_values)):
    for j in range(len(encoded_values)):
        matrix[i][j] = encoded_values[i] if i <= j else 0

diagonal_sum = sum(matrix[i][i] for i in range(len(encoded_values)))
adjusted_values = [
    val + diagonal_sum if val % 2 == 0 else val - diagonal_sum
    for val in encoded_values
]

root = build_tree_from_tokens(adjusted_values)
tree_sum = traverse_sum(root)

weight_matrix = [
    [1 if i == j else 0 for j in range(len(adjusted_values))]
    for i in range(len(adjusted_values))
]
weighted_sum = sum(
    adjusted_values[i] * weight_matrix[i][i]
    for i in range(len(adjusted_values))
)

final_score = (
    (tree_sum + weighted_sum) // len(adjusted_values)
    if len(adjusted_values) > 0 else 0
)
print(f"Result: {final_score}")