from collections import Counter

initial_deposit = 1000
monthly_fees = [25, 25, 30, 25]
transaction_logs = ['deposit:500', 'withdraw:200', 'deposit:300', 'fee:25', 'deposit:150', 'withdraw:100']

# Process transactions
account_operations = [initial_deposit]
current_balance = initial_deposit

for transaction in transaction_logs:
    operation, amount = transaction.split(':')
    amount = int(amount)
    
    # Distractor: Count transaction types but don't use the result
    transaction_counter = Counter([t.split(':')[0] for t in transaction_logs])
    
    if operation == 'deposit':
        current_balance += amount
    elif operation == 'withdraw':
        current_balance -= amount
    elif operation == 'fee':
        current_balance -= amount
    
    # Distractor: Calculate average but don't use it
    avg_transaction = sum([int(t.split(':')[1]) for t in transaction_logs]) / len(transaction_logs)
    
    account_operations.append(current_balance)

# Distractor: Process fees but result is overridden
fee_total = sum(monthly_fees)
temp_adjusted = account_operations[-1] - fee_total

# Key statement
final_balance = account_operations[-1]
print(f"Result: {final_balance}")