accounts = {"checking": 1250, "investment": 3200, "credit": -150}

# Calculate total balance from relevant accounts
temp_sum = accounts.get("checking", 0) + accounts.get("investment", 0)
final_balance = accounts.get("savings", 0) + accounts.get("checking", 0)

print(f"Target result: {final_balance}")