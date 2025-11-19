import re
from collections import defaultdict
import math

class TradeNode:
    def __init__(self, volume, price_change):
        self.volume = volume
        self.price_change = price_change
        self.left = None
        self.right = None

def build_trade_tree(trades):
    if not trades:
        return None
    
    root = TradeNode(trades[0][0], trades[0][1])
    for volume, price_change in trades[1:]:
        current = root
        while True:
            if volume < current.volume:
                if current.left is None:
                    current.left = TradeNode(volume, price_change)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = TradeNode(volume, price_change)
                    break
                else:
                    current = current.right
    return root

def calculate_tree_variance(node):
    if not node:
        return 0, 0, 0  # sum, count, variance_component
    
    left_sum, left_count, left_var = calculate_tree_variance(node.left)
    right_sum, right_count, right_var = calculate_tree_variance(node.right)
    
    total_sum = left_sum + right_sum + node.price_change
    total_count = left_count + right_count + 1
    
    mean = total_sum / total_count if total_count > 0 else 0
    variance_component = left_var + right_var + (node.price_change - mean) ** 2
    
    return total_sum, total_count, variance_component

# Transaction log processing
transaction_log = [
    "TRADE|AAPL|100|150.25",
    "TRADE|GOOGL|50|2800.75",
    "SUSPICIOUS|TSLA|200|950.50",
    "TRADE|MSFT|75|300.00",
    "SUSPICIOUS|AMZN|300|3200.25",
    "TRADE|META|60|220.80"
]

# Parse transactions with regex
parsed_trades = []
suspicious_patterns = 0

for entry in transaction_log:
    match = re.match(r'(\w+)\|(\w+)\|(\d+)\|(\d+\.\d+)', entry)
    if match:
        trade_type, symbol, volume, price = match.groups()
        volume_int = int(volume)
        price_float = float(price)
        
        if trade_type == "SUSPICIOUS":
            suspicious_patterns += 1
        
        # Apply complex calculation to determine price change impact
        price_change_impact = (price_float * volume_int) / 1000.0
        parsed_trades.append((volume_int, price_change_impact))

# Build binary tree from trades
trade_tree = build_trade_tree(parsed_trades)

# Calculate statistical measures
sum_prices, count_trades, variance = calculate_tree_variance(trade_tree)
mean_price_change = sum_prices / count_trades if count_trades > 0 else 0

# Compute suspicion score using multiple factors
suspicion_score = (
    (suspicious_patterns * 2.5) +
    (variance / 10000.0) +
    (mean_price_change / 10.0) +
    math.sqrt(count_trades) * 1.5
)

# Round to 2 decimal places for precision
suspicion_score = round(suspicion_score, 2)

print(f"Result: {suspicion_score}")