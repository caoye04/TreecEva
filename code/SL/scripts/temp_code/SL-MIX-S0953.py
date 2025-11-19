class CurrencyNode:
    def __init__(self, currency, rate=1.0):
        self.currency = currency
        self.rate = rate
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

# Build the currency tree
usd = CurrencyNode('USD')
eur = CurrencyNode('EUR', 0.85)
jpy = CurrencyNode('JPY', 110.0)
gbp = CurrencyNode('GBP', 0.75)
aud = CurrencyNode('AUD', 1.35)
cad = CurrencyNode('CAD', 1.25)

usd.add_child(eur)
usd.add_child(jpy)
usd.add_child(gbp)
eur.add_child(aud)
eur.add_child(cad)
jpy.add_child(aud)
jpy.add_child(cad)
gbp.add_child(aud)
gbp.add_child(cad)

def find_max_profit_path(node, depth=0, current_product=1.0):
    if depth == 3:
        return current_product
    
    max_profit = 0
    for child in node.children:
        profit = find_max_profit_path(child, depth + 1, current_product * child.rate)
        if profit > max_profit:
            max_profit = profit
    return max_profit

# Using list comprehension to calculate profits for all paths of depth 3
all_paths_profits = [
    find_max_profit_path(child, 1, child.rate)
    for child in usd.children
]

# Greedy selection of maximum profit
max_arbitrage_profit = max(all_paths_profits)
print(f'Result: {max_arbitrage_profit}')