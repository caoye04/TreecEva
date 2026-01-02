import math
from collections import defaultdict
from statistics import variance

class TreeNode:
    def __init__(self, nucleotide):
        self.nucleotide = nucleotide
        self.value = {'A': 1, 'T': 2, 'G': 3, 'C': 4}[nucleotide]
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_dna_tree():
    # Creating a DNA tree representing: A(T(G,C), G(A,T))
    root = TreeNode('A')
    root.left = TreeNode('T')
    root.right = TreeNode('G')
    root.left.left = TreeNode('G')
    root.left.right = TreeNode('C')
    root.right.left = TreeNode('A')
    root.right.right = TreeNode('T')
    return root

def get_tree_levels(root):
    if not root:
        return []
    levels = defaultdict(list)
    queue = [(root, 0)]
    
    while queue:
        node, level = queue.pop(0)
        levels[level].append(node.value)
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return levels

def create_variance_linked_list(levels):
    head = None
    current = None
    
    for level in sorted(levels.keys()):
        vals = levels[level]
        if len(vals) > 1:
            var = variance(vals)
        else:
            var = 0.0
        
        if not head:
            head = ListNode(var)
            current = head
        else:
            current.next = ListNode(var)
            current = current.next
    
    return head

def generate_fibonacci_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def transform_variances(linked_list):
    values = []
    current = linked_list
    while current:
        values.append(current.val)
        current = current.next
    
    fib_seq = generate_fibonacci_sequence(len(values))
    
    # Apply transformation: value * (fibonacci_index + 1)^2
    transformed = [values[i] * ((i+1)**2) for i in range(len(values))]
    
    return transformed

def main():
    # Build the DNA tree
    dna_tree = build_dna_tree()
    
    # Get values by level
    level_values = get_tree_levels(dna_tree)
    
    # Create linked list of variances
    variance_list = create_variance_linked_list(level_values)
    
    # Transform the variances
    transformed_values = transform_variances(variance_list)
    
    # What is the third element in the transformed sequence?
    third_element = transformed_values[2] if len(transformed_values) > 2 else 0
    
    print(f"Result: {third_element}")

if __name__ == "__main__":
    main()