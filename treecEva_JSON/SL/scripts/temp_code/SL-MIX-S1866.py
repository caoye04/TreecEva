from collections import deque
import math

class TransactionNode:
    def __init__(self, batch_id, amount, children=None):
        self.batch_id = batch_id
        self.amount = amount
        self.children = children if children else []

def audit_transactions(root_node):
    validation_stack = []
    compliance_score = 0
    batch_queue = deque([root_node])
    
    while batch_queue:
        current_batch = batch_queue.popleft()
        
        # Short-circuit evaluation for high-value suspicious transactions
        is_suspicious = current_batch.amount > 10000 and (
            len(current_batch.children) == 0 or 
            any(child.amount > 5000 for child in current_batch.children)
        )
        
        if not is_suspicious:
            validation_stack.append(current_batch.amount)
            batch_queue.extend(current_batch.children)
        
        # Process stack when it reaches certain depth
        if len(validation_stack) >= 3:
            batch_total = sum(validation_stack[-3:])
            if batch_total % 7 == 0:  # Compliance check
                compliance_score += math.floor(batch_total / 1000)
            validation_stack = validation_stack[:-3]
    
    # Final compliance adjustment
    while validation_stack:
        remaining_total = sum(validation_stack[-min(3, len(validation_stack)):])
        if remaining_total > 15000 and remaining_total < 25000:
            compliance_score += 5
        validation_stack = validation_stack[:-min(3, len(validation_stack))]
    
    return compliance_score

# Audit tree construction
root = TransactionNode('BATCH_001', 12000)
child1 = TransactionNode('BATCH_002', 8000)
child2 = TransactionNode('BATCH_003', 15000)
child3 = TransactionNode('BATCH_004', 3000)
child4 = TransactionNode('BATCH_005', 6000)

root.children = [child1, child2]
child1.children = [child3, child4]
child2.children = [TransactionNode('BATCH_006', 4500)]

compliance_score = audit_transactions(root)
print(f"Result: {compliance_score}")