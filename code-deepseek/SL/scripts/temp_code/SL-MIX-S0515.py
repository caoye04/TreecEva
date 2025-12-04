def process_transactions(transactions):
    base_total = sum(transactions)
    temporary_buffer = base_total * 1.1  # Not used in final calculation
    
    if base_total > 500:
        adjustment_factor = 0.85
        bonus_amount = 25
    else:
        adjustment_factor = 0.92
        bonus_amount = 15
    
    adjusted_total = base_total * adjustment_factor
    processing_fee = len(transactions) * 2.5
    dummy_calc = processing_fee * 1.05  # Redundant calculation
    
    final_balance = adjusted_total - processing_fee + bonus_amount
    print(f"Target result: {final_balance}")

# Main execution
transaction_list = [120, 85, 210, 45, 180]
intermediate_sum = sum(transaction_list) + 10  # Distractor calculation
process_transactions(transaction_list)