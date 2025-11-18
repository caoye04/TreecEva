from functools import reduce

class TransactionNode:
    def __init__(self, symbol, gain_loss, volume):
        self.symbol = symbol
        self.gain_loss = gain_loss
        self.volume = volume
        self.left = None
        self.right = None

def build_transaction_tree():
    root = TransactionNode('AAPL', -1500, 100)
    root.left = TransactionNode('GOOGL', 2300, 50)
    root.right = TransactionNode('TSLA', -800, 200)
    root.left.left = TransactionNode('MSFT', -1200, 75)
    root.left.right = TransactionNode('AMZN', 900, 60)
    root.right.left = TransactionNode('NVDA', -2100, 150)
    return root

def collect_harvestable_transactions(node):
    if not node:
        return []
    
    harvestable = []
    # Logical conditions for tax-loss harvesting
    if node.gain_loss < 0 and node.volume > 60:
        harvestable.append(node)
    
    harvestable += collect_harvestable_transactions(node.left)
    harvestable += collect_harvestable_transactions(node.right)
    return harvestable

def calculate_weighted_loss(transactions):
    # Using functional programming to calculate weighted losses
    losses = list(map(lambda t: abs(t.gain_loss) * (t.volume / 100), transactions))
    return losses

tree_root = build_transaction_tree()
harvestable_transactions = collect_harvestable_transactions(tree_root)

# Apply additional filtering using logical operations
qualified_for_harvest = list(filter(lambda t: t.symbol != 'NVDA' or t.gain_loss < -2000, harvestable_transactions))

weighted_losses = calculate_weighted_loss(qualified_for_harvest)

# Sort using a custom algorithm (bubble sort implementation)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_losses = bubble_sort(weighted_losses.copy())

# Calculate total using reduce
harvested_loss_total = reduce(lambda x, y: x + y, sorted_losses, 0)

print(f'Result: {harvested_loss_total}')