def process_transaction_data(transactions, categories):
    # Initialize tracking variables
    category_totals = {}
    temp_buffer = []
    validation_flags = set()
    processed_count = 0
    
    # Distractor: Unused intermediate calculation
    preliminary_sum = sum(len(str(t)) for t in transactions) * 2
    
    for transaction in transactions:
        amount, category, status = transaction
        
        # Distractor: Unused validation logic
        if status == 'pending':
            validation_flags.add(category)
        
        # Relevant logic: Process valid categories
        if category in categories and status == 'completed':
            if category not in category_totals:
                category_totals[category] = 0
            
            # Distractor: Misleading intermediate operation
            adjusted_amount = amount * 1.1
            
            # Actual operation
            category_totals[category] += amount
            processed_count += 1
            
            # Distractor: Unused buffer
            temp_buffer.append((category, adjusted_amount))
    
    # Distractor: Unrelated computation
    metadata_sum = sum(len(c) for c in categories) * 100
    
    # Key calculation
    if category_totals:
        primary_total = max(category_totals.values())
        secondary_total = min(category_totals.values())
        
        # Distractor: Misleading operation that doesn't affect result
        intermediate_calc = (primary_total + secondary_total) // 2
        
        # Final result calculation
        final_result = primary_total - secondary_total
    else:
        final_result = 0
    
    # Distractor: Dead code path
    if processed_count > 10:
        final_result = final_result * 2
    
    return final_result

# Main execution
transaction_logs = [
    (150, 'electronics', 'completed'),
    (80, 'books', 'completed'),
    (200, 'electronics', 'pending'),
    (45, 'books', 'completed'),
    (120, 'clothing', 'completed'),
    (90, 'electronics', 'completed')
]

valid_categories = {'electronics', 'books', 'clothing'}

final_result = process_transaction_data(transaction_logs, valid_categories)
print(f"Result: {final_result}")