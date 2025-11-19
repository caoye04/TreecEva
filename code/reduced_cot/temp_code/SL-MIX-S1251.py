class PermissionNode:
    def __init__(self, mask, next_node=None):
        self.mask = mask
        self.next = next_node

def build_permission_chain():
    # Create nodes with specific permission masks
    node3 = PermissionNode(0b11010010)
    node2 = PermissionNode(0b10110101, node3)
    node1 = PermissionNode(0b01101100, node2)
    head = PermissionNode(0b10011011, node1)
    return head

def compute_access_token(chain_head, master_key):
    current = chain_head
    cumulative_mask = 0
    
    while current:
        cumulative_mask ^= current.mask
        current = current.next
    
    final_token = cumulative_mask & master_key
    return final_token

# Build the permission chain
permission_chain = build_permission_chain()

# Master key for final validation
security_master_key = 0b11110000

# Compute the final access token
access_token = compute_access_token(permission_chain, security_master_key)
print(f"Result: {access_token}")