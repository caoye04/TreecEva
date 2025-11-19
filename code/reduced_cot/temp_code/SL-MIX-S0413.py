from functools import reduce
from collections import namedtuple

# Define a trade record structure
Trade = namedtuple('Trade', ['volume', 'timestamp'])

# Trade data: volume in USD, timestamp as integer
trades_ledger = [
    Trade(12500, 162345),
    Trade(8750, 162346),
    Trade(15000, 162347),
    Trade(3200, 162348)
]

# Fee tiers: volume threshold -> rate
fee_tiers = [(10000, 0.001), (5000, 0.0015), (0, 0.002)]

def calculate_tiered_rate(trade_volume):
    for threshold, rate in fee_tiers:
        if trade_volume >= threshold:
            return rate
    return fee_tiers[-1][1]  # fallback to lowest tier

# Volume discount function
volume_discount = lambda vol: 0.05 if vol > 10000 else (0.02 if vol > 5000 else 0)

# Compute discounted fees using list comprehension and functional constructs
fees_list = [
    trade.volume * calculate_tiered_rate(trade.volume) * (1 - volume_discount(trade.volume))
    for trade in trades_ledger
]

# Apply greedy reduction to accumulate fees with a bonus adjustment
final_accumulated_fee = reduce(
    lambda acc, fee: acc + fee + (0.0001 if fee > 10 else 0), 
    fees_list, 
    0.0
)

print(f"Result: {round(final_accumulated_fee, 4)}")