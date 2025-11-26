def process_transactions(transactions):
    balance = 100
    for transaction in transactions:
        balance += transaction
    return balance

account_data = [25, -10, 15, -5, 30]
initial_funds = 50
backup_data = [-20, 35]

final_balance = process_transactions(account_data)
print(f"Result: {final_balance}")