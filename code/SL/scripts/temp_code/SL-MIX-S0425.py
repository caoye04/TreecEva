def process_transaction_data(log_data):
    # Distractor: This calculates word count but isn't used in final result
    word_count = len(log_data.split())
    
    # Distractor: Uppercase conversion that doesn't affect numeric processing
    processed_log = log_data.upper()
    
    # Main processing logic
    transaction_set = set()
    balance = 1000
    
    for line in processed_log.split(';'):
        if line.strip():
            parts = line.split(':')
            if len(parts) == 2:
                operation, amount_str = parts
                try:
                    amount = int(amount_str.strip())
                    transaction_set.add(operation.strip())
                    
                    # Actual balance calculation
                    if operation.strip() == 'DEPOSIT':
                        balance += amount
                        # Distractor: Redundant operation
                        temp_adjust = balance | 0b1010
                    elif operation.strip() == 'WITHDRAW':
                        balance -= amount
                        # Distractor: Unused bitwise operation
                        check_bit = balance & 0xFF
                    elif operation.strip() == 'FEE':
                        balance = max(balance - amount, 0)
                        # Distractor: String operation on number
                        fee_str = str(balance)
                except ValueError:
                    # Distractor: Dead code path
                    error_count = len(transaction_set)
                    
    # Distractor: Unused character counting
    char_total = sum(len(op) for op in transaction_set)
    
    # Final adjustment based on unique operations
    final_adjust = len(transaction_set) * 5
    
    # Final balance calculation
    final_balance = balance + final_adjust
    
    # Distractor: Unused calculation
    avg_transaction = balance / len(transaction_set) if transaction_set else 0
    
    print(f"Result: {final_balance}")
    return final_balance

# Test data
transaction_log = "DEPOSIT:500;WITHDRAW:200;FEE:50;DEPOSIT:300;WITHDRAW:150"

# Execute main processing
final_balance = process_transaction_data(transaction_log)