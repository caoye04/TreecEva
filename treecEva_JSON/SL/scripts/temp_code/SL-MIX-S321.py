class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def parse_header_fields(header_str):
    tokens = header_str.split('|')
    fields = []
    for token in tokens:
        if token.startswith('0x'):
            fields.append(int(token, 16))
        else:
            fields.append(int(token))
    return fields

def build_binary_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            node.left = TreeNode(values[i])
            queue.append(node.left)
            i += 1
        if i < len(values):
            node.right = TreeNode(values[i])
            queue.append(node.right)
            i += 1
    return root

def traverse_and_xor(root):
    if not root:
        return 0
    result = root.val
    if root.left:
        result ^= traverse_and_xor(root.left)
    if root.right:
        result ^= traverse_and_xor(root.right)
    return result

def build_linked_list(values):
    if not values:
        return None
    head = LinkedListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = LinkedListNode(val)
        current = current.next
    return head

def linked_list_sum_mod(head, mod):
    total = 0
    current = head
    while current:
        total = (total + current.val) % mod
        current = current.next
    return total

def compute_custom_checksum(header_string):
    # Parse header fields
    fields = parse_header_fields(header_string)
    
    # Build binary tree from first half of fields
    mid = len(fields) // 2
    tree_root = build_binary_tree(fields[:mid])
    
    # Traverse tree and apply XOR operation
    tree_xor_result = traverse_and_xor(tree_root)
    
    # Build linked list from second half of fields
    linked_list_head = build_linked_list(fields[mid:])
    
    # Compute sum of linked list values modulo 256
    list_sum_mod = linked_list_sum_mod(linked_list_head, 256)
    
    # Apply bitwise operations
    intermediate = (tree_xor_result << 2) & 0xFF  # Left shift by 2 and mask to 8 bits
    intermediate |= list_sum_mod  # Bitwise OR with list sum
    
    # String transformation
    hex_str = hex(intermediate)[2:]  # Remove '0x' prefix
    transformed_str = ''.join(reversed(hex_str))  # Reverse the string
    
    # Convert back to integer
    final_value = int(transformed_str, 16) if transformed_str else 0
    
    # Final modular arithmetic
    final_checksum = (final_value * 17 + 23) % 1000
    
    return final_checksum

# Main execution
packet_header = "0x1A|0x2B|0x3C|0x4D|123|456|789|101"
final_checksum = compute_custom_checksum(packet_header)
print(f"Result: {final_checksum}")