from functools import wraps

class TransactionNode:
    def __init__(self, amount):
        self.amount = amount
        self.next = None

def tax_decorator(func):
    @wraps(func)
    def wrapper(amount):
        taxed_amount = func(amount)
        return taxed_amount * 0.9  # 10% tax
    return wrapper

@tax_decorator
def calculate_profit(amount):
    return amount * 1.05  # 5% profit margin

def process_transactions(head):
    profit_map = {}
    current = head
    total = 0.0
    
    while current:
        profit = calculate_profit(current.amount)
        total += profit
        profit_map[current.amount] = profit
        current = current.next
    
    # Apply bonus if more than 3 transactions
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
        
    if count > 3:
        total += sum(profit_map.values()) * 0.02  # 2% bonus
    
    return total

# Build linked list: 100 -> 200 -> 150 -> 300
node1 = TransactionNode(100)
node2 = TransactionNode(200)
node3 = TransactionNode(150)
node4 = TransactionNode(300)
node1.next = node2
node2.next = node3
node3.next = node4

final_profit = process_transactions(node1)
print(f"Result: {final_profit}")