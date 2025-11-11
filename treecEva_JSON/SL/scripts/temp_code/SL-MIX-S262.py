import re
from statistics import variance
from itertools import compress

def calculate_adjusted_volatility(transactions):
    # Filter transactions matching the pattern: starts with 'TX', followed by 4 digits, then optional '-REF\d+'
    pattern = r'^TX\d{4}(?:-REF\d+)?$'
    valid_flags = [bool(re.match(pattern, tx)) for tx in transactions]
    
    # Extract numeric values from valid transactions
    amounts = []
    for tx in compress(transactions, valid_flags):
        # Extract all digits and convert to integer (assuming single numeric value per transaction)
        nums = re.findall(r'\d+', tx)
        if nums:
            amounts.append(int(nums[0]))
    
    # Calculate base variance
    if len(amounts) < 2:
        return 0
    base_var = variance(amounts)
    
    # Adjust based on number of valid transactions
    adjustment_factor = len([f for f in valid_flags if f]) * 0.5
    adjusted_volatility_index = base_var * adjustment_factor
    
    return adjusted_volatility_index

# Transaction log data
transaction_log = [
    'TX1234',
    'TX5678-REF99',
    'TXABCD',
    'TX9999-REF01',
    'INVALID123',
    'TX0001',
    'TX2222-REF55'
]

adjusted_volatility_index = calculate_adjusted_volatility(transaction_log)
print(f"Result: {adjusted_volatility_index}")