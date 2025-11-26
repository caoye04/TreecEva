transactions = [150, -75, 200, -50, 100]
fee_percentage = 0.02
processed_transactions = [amt * (1 - fee_percentage) if amt > 0 else amt for amt in transactions]
final_balance = sum(processed_transactions)
print(f"Final balance: {final_balance}")