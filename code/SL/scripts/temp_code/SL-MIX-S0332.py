from collections import defaultdict
from functools import wraps

class NucleotideNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def encode_nucleotide(nucleotide):
    encoding_map = {'A': 10, 'T': 20, 'G': 30, 'C': 40}
    return encoding_map.get(nucleotide, 0)

def base_pair_transform(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # Base pairing rule: A-T, G-C with score adjustment
        if result == 30:  # A(10) + T(20)
            return 100
        elif result == 70:  # G(30) + C(40)
            return 200
        return result
    return wrapper

@base_pair_transform
def calculate_pairing_score(node1, node2):
    return node1.value + node2.value

# Initialize doubly-linked list with encoded nucleotides
sequence1 = ['A', 'T', 'G', 'C']
sequence2 = ['T', 'A', 'C', 'G']

head1 = None
prev_node = None
for nuc in sequence1:
    node = NucleotideNode(encode_nucleotide(nuc))
    if head1 is None:
        head1 = node
    else:
        prev_node.next = node
        node.prev = prev_node
    prev_node = node

tail1 = prev_node

head2 = None
prev_node = None
for nuc in sequence2:
    node = NucleotideNode(encode_nucleotide(nuc))
    if head2 is None:
        head2 = node
    else:
        prev_node.next = node
        node.prev = prev_node
    prev_node = node

tail2 = prev_node

# Traverse both lists forward and backward simultaneously
forward_scores = []
node1, node2 = head1, head2
while node1 and node2:
    score = calculate_pairing_score(node1, node2)
    forward_scores.append(score)
    node1 = node1.next
    node2 = node2.next

backward_scores = []
node1, node2 = tail1, tail2
while node1 and node2:
    score = calculate_pairing_score(node1, node2)
    backward_scores.append(score)
    node1 = node1.prev
    node2 = node2.prev

# Perform set operations on scores
fwd_set = frozenset(forward_scores)
bwd_set = frozenset(backward_scores)
common_scores = fwd_set & bwd_set
unique_to_fwd = fwd_set - bwd_set

# Calculate final pairing score
final_pairing_score = sum(common_scores) + len(unique_to_fwd) * max(common_scores)
print(f"Result: {final_pairing_score}")