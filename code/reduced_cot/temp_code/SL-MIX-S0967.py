transactions = [150, -45, 200, -30, 75, -20]
account_data = {
    "savings": {"balance": 1000, "rate": 0.02},
    "checking": {"balance": 500, "rate": 0.01},
    "investment": {"balance": 2000, "rate": 0.05}
}

primary_account = "checking"
processed_transactions = []
temporary_hold = 0

for amount in transactions:
    if amount > 0:
        account_data[primary_account]["balance"] += amount
    else:
        account_data[primary_account]["balance"] -= abs(amount)
    
    processed_transactions.append(amount)
    temporary_hold = amount * 0.1

account_data["savings"]["balance"] += account_data["savings"]["rate"] * account_data["savings"]["balance"]
account_data["investment"]["balance"] += account_data["investment"]["rate"] * account_data["investment"]["balance"]

final_balance = account_data[primary_account]["balance"]
print(f"Result: {final_balance}")