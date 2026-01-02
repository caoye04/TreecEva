from collections import Counter

def process_transactions(transactions, threshold):
    counts = Counter(transactions)
    filtered = [amt for amt in transactions if counts[abs(amt)] >= threshold]
    return [x * 0.9 if x > 0 else x * 1.1 for x in filtered]

def final_tally(data):
    base = sum(data)
    adjustment = base % 7 if base != 0 else 5
    return base - adjustment

# Simulate transaction stream with noise
dummy_data = [150, -80, 200, -30, -80, 200, 200, -50]
config_flag = True
scaling_factor = 1.0

modified_data = process_transactions(dummy_data, threshold=2)
balance = final_tally(modified_data)

Result: {balance}