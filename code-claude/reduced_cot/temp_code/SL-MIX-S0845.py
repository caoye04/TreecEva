import itertools

# Function to process customer data
def analyze_transaction_data(transaction_code):
    # Extract relevant portions from transaction code
    timestamp = transaction_code[:4]  # First 4 characters represent time
    product_info = transaction_code[4:10]  # Characters 5-10 contain product info
    customer_id = transaction_code[10:]  # Remaining characters are customer ID
    
    # Process the transaction timestamp
    hours = int(timestamp[:2])
    minutes = int(timestamp[2:])
    
    # Determine transaction priority based on time
    priority = 1 if hours < 12 else 2
    
    # Check for special product codes
    special_markers = ['X', 'Z', 'Q']
    contains_special = any(marker in product_info for marker in special_markers)
    
    # Process the product information
    sliced_text = product_info[1:5]  # Take characters 2-5 from product info
    unique_count = len(set(sliced_text))  # Count unique characters
    
    # Calculate transaction value
    transaction_value = unique_count * priority
    
    return transaction_value

# Test with sample transaction
transaction = "0945ABCDEF123456"
result = analyze_transaction_data(transaction)
print(f"Result: {result}")