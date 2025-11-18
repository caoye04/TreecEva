class TransactionNode:
    def __init__(self, timestamp, value):
        self.timestamp = timestamp
        self.value = value
        self.left = None
        self.right = None

class TransactionTree:
    def __init__(self):
        self.root = None
    
    def insert(self, timestamp, value):
        if not self.root:
            self.root = TransactionNode(timestamp, value)
        else:
            self._insert_recursive(self.root, timestamp, value)
    
    def _insert_recursive(self, node, timestamp, value):
        if timestamp < node.timestamp:
            if node.left is None:
                node.left = TransactionNode(timestamp, value)
            else:
                self._insert_recursive(node.left, timestamp, value)
        else:
            if node.right is None:
                node.right = TransactionNode(timestamp, value)
            else:
                self._insert_recursive(node.right, timestamp, value)

def extract_transactions_in_order(node):
    result = []
    if node:
        result.extend(extract_transactions_in_order(node.left))
        result.append((node.timestamp, node.value))
        result.extend(extract_transactions_in_order(node.right))
    return result

def performance_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class DatabaseManager:
    def __init__(self):
        self.transactions = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    @performance_logger
    def add_transaction(self, timestamp, value):
        self.transactions.append((timestamp, value))

# Initialize components
transaction_tree = TransactionTree()
initial_balance = 1000

# Add transactions using context manager
with DatabaseManager() as db:
    transactions_data = [
        (100, -50),
        (200, 150),
        (50, 200),
        (300, -100),
        (250, 75),
        (150, -25),
        (75, 100)
    ]
    
    for timestamp, value in transactions_data:
        db.add_transaction(timestamp, value)
        transaction_tree.insert(timestamp, value)

# Extract transactions in chronological order
ordered_transactions = extract_transactions_in_order(transaction_tree.root)

# Apply greedy selection: only take positive value transactions
selected_values = [value for _, value in ordered_transactions if value > 0]

# Sort selected values in descending order for maximum gain
selected_values.sort(reverse=True)

# Calculate final balance with a bitwise adjustment
final_balance = initial_balance
for i, value in enumerate(selected_values):
    if i & 1:  # Odd indices
        final_balance += value << 1  # Left shift (multiply by 2)
    else:  # Even indices
        final_balance += value

print(f"Result: {final_balance}")