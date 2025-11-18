from collections import deque

def compute_compliance_deficit():
    # Compliance weight calculator using closure
    def create_weight_function(base_rate):
        return lambda risk_level: base_rate * (risk_level ** 2) + (risk_level % 3)
    
    # Transaction tree node definition
    class TransactionNode:
        def __init__(self, id_code, risk_val, children=None):
            self.id_code = id_code
            self.risk_val = risk_val
            self.children = children if children else []
    
    # Build transaction hierarchy
    leaf_a = TransactionNode('TXN-A', 2)
    leaf_b = TransactionNode('TXN-B', 4)
    leaf_c = TransactionNode('TXN-C', 1)
    mid_x = TransactionNode('TXN-X', 3, [leaf_a, leaf_b, leaf_c])
    leaf_d = TransactionNode('TXN-D', 5)
    leaf_e = TransactionNode('TXN-E', 2)
    mid_y = TransactionNode('TXN-Y', 4, [leaf_d, leaf_e])
    root_z = TransactionNode('TXN-Z', 6, [mid_x, mid_y])
    
    # Compliance calculation with stack-based traversal
    compliance_weights = create_weight_function(1.5)
    deficit_accumulator = 0
    traversal_stack = deque([root_z])
    
    # Audit process with recursive-like iterative approach
    while traversal_stack:
        current_node = traversal_stack.pop()
        required_compliance = compliance_weights(current_node.risk_val)
        actual_score = (current_node.risk_val << 1) ^ len(current_node.id_code)
        
        if actual_score < required_compliance:
            deficit_accumulator += int(required_compliance - actual_score)
        
        # Add children to stack (right to left for consistent processing)
        for child in reversed(current_node.children):
            traversal_stack.append(child)
    
    return deficit_accumulator

audit_deficit = compute_compliance_deficit()
print(f"Result: {audit_deficit}")