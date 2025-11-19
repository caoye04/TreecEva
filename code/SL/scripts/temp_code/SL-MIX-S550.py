import heapq

class SignalNode:
    def __init__(self, freq=0):
        self.freq = freq
        self.left = None
        self.right = None

def build_signal_tree():
    # Create leaf nodes
    leaves = [SignalNode(12), SignalNode(25), SignalNode(36), SignalNode(48)]
    
    # Level 1 internal nodes
    node1 = SignalNode()
    node1.left = leaves[0]
    node1.right = leaves[1]
    node1.freq = (node1.left.freq ^ node1.right.freq) >> 1
    
    node2 = SignalNode()
    node2.left = leaves[2]
    node2.right = leaves[3]
    node2.freq = (node2.left.freq ^ node2.right.freq) >> 1
    
    # Root node
    root = SignalNode()
    root.left = node1
    root.right = node2
    root.freq = (root.left.freq ^ root.right.freq) >> 1
    
    return root, leaves

def collect_all_frequencies(node):
    if not node:
        return []
    return [node.freq] + collect_all_frequencies(node.left) + collect_all_frequencies(node.right)

tree_root, leaf_nodes = build_signal_tree()
all_freqs = collect_all_frequencies(tree_root)
max_heap = [-f for f in all_freqs]  # Negative for max-heap behavior
heapq.heapify(max_heap)

max_frequency = -heapq.heappop(max_heap)
leaf_count = len(leaf_nodes)
root_frequency = tree_root.freq

final_signal_strength = root_frequency + (max_frequency * leaf_count)
print(f"Result: {final_signal_strength}")