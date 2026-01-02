from collections import defaultdict

def apply_fee_adjustments():
    # Simulate user transaction records with base fees
    user_fees = defaultdict(float)
    transactions = [
        ('user_123', 'deposit', 500),
        ('user_456', 'withdrawal', 300),
        ('user_123', 'trade', 1000),
        ('user_789', 'deposit', 200),
        ('user_456', 'trade', 750)
    ]

    # Base fee calculation per transaction type
    fee_rates = {
        'deposit': 0.01,
        'withdrawal': 0.02,
        'trade': 0.03
    }

    # Accumulate fees per user
    for user_id, tx_type, amount in transactions:
        if tx_type in fee_rates:
            user_fees[user_id] += amount * fee_rates[tx_type]

    # Apply loyalty discount for users with multiple transactions
    transaction_count = defaultdict(int)
    for user_id, _, _ in transactions:
        transaction_count[user_id] += 1

    adjusted_fees = {}
    for user_id, total_fee in user_fees.items():
        if transaction_count[user_id] > 1:
            adjusted_fees[user_id] = total_fee * 0.9  # 10% discount
        else:
            adjusted_fees[user_id] = total_fee

    # Compute final balance after company absorbs max $5 per user
    total_balance = 0
    for adj_fee in adjusted_fees.values():
        total_balance += min(adj_fee, 5)

    return total_balance

result = apply_fee_adjustments()
print(f"Result: {result}")