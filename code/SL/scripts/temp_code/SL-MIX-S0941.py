account_balance = 850
monthly_interest_rate = 0.015
service_fee = 12.50

# Calculate interest earned
interest = account_balance * monthly_interest_rate

# Calculate final balance
fees = service_fee
final_balance = account_balance + interest - fees

print(f"Result: {final_balance}")