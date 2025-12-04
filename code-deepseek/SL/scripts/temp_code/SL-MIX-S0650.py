transaction_count = 15
account_balance = 1000
threshold = 10
fee_per_transaction = 5
penalty_rate = 0.1
interest_rate = 0.05
bonus_amount = 50

# Distractor calculations
total_fees = transaction_count * fee_per_transaction
potential_penalty = account_balance * penalty_rate
calculated_interest = account_balance * interest_rate

# Unused intermediate variable
unused_adjustment = total_fees + potential_penalty - bonus_amount

# Core logic with conditional expression
penalty = account_balance * penalty_rate if transaction_count > threshold else 0
bonus = bonus_amount if transaction_count > threshold else 0
interest = account_balance * interest_rate if transaction_count <= threshold else 0

# Final calculation
final_balance = account_balance - penalty + bonus if transaction_count > threshold else account_balance + interest

print(f"Result: {final_balance}")