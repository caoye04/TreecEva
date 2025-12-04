def process_transactions(log):
    # Filter transactions and apply fee calculation
    valid_transactions = list(filter(lambda x: x['status'] == 'completed', log))
    total_fees = sum(map(lambda t: t['amount'] * 0.02, valid_transactions))
    return round(total_fees, 2)

transaction_log = [
    {'amount': 150, 'status': 'completed'},
    {'amount': 200, 'status': 'pending'},
    {'amount': 75, 'status': 'completed'},
    {'amount': 300, 'status': 'completed'}
]

# Process the transaction log to calculate total fees
final_output = process_transactions(transaction_log)
print(f"Result: {final_output}")