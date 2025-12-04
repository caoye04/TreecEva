from collections import Counter, defaultdict

# Restaurant inventory tracking system
food_inventory = ['tomato', 'lettuce', 'onion', 'tomato', 'cheese', 'bread', 'beef', 'chicken', 'onion']
inventory_counter = Counter(food_inventory)

# Customer order processing
order_items = ['burger', 'salad', 'fries', 'drink']
recipe_ingredients = {
    'burger': ['beef', 'lettuce', 'tomato', 'cheese', 'bread', 'onion'],
    'salad': ['lettuce', 'tomato', 'onion'],
    'fries': ['potato'],
    'drink': ['soda']
}

# Track which ingredients we need for the order
needed_ingredients = []
for item in order_items:
    ingredients = recipe_ingredients.get(item, [])
    needed_ingredients.extend(ingredients)

# Calculate quantities and store in defaultdict
ingredient_quantities = defaultdict(int)
for ingredient in needed_ingredients:
    ingredient_quantities[ingredient] += 1

# Check if we have enough inventory for the order
missing_items = []
for ingredient, quantity in ingredient_quantities.items():
    if inventory_counter[ingredient] < quantity:
        missing_items.append(ingredient)

# Calculate inventory statistics
total_inventory = sum(inventory_counter.values())
avg_per_item = total_inventory / len(inventory_counter) if inventory_counter else 0

# Calculate order statistics
total_needed = len(needed_ingredients)
unique_needed = len(set(needed_ingredients))

# Find ingredients that appear in both inventory and order
order_set = set(needed_ingredients)
inventory_set = set(food_inventory)

# Calculate the overlap between order ingredients and inventory items
unique_overlap = len(order_set.intersection(inventory_set))

# Calculate non-essential metrics
processing_time = total_needed * 0.5  # Estimated time to prepare ingredients
available_percentage = (unique_overlap / unique_needed) * 100 if unique_needed else 0
missing_percentage = (len(missing_items) / unique_needed) * 100 if unique_needed else 0

# Final result
print(f"Result: {unique_overlap}")