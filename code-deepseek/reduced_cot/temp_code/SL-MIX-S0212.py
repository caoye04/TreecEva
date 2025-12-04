account_active = True
current_balance = 1500
monthly_deposit = 300
monthly_fee = 25
inactive_penalty = 100

# Main account calculation
final_balance = (current_balance + monthly_deposit - monthly_fee) if account_active else 0

print(f"Target result: {final_balance}")