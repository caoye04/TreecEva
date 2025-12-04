def account_summary(operations):
    # Process transaction operations with some intermediate calculations
    base_amount = 1000
    temp_buffer = [op * 2 for op in operations[:3]]  # List comprehension - not used in final result
    
    # Main processing with slicing and XOR operations
    processed = operations[1:-1]
    running_total = base_amount
    
    # Some intermediate variables that don't affect final result
    operation_count = len(operations)
    max_value = max(operations)  # Red herring calculation
    
    for amount in processed:
        if amount > 0:
            running_total += amount
        else:
            running_total -= abs(amount)
    
    # Additional bitwise operations that don't change the result
    verification = running_total ^ 0xFF  # XOR operation - irrelevant to final balance
    temp_check = verification & 0x0F  # AND operation - distractor
    
    final_balance = running_total
    print(f"Target result: {final_balance}")
    return final_balance

# Transaction data: deposits and withdrawals
transactions = [500, -200, 300, -150, 100, -50, 400]
final_balance = account_summary(transactions)