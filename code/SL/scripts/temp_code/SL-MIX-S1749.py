from collections import defaultdict
import math

def calculate_volatility_adjustment(trade_volume, market_data):
    avg_price = sum(market_data) / len(market_data)
    squared_diffs = [(price - avg_price) ** 2 for price in market_data]
    variance = sum(squared_diffs) / len(squared_diffs)
    return math.sqrt(variance) / avg_price

def compute_transaction_fee(volume, adjustment_factor):
    base_rate = 0.001
    volume_tier = min(0.0005, volume * 0.0000001)
    return base_rate + volume_tier + adjustment_factor * 0.0002

trades = [
    {'id': 'BTC-001', 'volume': 2.5, 'prices': [42000.0, 42100.5, 41980.2]},
    {'id': 'ETH-002', 'volume': 15.3, 'prices': [2800.1, 2820.3, 2795.8]},
    {'id': 'SOL-003', 'volume': 100.0, 'prices': [120.5, 121.0, 119.8]}
]

selected_trades = []
fee_components = defaultdict(float)
total_volume = 0.0

for trade in trades:
    vol_adjustment = calculate_volatility_adjustment(trade['volume'], trade['prices'])
    if vol_adjustment < 0.01:  # Select low-volatility trades
        selected_trades.append(trade)
        total_volume += trade['volume']
        fee_components[trade['id']] = compute_transaction_fee(trade['volume'], vol_adjustment)

# Apply volume-based discount using greedy selection
volume_bonus_pool = total_volume * 0.0001
sorted_trades = sorted(selected_trades, key=lambda x: x['volume'], reverse=True)
discount_allocation = {}
remaining_bonus = volume_bonus_pool

for trade in sorted_trades:
    max_allocatable = min(remaining_bonus, fee_components[trade['id']] * 0.3)
    discount_allocation[trade['id']] = max_allocatable
    remaining_bonus -= max_allocatable

# Calculate final fees with discount
final_fees = {}
for tid in fee_components:
    final_fees[tid] = fee_components[tid] - discount_allocation.get(tid, 0.0)

# Determine optimal fee as weighted average
weighted_sum = 0.0
total_weight = 0.0
for trade in selected_trades:
    tid = trade['id']
    weight = trade['volume']
    weighted_sum += final_fees[tid] * weight
    total_weight += weight

optimal_fee = weighted_sum / total_weight if total_weight > 0 else 0.0
print(f"Result: {optimal_fee}")