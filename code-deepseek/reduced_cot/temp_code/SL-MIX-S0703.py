def process_account_transactions(transactions):
    balances = []
    current_balance = 1000
    temp_holder = 0
    
    for idx, (deposit, withdrawal) in enumerate(zip(transactions[::2], transactions[1::2])):
        temp_holder = deposit - withdrawal
        current_balance += temp_holder
        balances.append(current_balance)
        
    # Distractor calculation that doesn't affect final result
    unused_sum = sum(balances[::2]) + len(transactions)
    
    account_totals = [balance * 1.05 for balance in balances]
    final_balance = account_totals[-1]
    print(f"Target result: {final_balance}")

# Main execution
transactions = [500, 200, 300, 150, 700, 400, 100, 50]
process_account_transactions(transactions)