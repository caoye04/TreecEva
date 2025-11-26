initial_balance = 1000
transaction_log = ["deposit:200", "withdrawal:150", "deposit:300", "withdrawal:50"]

total_deposits = 0
total_withdrawals = 0

for entry in transaction_log:
    if entry.startswith("deposit:"):
        amount = int(entry.split(":")[1])
        total_deposits += amount
    elif entry.startswith("withdrawal:"):
        amount = int(entry.split(":")[1])
        total_withdrawals += amount

final_balance = total_deposits - total_withdrawals + initial_balance
print(f"Result: {final_balance}")