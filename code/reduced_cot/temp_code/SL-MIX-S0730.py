from collections import defaultdict
import math

def tokenize_transaction(log_entry):
    return log_entry.replace('$', '').split()

def calculate_adjustment(tokens):
    symbol = tokens[0]
    quantity = int(tokens[1])
    price = float(tokens[2])
    adjustment_factor = 1.0
    if quantity > 100:
        adjustment_factor += 0.05
    elif quantity < 50:
        adjustment_factor -= 0.02
    return price * quantity * adjustment_factor

def process_portfolio(transactions):
    portfolio_yield = 0.0
    volume_tracker = defaultdict(int)
    
    for entry in transactions:
        components = tokenize_transaction(entry)
        asset_symbol = components[0]
        qty = int(components[1])
        volume_tracker[asset_symbol] += qty
        
        if volume_tracker[asset_symbol] >= 200:
            adjustment = calculate_adjustment(components)
            portfolio_yield += adjustment
            volume_tracker[asset_symbol] = 0  # Reset after threshold
        else:
            base_value = float(components[2]) * int(components[1])
            portfolio_yield += base_value
    
    # Apply final market condition modifier
    market_sentiment = sum(1 for v in volume_tracker.values() if v > 75)
    if market_sentiment >= 2:
        portfolio_yield *= 1.03
    
    return round(portfolio_yield, 2)

# Transaction log entries
ledger = [
    "AAPL 150 $150.25",
    "GOOGL 75 $2800.50",
    "AAPL 60 $152.00",
    "TSLA 200 $950.75",
    "GOOGL 125 $2810.00"
]

final_yield = process_portfolio(ledger)
print(f"Result: {final_yield}")