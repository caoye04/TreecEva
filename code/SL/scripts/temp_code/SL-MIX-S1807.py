class TransactionNode:
    def __init__(self, rate, next_node=None):
        self.rate = rate
        self.next = next_node

def calculate_profit(chain_head, accumulated=1.0):
    if not chain_head:
        return accumulated
    new_accumulated = accumulated * chain_head.rate
    if new_accumulated > 1.2:
        new_accumulated *= 0.9  # 10% tax
    return calculate_profit(chain_head.next, new_accumulated)

# Linked list of currency conversion rates
head = TransactionNode(1.05)
head.next = TransactionNode(1.02)
head.next.next = TransactionNode(0.98)
head.next.next.next = TransactionNode(1.04)

# Dictionary comprehension for currency mapping
base_rates = {'USD_EUR': 1.05, 'EUR_GBP': 1.02, 'GBP_JPY': 0.98}
updated_rates = {pair: rate * 1.01 for pair, rate in base_rates.items()}
merged_rates = {**base_rates, **updated_rates}

# Greedy selection of profitable paths
is_profitable = lambda x: x > 1.0
profit_chain = [rate for rate in merged_rates.values() if is_profitable(rate)]

# Construct new linked list from profitable rates
new_head = None
for rate in reversed(profit_chain):
    new_head = TransactionNode(rate, new_head)

# Compute final gain with recursive backtracking and ternary logic
raw_gain = calculate_profit(new_head)
final_arbitrage_gain = raw_gain if raw_gain > 1.0 else 0

print(f'Result: {round(final_arbitrage_gain, 4)}')