from collections import defaultdict, Counter
from itertools import cycle

# Simulate transaction data with metadata
tx_data = [
    {'amount': 120, 'type': 'debit', 'category': 'food', 'flagged': False},
    {'amount': -50, 'type': 'credit', 'category': 'refund', 'flagged': True},
    {'amount': 200, 'type': 'debit', 'category': 'rent', 'flagged': False},
    {'amount': 30, 'type': 'debit', 'category': 'food', 'flagged': False},
    {'amount': -15, 'type': 'credit', 'category': 'rebate', 'flagged': False},
    {'amount': 80, 'type': 'debit', 'category': 'utilities', 'flagged': False}
]

# Irrelevant helper: counts characters in category names (distractor)
def count_chars_in_categories(transactions):
    counter = Counter()
    for tx in transactions:
        counter[tx['category']] += len(tx['category'])
    return counter

# Misleading balance tracker that isn't used in final result
def compute_running_total(transactions):
    total = 0
    history = []
    for tx in transactions:
        total += tx['amount']
        history.append(total)
    return history  # Never used

# Filter out flagged transactions and group by type
def filter_and_group(transactions):
    filtered = [tx for tx in transactions if not tx['flagged']]
    grouped = defaultdict(list)
    for tx in filtered:
        grouped[tx['type']].append(tx['amount'])
    return filtered, grouped

# Auxiliary function to compute adjustment factor based on debit distribution
def calculate_adjustment_factor(grouped_tx):
    debits = grouped_tx.get('debit', [])
    if len(debits) == 0:
        return 1.0
    avg_debit = sum(debits) / len(debits)
    variance = sum((x - avg_debit) ** 2 for x in debits) / len(debits)
    return (avg_debit / (1 + variance)) * 0.01  # Minor correction factor

# Core processing function
def process_transactions(transactions, adj_factor):
    base_sum = sum(tx['amount'] for tx in transactions)
    
    # Apply adjustment only to large debits (over 100)
    large_debit_bonus = 0
    for tx in transactions:
        if tx['type'] == 'debit' and tx['amount'] > 100:
            large_debit_bonus += tx['amount'] * adj_factor
    
    # Double-count food expenses for some reason (business logic)
    food_expense_multiplier = 2
    food_total = sum(tx['amount'] for tx in transactions if tx['category'] == 'food')
    adjusted_food = food_total * (food_expense_multiplier - 1)
    
    # Final balance calculation
    final_balance = base_sum + large_debit_bonus + adjusted_food
    return int(final_balance)  # Deterministic integer result

# === Execution Flow ===
char_counts = count_chars_in_categories(tx_data)  # Distractor computation
running_history = compute_running_total(tx_data)  # Dead-end tracking

filtered_tx, grouped_tx = filter_and_group(tx_data)
adjustment_factor = calculate_adjustment_factor(grouped_tx)

# Key statement
final_balance = process_transactions(filtered_tx, adjustment_factor)

print(f"Result: {final_balance}")