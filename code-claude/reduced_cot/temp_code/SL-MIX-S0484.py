from collections import Counter

# Fruit inventory tracking system
inventory = {
    'apple': 25,
    'banana': 18,
    'orange': 32,
    'apple': 40,  # This overwrites the previous apple entry
    'kiwi': 15,
    'grape': 22
}

# Calculate total fruit count
total_fruits = sum(inventory.values())

# Track which fruits have more than 20 items
well_stocked = [fruit for fruit, count in inventory.items() if count > 20]

# Count unique fruit types
unique_fruits = len(set(inventory.keys()))

# Additional inventory statistics
average_stock = total_fruits / unique_fruits
most_common = max(inventory.items(), key=lambda x: x[1])[0]

print(f"Result: {unique_fruits}")