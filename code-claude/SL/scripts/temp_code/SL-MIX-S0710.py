def calculate_interest(amount):
    # Calculate simple interest at 5%
    return amount * 0.05

def calculate_final_balance(transactions):
    # Start with zero balance
    balance = 0
    
    # Track the number of deposits and withdrawals
    deposit_count = 0
    withdrawal_count = 0
    
    # Process each transaction with its index
    for i, transaction in enumerate(transactions):
        if transaction > 0:
            # Deposit: add to balance
            balance += transaction
            deposit_count += 1
        else:
            # Withdrawal: subtract from balance
            balance += transaction  # transaction is negative
            withdrawal_count += 1
            
    # Calculate interest on final balance
    interest = calculate_interest(balance)
    
    # Apply bonus for having more deposits than withdrawals
    bonus = 10 if deposit_count > withdrawal_count else 0
    
    # Return final balance with interest and bonus
    return balance + interest + bonus

# Customer transaction history (positive = deposit, negative = withdrawal)
customer_transactions = [100, -20, 50, -30, 75]

# Calculate the final balance for the customer
total_balance = calculate_final_balance(customer_transactions)

print(f"Result: {total_balance}")