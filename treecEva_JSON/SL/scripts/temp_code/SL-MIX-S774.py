import heapq
from collections import defaultdict

class TokenNode:
    def __init__(self, token_type, frequency, left=None, right=None):
        self.token_type = token_type
        self.frequency = frequency
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.frequency < other.frequency

# Configuration string for tokenization
config_string = "VAR ASSIGN NUMBER SEMICOLON VAR ASSIGN STRING SEMICOLON IF LPAREN IDENTIFIER RPAREN LBRACE RBRACE"
tokens = config_string.split()

# Step 1: Build frequency map using dictionary comprehension
frequency_map = {token: tokens.count(token) for token in set(tokens)}

# Step 2: Create a min-heap of (frequency, token) for rare token prioritization
min_heap = [(freq, tok) for tok, freq in frequency_map.items()]
heapq.heapify(min_heap)

# Step 3: Extract two rarest tokens and compute a semantic score
if len(min_heap) >= 2:
    freq1, token1 = heapq.heappop(min_heap)
    freq2, token2 = heapq.heappop(min_heap)
    semantic_priority_score = (hash(token1) % 100) * freq1 + (hash(token2) % 100) * freq2
else:
    semantic_priority_score = 0

# Step 4: Construct a binary tree from remaining heap elements
node_heap = [TokenNode(tok, freq) for freq, tok in min_heap]
heapq.heapify(node_heap)

while len(node_heap) > 1:
    left = heapq.heappop(node_heap)
    right = heapq.heappop(node_heap)
    merged_freq = left.frequency + right.frequency
    merged_node = TokenNode('INTERNAL', merged_freq, left, right)
    heapq.heappush(node_heap, merged_node)

final_tree_root = node_heap[0] if node_heap else None

# Final adjustment to semantic score based on tree depth
def calculate_depth(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return 1 + max(calculate_depth(node.left), calculate_depth(node.right))

tree_depth = calculate_depth(final_tree_root)
semantic_priority_score += tree_depth * 10

print(f"Result: {semantic_priority_score}")