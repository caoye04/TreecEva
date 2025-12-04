from collections import Counter

# Shopping inventory management system
# Track items in shopping cart and wishlist

shopping_cart = ['apple', 'banana', 'orange', 'apple', 'mango', 'kiwi']
wishlist = ['banana', 'pineapple', 'kiwi', 'strawberry', 'mango']

# Count frequency of items in cart
item_counts = Counter(shopping_cart)
most_common_item = item_counts.most_common(1)[0][0]

# Find items that appear in both lists
unique_items = len(set(shopping_cart).intersection(set(wishlist)))

# Calculate total unique items across both lists
total_unique = len(set(shopping_cart).union(set(wishlist)))

print(f"Items in both lists: {unique_items}")
print(f"Total unique items: {total_unique}")
print(f"Most common item: {most_common_item}")