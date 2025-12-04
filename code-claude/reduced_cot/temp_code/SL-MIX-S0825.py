import itertools

# Bookstore inventory tracking
prices = {'novel': 12, 'textbook': 45, 'comic': 5, 'magazine': 8}
counts = {'novel': 10, 'textbook': 5, 'comic': 15, 'magazine': 7}

# Categorize items for display purposes
fiction = ['novel', 'comic']
non_fiction = ['textbook', 'magazine']

# Group items by price range
budget_items = [item for item, price in prices.items() if price < 10]
premium_items = [item for item, price in prices.items() if price >= 10]

# Calculate inventory value
inventory_value = sum(map(lambda item: prices.get(item, 0) * counts[item], counts.keys()))

# Calculate potential combinations for bundle deals
possible_bundles = len(list(itertools.combinations(prices.keys(), 2)))

# Show results
print(f"Budget items: {budget_items}")
print(f"Premium items: {premium_items}")
print(f"Possible bundle combinations: {possible_bundles}")
print(f"Total inventory value: {inventory_value}")