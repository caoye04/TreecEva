class TransactionNode:
    def __init__(self, amount, flagged=False):
        self.amount = amount
        self.flagged = flagged
        self.next = None

def build_transaction_chain():
    # Chain: 100 -> 200(f) -> 150 -> 300 -> 50(f) -> 400
    head = TransactionNode(100)
    head.next = TransactionNode(200, True)
    head.next.next = TransactionNode(150)
    head.next.next.next = TransactionNode(300)
    head.next.next.next.next = TransactionNode(50, True)
    head.next.next.next.next.next = TransactionNode(400)
    return head

class AuditContext:
    def __init__(self):
        self.correction_log = {}
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def apply_correction(self, amount):
        # Apply 10% correction to non-flagged transactions
        return amount * 1.1

def process_transactions(chain_head):
    balance = 0
    correction_threshold = 500
    corrections_applied = 0
    
    with AuditContext() as audit:
        current = chain_head
        while current:
            if not current.flagged and corrections_applied < 3:
                corrected_amount = audit.apply_correction(current.amount)
                balance += corrected_amount
                corrections_applied += 1
                # Log correction
                audit.correction_log[current.amount] = corrected_amount
            else:
                balance += current.amount
            current = current.next
        
        # Merge with base adjustments dictionary
        base_adjustments = {100: 110, 200: 200, 150: 165}
        merged_adjustments = {**base_adjustments, **audit.correction_log}
        
        # Calculate final adjustment using arithmetic operations
        adjustment_factor = (len(merged_adjustments) & 0b111) ^ 0b101  # Bitwise operations
        adjusted_balance = balance + (adjustment_factor * 10)
        
    return adjusted_balance

# Main execution
transaction_chain = build_transaction_chain()
adjusted_balance = process_transactions(transaction_chain)
print(f"Result: {adjusted_balance}")