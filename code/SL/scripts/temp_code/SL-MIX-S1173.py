class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def traverse_and_accumulate(node, multiplier=1):
    if not node:
        return 0
    
    # Process linked list associated with this tree node
    linked_sum = 0
    current = node.val  # This is the head of the linked list
    while current:
        linked_sum += current.val
        current = current.next
    
    # Recursively process children with short-circuit evaluation
    left_val = traverse_and_accumulate(node.left, multiplier*2) if node.left else 0
    right_val = traverse_and_accumulate(node.right, multiplier*3) if node.right else 0
    
    # Combine values using logical operations and arithmetic
    has_children = bool(node.left or node.right)
    base_value = linked_sum * multiplier
    
    # Apply conditional logic with short-circuit evaluation
    adjusted_value = base_value + (left_val or 0) + (right_val or 0) if has_children else base_value
    
    return adjusted_value

# Build the hybrid structure
# Root node with linked list [2, 4, 6]
root_ll = create_linked_list([2, 4, 6])
root = TreeNode(root_ll)

# Left child with linked list [1, 3]
left_ll = create_linked_list([1, 3])
root.left = TreeNode(left_ll)

# Right child with linked list [5, 7, 9]
right_ll = create_linked_list([5, 7, 9])
root.right = TreeNode(right_ll)

# Left-left grandchild with linked list [8]
left_left_ll = create_linked_list([8])
root.left.left = TreeNode(left_left_ll)

# Process the structure
aggregated_bandwidth = traverse_and_accumulate(root)
print(f"Result: {aggregated_bandwidth}")