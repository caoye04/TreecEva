account_balances = {
    'savings': 1500,
    'checking': 800,
    'investment': 2500
}

interest_rates = {
    'savings': 0.02,
    'checking': 0.01,
    'investment': 0.035
}

# Find account with highest interest rate
highest_interest_account = max(interest_rates, key=interest_rates.get)

# Calculate final balance after interest
final_balance = account_balances[highest_interest_account] * (1 + interest_rates[highest_interest_account])

print(f"Target result: {final_balance}")