account_balances = [1200, 850, 2100, 430, 1600]
interest_rates = [0.02, 0.015, 0.025, 0.01, 0.018]

# Initialize tracking variables
base_total = sum(account_balances)
total_balance = 0

# Process each account with interest calculation
for i, account in enumerate(account_balances):
    interest_amount = account * interest_rates[i]
    total_balance += account + interest_amount

# Final output
print(f"Total balance: {total_balance}")