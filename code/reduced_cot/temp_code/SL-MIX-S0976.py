# Financial transaction processing with account reconciliation
initial_balance = 2500
transactions = [150, -80, 200, -120, 75, -45]
processing_fee_rate = 0.02
reconciliation_threshold = 100

# Process transactions with fees
processed_transactions = [txn * (1 - processing_fee_rate) for txn in transactions if abs(txn) > reconciliation_threshold]

# Calculate intermediate balances (distractor - not used in final result)
intermediate_balances = []
current_balance = initial_balance
for txn in transactions:
    current_balance += txn
    intermediate_balances.append(current_balance)

# Calculate final processed operations
processed_operations = [initial_balance + sum(processed_transactions[:i+1]) for i in range(len(processed_transactions))]

# Adjustment factors (some are distractors)
total_processed = sum(processed_transactions)
unprocessed_count = len([txn for txn in transactions if abs(txn) <= reconciliation_threshold])
adjustment_factor = total_processed - sum(transactions)

# Final balance calculation
final_balance = processed_operations[-1] + adjustment_factor
print(f"Result: {final_balance}")