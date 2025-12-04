from collections import Counter

def analyze_transactions(transactions):
    # Calculate the transaction sums
    transaction_sums = []
    for transaction in transactions:
        # Sum of purchase amounts in each transaction
        transaction_sum = sum(transaction)
        transaction_sums.append(transaction_sum)
    
    # Find most common transaction sum
    frequency_counter = Counter(transaction_sums)
    most_frequent_sum = max(frequency_counter.items(), key=lambda x: x[1])[0]
    
    # Calculate average transaction amount
    avg_amount = sum(transaction_sums) / len(transaction_sums)
    rounded_avg = round(avg_amount, 2)
    
    return most_frequent_sum, rounded_avg

# Sample transaction data (each inner list represents amounts in one transaction)
daily_transactions = [
    [10, 15, 5],    # Sum: 30
    [25, 5],        # Sum: 30
    [20, 10, 15],   # Sum: 45
    [30],           # Sum: 30
    [15, 15],       # Sum: 30
    [45],           # Sum: 45
    [20, 20, 5]     # Sum: 45
]

most_common, average = analyze_transactions(daily_transactions)
print(f"Most frequent transaction sum: {most_common}")
print(f"Average transaction amount: {average}")

# Result: {most_common}