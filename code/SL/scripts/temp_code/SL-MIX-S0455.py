import heapq
from functools import wraps

def log_balance_changes(func):
    @wraps(func)
    def wrapper(balance, adjustment):
        new_balance = func(balance, adjustment)
        return new_balance
    return wrapper

@log_balance_changes
def apply_adjustment(balance, adjustment):
    return balance + adjustment

# Initialize transaction min-heap with priority values
transactions = [
    (3, lambda x: x * 1.02),   # Priority 3: 2% gain
    (1, lambda x: x - 100),     # Priority 1: $100 fee
    (2, lambda x: x + 50),      # Priority 2: $50 bonus
    (5, lambda x: x * 0.95),    # Priority 5: 5% loss
    (4, lambda x: x + 200)      # Priority 4: $200 deposit
]

heapq.heapify(transactions)
initial_balance = 1000
ledger_balance = initial_balance
processed_count = 0

while transactions and processed_count < 4:
    priority, adjustment_func = heapq.heappop(transactions)
    
    # Skip if adjustment would result in negative balance
    temp_balance = adjustment_func(ledger_balance)
    if temp_balance < 0:
        continue
    
    # Apply adjustment with logging decorator
    ledger_balance = apply_adjustment(ledger_balance, temp_balance - ledger_balance)
    processed_count += 1
    
    # Early return condition for specific priority
    if priority == 2:
        break

# Additional adjustment outside loop
final_adjustment = lambda x: x - (x % 10)
final_balance = final_adjustment(ledger_balance)

print(f"Result: {final_balance}")