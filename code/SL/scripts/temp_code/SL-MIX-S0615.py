def process_payments(transaction_data):
    # Process payment transactions with validation
    processed = {}
    temp_sum = 0
    
    for key, amount in transaction_data.items():
        # Validate transaction amount
        if amount > 0:
            processed[key] = amount % 100  # Extract last two digits
            temp_sum += amount * 2  # Distractor calculation
    
    # Apply processing fee (distractor)
    fee_calc = lambda x: x * 0.05
    fee_amount = fee_calc(len(processed))
    
    return processed

def compute_final(data_dict):
    # Compute final value from processed data
    char_counts = {}
    total = 0
    
    for key, value in data_dict.items():
        # Count characters in key (distractor)
        char_counts[key] = len(str(key))
        
        # Actual computation: sum values with modular arithmetic
        total = (total + value) % 50
    
    # Additional distractor operations
    unused_calc = sum(char_counts.values()) * 3
    
    return total

# Main execution
transactions = {
    'txn_001': 125,
    'txn_002': 87,
    'txn_003': 342,
    'txn_004': 56
}

# Process payments and compute result
processed_data = process_payments(transactions)
intermediate_check = len(processed_data)  # Unused variable
final_value = compute_final(processed_data)

print(f"Target result: {final_value}")