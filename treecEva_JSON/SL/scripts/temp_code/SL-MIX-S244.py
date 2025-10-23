from collections import deque
from functools import reduce

class TransactionLogger:
    def __init__(self, func):
        self.func = func
        self.log = []
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.log.append(result)
        return result

@TransactionLogger
def process_correction(value, rate=1.05):
    return value * rate

def apply_reversals(transactions_stack):
    reversed_amount = 0.0
    while transactions_stack:
        transaction = transactions_stack.pop()
        reversed_amount += transaction * 0.02
    return reversed_amount

# Initialize account state
account_balance = 1000.0
recent_corrections = deque([200.0, -50.0, 125.5, -30.25])
suspicious_transactions = [150.0, 75.0, 200.0]

# Process corrections from queue
while recent_corrections:
    correction = recent_corrections.popleft()
    account_balance += process_correction(correction)

# Apply reversals from stack
reversal_stack = deque(suspicious_transactions)
account_balance -= apply_reversals(reversal_stack)

# Final adjustment using functional approach
adjustments = [1.02, 0.98, 1.01]
compound_factor = reduce(lambda x, y: x * y, adjustments)
account_balance = account_balance * compound_factor

print(f"Result: {account_balance}")