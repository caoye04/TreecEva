from collections import Counter

# Process transaction data for a payment system
transaction_types = ['success', 'success', 'failed', 'success', 'cancelled', 'failed']

# Count transaction types
transaction_counts = Counter(transaction_types)

# Extract counts for analysis
successful_count = transaction_counts['success']
failed = transaction_counts['failed']
cancelled = transaction_counts['cancelled']

# Calculate some metrics
processed = successful_count + failed + cancelled
quality_metric = successful_count / processed if processed > 0 else 0

# Apply bitwise operation to combine failed and cancelled transactions
# This represents transactions that need investigation
transaction_result = successful_count - (failed & cancelled)

# Display the final transaction result
print(f"Result: {transaction_result}")