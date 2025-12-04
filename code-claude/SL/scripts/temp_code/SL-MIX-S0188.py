from collections import Counter

def product_of_common_elements(items1, items2):
    # Find common elements and their frequencies
    counter1 = Counter(items1)
    counter2 = Counter(items2)
    
    # Get common elements
    common_elements = counter1.keys() & counter2.keys()
    
    # Calculate product of common elements
    result = 1
    for item in common_elements:
        # Take the minimum frequency from both collections
        min_frequency = min(counter1[item], counter2[item])
        result *= item * min_frequency
    
    return result

# First shopping basket with item prices
basket1 = [2, 3, 5, 7, 2, 11, 7, 3]

# Calculate some statistics about basket1
avg_price = sum(basket1) / len(basket1)
max_price = max(basket1)
min_price = min(basket1)
median_candidate = sorted(basket1)[len(basket1)//2]

# Second shopping basket with item prices
basket2 = [3, 5, 5, 7, 13, 17, 3]

# Calculate potential discount
potential_discount = 0
for i, price in enumerate(basket2):
    if i % 2 == 0 and price > 4:
        potential_discount += price * 0.1

# Determine which basket has more unique items
unique_items1 = set(basket1)
unique_items2 = set(basket2)
larger_variety = "basket1" if len(unique_items1) > len(unique_items2) else "basket2"

# Calculate the product of common elements
common_product = product_of_common_elements(basket1, basket2)

# Process some additional data
for price in zip(basket1, basket2):
    if len(price) == 2:
        # This doesn't affect our target variable
        temp_sum = sum(price)

print(f"Result: {common_product}")