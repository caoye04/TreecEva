class TransactionNode:
    def __init__(self, amount=0):
        self.amount = amount
        self.next = None

class AuditLogger:
    def __enter__(self):
        self.log = []
        return self
    
    def record(self, entry):
        self.log.append(entry)
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def calculate_adjustments(transactions_head):
    correction_factors = {100: 0.95, 200: 0.90, 300: 0.85}
    default_factor = 0.98
    
    total_discrepancy = 0
    current = transactions_head
    
    with AuditLogger() as logger:
        while current:
            base_amount = current.amount
            factor = correction_factors.get(base_amount, default_factor)
            adjusted_amount = base_amount * factor
            
            if adjusted_amount > 100 and adjusted_amount < 300:
                adjusted_amount *= 1.1
            elif adjusted_amount >= 300:
                adjusted_amount *= 0.95
            
            if not (adjusted_amount < 50):
                total_discrepancy += adjusted_amount
            
            logger.record(f"Processed {base_amount} -> {adjusted_amount}")
            current = current.next
    
    # Apply final corrections
    high_value_bonus = 25 if total_discrepancy > 500 else 0
    final_adjustment = total_discrepancy + high_value_bonus
    
    return final_adjustment

# Setup transaction chain
head = TransactionNode(150)
head.next = TransactionNode(250)
head.next.next = TransactionNode(75)
head.next.next.next = TransactionNode(320)

final_adjustment = calculate_adjustments(head)
print(f"Result: {final_adjustment}")