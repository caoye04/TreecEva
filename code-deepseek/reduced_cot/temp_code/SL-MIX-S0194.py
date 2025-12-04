from collections import Counter

def calculate_processing_fee(base_amount, fee_multiplier):
    irrelevant_calc = base_amount * 3.14159  # Misleading computation
    return base_amount * fee_multiplier

def apply_discount_matrix(amounts, discount_matrix):
    total = sum(amounts)
    discount_applied = discount_matrix.get(len(amounts), 0.05)
    return total * (1 - discount_applied)

def process_final_settlement(transactions, fees, discounts):
    transaction_counter = Counter(transactions)
    fee_total = 0
    
    # Irrelevant loop - counts but doesn't affect final result
    for i in range(5):
        dummy_var = i * 2 + 7
    
    # Process main transactions
    main_amounts = []
    for trans_type, count in transaction_counter.items():
        if trans_type.startswith('TX_'):
            base_fee = fees.get(trans_type, 25)
            processed_fee = calculate_processing_fee(base_fee, 1.08)
            main_amounts.append(processed_fee * count)
    
    # Dead code path - condition never met
    if len(transactions) > 100:
        unused_bonus = 500
    
    subtotal = sum(main_amounts)
    final_amount = apply_discount_matrix(main_amounts, discounts)
    
    # Misleading intermediate calculation
    temp_calc = subtotal * 0.85  # This is misleading
    
    return round(final_amount, 2)

# Main execution
account_fees = {'TX_STANDARD': 30, 'TX_PREMIUM': 50, 'TX_BASIC': 20}
discount_matrix = {1: 0.10, 2: 0.15, 3: 0.20, 4: 0.25}
transaction_log = ['TX_STANDARD', 'TX_PREMIUM', 'TX_BASIC', 'TX_STANDARD', 'TX_PREMIUM']

# Irrelevant variables
unused_credit = 1000
backup_calc = sum(account_fees.values()) * 2.5

final_balance = process_final_settlement(transaction_log, account_fees, discount_matrix)
print(f"Result: {final_balance}")