from collections import defaultdict

class ExchangeNode:
    def __init__(self, change, next_node=None):
        self.change = change
        self.next = next_node

def compute_weighted_fib(n, weights):
    if n <= 0:
        return 0
    elif n == 1:
        return weights[0]
    fib = [0] * (n + 1)
    fib[1] = weights[0]
    if n > 1:
        fib[2] = weights[1]
        for i in range(3, n + 1):
            fib[i] = fib[i-1] + fib[i-2] + weights[i-1]
    return fib[n]

exchange_rates = [
    ExchangeNode(2),
    ExchangeNode(-1),
    ExchangeNode(3),
    ExchangeNode(-2),
    ExchangeNode(1)
]

for i in range(len(exchange_rates) - 1):
    exchange_rates[i].next = exchange_rates[i + 1]

rate_map = defaultdict(int)
current = exchange_rates[0]
cumulative_change = 0
visited_count = 0

while current:
    cumulative_change += current.change
    rate_map[visited_count] = cumulative_change
    if cumulative_change > 4:
        break
    current = current.next
    visited_count += 1

weight_list = [rate_map[i] for i in sorted(rate_map.keys())]
final_adjustment = compute_weighted_fib(len(weight_list), weight_list)
print(f"Result: {final_adjustment}")