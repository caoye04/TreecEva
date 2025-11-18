import re
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def sum_range_bst(root, low, high):
    if not root:
        return 0
    if root.val < low:
        return sum_range_bst(root.right, low, high)
    if root.val > high:
        return sum_range_bst(root.left, low, high)
    return root.val + sum_range_bst(root.left, low, high) + sum_range_bst(root.right, low, high)

# Transaction log entries
log_entries = [
    "TXN-INFO: User123 spent $1,204.99 on 2023-04-01",
    "TXN-INFO: User456 earned $20,000.00 bonus on 2023-04-02",
    "TXN-WARN: Suspicious activity $5,555.55 detected for User789",
    "TXN-INFO: User101 paid $99.99 for service subscription",
    "TXN-CRIT: Anomalous withdrawal $100,000.00 flagged"
]

# Parse and extract monetary values
pattern = r'\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)'
transaction_values = []
for entry in log_entries:
    matches = re.findall(pattern, entry)
    for match in matches:
        # Remove commas and convert to float
        value = float(match.replace(',', ''))
        transaction_values.append(value)

# Initialize min-heap for transaction values
heap = []
for val in transaction_values:
    heapq.heappush(heap, val)

# Build BST from heap values
bst_root = None
heap_copy = heap[:]
while heap_copy:
    val = heapq.heappop(heap_copy)
    bst_root = insert_into_bst(bst_root, val)

# Calculate anomaly score using lambda and dictionary comprehension
threshold_map = {val: val > 10000 for val in transaction_values}
anomaly_weights = {val: 2 if is_large else 1 for val, is_large in threshold_map.items()}
anomaly_score = sum(val * weight for val, weight in anomaly_weights.items() if val > 1000)

# Apply pattern-based penalty using regex matching count
penalty_count = sum(1 for entry in log_entries if re.search(r'TXN-(WARN|CRIT)', entry))
anomaly_score *= penalty_count

print(f"Result: {anomaly_score}")