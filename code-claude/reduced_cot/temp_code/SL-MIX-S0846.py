def process_financial_data(raw_transactions):
    # Initialize tracking variables
    suspicious_threshold = 950
    flagged_count = 0
    potential_fraud = set()
    processed_data = {}
    
    # Process each transaction and apply business rules
    for tx_id, details in enumerate(raw_transactions):
        # Extract transaction details
        amount = details.get('amount', 0)
        category = details.get('category', 'unknown')
        timestamp = details.get('timestamp', 0)
        user_id = details.get('user_id', -1)
        
        # Flag suspicious transactions (not used in final calculation)
        if amount > suspicious_threshold or category == 'foreign':
            flagged_count += 1
            potential_fraud.add(tx_id)
            risk_score = min(100, amount / 10)
        else:
            risk_score = max(1, amount / 100)
        
        # Store processed information
        processed_data[tx_id] = {
            'risk': risk_score,
            'processed_time': timestamp + 120,
            'original_amount': amount
        }
    
    # Apply security filters
    security_coefficient = 1.5 if flagged_count > 3 else 1.0
    
    # Create a list of valid transaction IDs based on complex criteria
    valid_tx_ids = []
    for tx_id in range(len(raw_transactions)):
        # Skip transactions that were flagged
        if tx_id in potential_fraud:
            continue
            
        # Get original transaction data
        tx_data = raw_transactions[tx_id]
        tx_amount = tx_data.get('amount', 0)
        tx_category = tx_data.get('category', 'unknown')
        
        # Apply business rules for valid transactions
        is_valid = tx_amount > 0 and tx_category != 'rejected'
        
        if is_valid:
            valid_tx_ids.append(tx_id)
    
    # Extract the valid transactions from processed data
    # This creates tuples of (tx_id, amount) for valid transactions
    filtered_transactions = [(tx_id, processed_data[tx_id]['original_amount']) 
                            for tx_id in valid_tx_ids 
                            if tx_id in processed_data]
    
    # Count valid transactions
    valid_transactions = sum(1 for tx_id, amount in filtered_transactions)
    
    # Calculate other metrics (not used in final result)
    avg_transaction = sum(amount for _, amount in filtered_transactions) / max(1, valid_transactions)
    weighted_risk = sum(processed_data[tx_id]['risk'] * security_coefficient 
                        for tx_id in valid_tx_ids) if valid_tx_ids else 0
    
    # Generate summary report (not relevant to question)
    summary = {
        'total_processed': len(raw_transactions),
        'flagged': flagged_count,
        'valid': valid_transactions,
        'avg_amount': avg_transaction,
        'risk_index': weighted_risk / max(1, len(valid_tx_ids))
    }
    
    print(f"Result: {valid_transactions}")
    return valid_transactions

# Sample transaction data
raw_data = [
    {'amount': 750, 'category': 'retail', 'timestamp': 1625176800, 'user_id': 42},
    {'amount': 1200, 'category': 'foreign', 'timestamp': 1625176900, 'user_id': 17},
    {'amount': 0, 'category': 'rejected', 'timestamp': 1625177000, 'user_id': 23},
    {'amount': 340, 'category': 'services', 'timestamp': 1625177100, 'user_id': 42},
    {'amount': 560, 'category': 'retail', 'timestamp': 1625177200, 'user_id': 17},
    {'amount': 990, 'category': 'entertainment', 'timestamp': 1625177300, 'user_id': 42}
]

process_financial_data(raw_data)