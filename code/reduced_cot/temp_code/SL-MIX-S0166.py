def analyze_financial_operations():
    transaction_history = {45, 78, 23, 91, 67, 34}
    audit_log = {23, 67, 12, 89, 45, 56}
    
    # Process primary transactions
    primary_set = transaction_history - audit_log
    intermediate_calc = sum(transaction_history) * 2
    
    # Process secondary operations  
    secondary_set = audit_log - transaction_history
    temp_adjustment = len(transaction_history) * len(audit_log)
    
    # Merge and finalize
    merged_operations = primary_set | secondary_set
    final_balance = len(merged_operations)
    
    # Distractor operations
    verification_check = sum(primary_set) + sum(secondary_set)
    unused_calculation = intermediate_calc % temp_adjustment
    
    print(f"Target result: {final_balance}")

analyze_financial_operations()