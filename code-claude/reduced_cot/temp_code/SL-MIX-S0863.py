def calculate_fees(amount, tier):
    base_fees = {'premium': 0.01, 'standard': 0.02, 'basic': 0.03}
    discount_factor = 0.95 if amount > 1000 else 1.0
    
    # Calculate fee with potential discount
    return amount * base_fees.get(tier, 0.03) * discount_factor

# Initialize account data
account_history = {
    'deposits': [250, 500, 750, 1000],
    'withdrawals': [100, 200, 300],
    'fees_paid': 0
}

# Calculate total deposits with processing bonuses
deposit_bonus = 25
processed_deposits = sum(account_history['deposits']) + deposit_bonus

# Apply loyalty bonus based on account age (months)
account_age = 15
loyalty_multiplier = 1.0 + (account_age / 100)
bonus_adjusted_deposits = processed_deposits * loyalty_multiplier

# Process withdrawals with service charges
withdrawal_charges = calculate_fees(sum(account_history['withdrawals']), 'standard')
total_withdrawals = sum(account_history['withdrawals']) + withdrawal_charges
account_history['fees_paid'] += withdrawal_charges

# Track transactions by ID
active_transactions = {}
transaction_ids = [105, 106, 107, 108]
interest_rates = [0.02, 0.03, 0.025, 0.015]

# Populate transactions with balances
for i, tx_id in enumerate(transaction_ids[:-1]):
    # Calculate transaction balance with interest
    tx_amount = bonus_adjusted_deposits - total_withdrawals
    interest = tx_amount * interest_rates[i]
    
    # Record transaction with interest applied
    active_transactions[tx_id] = tx_amount + interest
    
    # Simulate some activity (doesn't affect final result)
    temp_forecast = tx_amount * (1 + interest_rates[i] * 12)
    seasonal_adjustment = temp_forecast * 0.01

# Add one more special transaction
active_transactions[transaction_ids[-1]] = bonus_adjusted_deposits - total_withdrawals

# Select highest balance transaction
final_balance = active_transactions[max(active_transactions, key=lambda k: active_transactions[k])]

# Apply final processing
rounding_precision = 2
final_balance = round(final_balance, rounding_precision)

print(f"Result: {final_balance}")