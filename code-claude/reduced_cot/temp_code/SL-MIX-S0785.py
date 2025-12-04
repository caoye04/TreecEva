import itertools

def calculate_final_score(transactions):
    # Calculate a weighted score based on transaction patterns
    if not transactions:
        return 0
    
    # Extract values for calculation
    values = [t['amount'] for t in transactions]
    categories = [t['category'] for t in transactions]
    
    # Some statistical calculations that don't affect final result
    avg_value = sum(values) / len(values)
    max_value = max(values)
    min_value = min(values)
    value_range = max_value - min_value
    
    # Count categories (this part matters)
    category_counts = {}
    for category in categories:
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Find pairs of consecutive identical categories (doesn't affect result)
    pairs = list(itertools.pairwise(categories))
    identical_pairs = sum(1 for a, b in pairs if a == b)
    
    # Calculate diversity score based on unique categories
    unique_categories = set(categories)
    diversity_factor = len(unique_categories) * 2
    
    # Calculate volume score based on transaction amounts
    volume_factor = sum(min(v, 100) for v in values) // 10
    
    # Calculate frequency bonus based on most common category
    most_common_category = max(category_counts.items(), key=lambda x: x[1])
    frequency_bonus = most_common_category[1] * 5
    
    # These adjustments don't affect the final result
    seasonal_adjustment = 15 if avg_value > 50 else 0
    loyalty_bonus = identical_pairs * 3
    
    # Final calculation
    base_score = diversity_factor + volume_factor + frequency_bonus
    return base_score

# Sample transaction data
transactions = [
    {'id': 101, 'amount': 75, 'category': 'food'},
    {'id': 102, 'amount': 120, 'category': 'electronics'},
    {'id': 103, 'amount': 45, 'category': 'food'},
    {'id': 104, 'amount': 25, 'category': 'books'},
    {'id': 105, 'amount': 60, 'category': 'clothing'},
    {'id': 106, 'amount': 35, 'category': 'food'},
    {'id': 107, 'amount': 90, 'category': 'electronics'},
    {'id': 108, 'amount': 15, 'category': 'books'}
]

# Filter transactions based on amount threshold
threshold = 40
filtered_transactions = [t for t in transactions if t['amount'] > threshold]

# Calculate potential discount (not used in final calculation)
potential_discount = len(filtered_transactions) * 2

# Calculate the final score
final_score = calculate_final_score(filtered_transactions)

# Display the result
print(f"Result: {final_score}")