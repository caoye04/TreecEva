# Calorie counter for a fruit inventory management system

# Calories per 100g of each fruit
calories_per_fruit = {
    'apple': 52,
    'banana': 89,
    'orange': 47,
    'pear': 57,
    'grape': 67,
    'kiwi': 61,
    'mango': 60
}

# Current inventory (in units)
inventory = {
    'apple': 5,
    'banana': 3,
    'orange': 2,
    'pear': 0,
    'grape': 4,
    'kiwi': 1,
    'strawberry': 8
}

# Available fruit types
fruit_types = list(calories_per_fruit.keys())

# Only count fruits that are both in calories database and inventory
common_fruits = [fruit for fruit in fruit_types if fruit in inventory and inventory[fruit] > 0]

# Display information
print(f"Available fruits: {common_fruits}")

# Calculate total calories
total_calories = sum(calories_per_fruit[fruit] * inventory[fruit] for fruit in common_fruits)

# Display nutrition stats
print(f"Average calories per fruit: {total_calories / len(common_fruits):.2f}")
print(f"Total calories: {total_calories}")