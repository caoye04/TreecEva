account_balance = 1500
interest_rate = 0.05
time_period = 2
overdraft_fee = 25

# Calculate interest earned
interest = account_balance * interest_rate * time_period

# Check for minimum balance violation
minimum_balance = 1000
if account_balance < minimum_balance:
    penalty = overdraft_fee
else:
    penalty = 0

# Final calculation
final_balance = account_balance + interest - penalty
print(f"Result: {final_balance}")