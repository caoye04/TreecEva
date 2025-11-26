from collections import Counter

def process_financial_transactions():
    account_balance = 1500
    transactions = [45, -120, 300, -75, 80, -25]
    
    # Distractor: Processing transaction types that won't be used
    transaction_types = Counter(['deposit', 'withdrawal', 'deposit', 'fee', 'deposit', 'withdrawal'])
    deposit_count = transaction_types['deposit']
    withdrawal_count = transaction_types['withdrawal']
    
    # Distractor: Calculating average transaction (not used in final result)
    total_transactions = sum(transactions)
    avg_transaction = total_transactions / len(transactions)
    
    # Relevant: Filter only positive transactions
    positive_transactions = [t for t in transactions if t > 0]
    
    # Distractor: Complex calculation that doesn't affect final result
    temp_sum = sum([x * 2 for x in transactions]) - account_balance
    
    # Key calculation for final result
    transaction_sum = sum(positive_transactions)
    final_balance = account_balance + transaction_sum
    
    print(f"Target result: {final_balance}")

process_financial_transactions()