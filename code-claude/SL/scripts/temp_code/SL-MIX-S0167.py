import itertools

def process_inventory(items):
    # Dictionary of items with their properties
    inventory = {
        'apple': {'price': 1.20, 'quantity': 10, 'category': 'fruit'},
        'banana': {'price': 0.50, 'quantity': 15, 'category': 'fruit'},
        'carrot': {'price': 0.30, 'quantity': 8, 'category': 'vegetable'},
        'potato': {'price': 0.25, 'quantity': 20, 'category': 'vegetable'},
        'milk': {'price': 2.50, 'quantity': 5, 'category': 'dairy'}
    }
    
    # Extract prices of items in stock
    prices = [inventory[item]['price'] for item in items if item in inventory]
    
    # Calculate average price
    avg_price = sum(prices) / len(prices) if prices else 0
    
    # Filter values below average
    filtered_values = [price for price in prices if price < avg_price]
    
    # Calculate sum of filtered values
    filtered_sum = sum(filtered_values)
    
    # Slice the filtered values for reporting
    report_values = filtered_values[:2]
    
    print(f"Target result: {filtered_sum}")
    return filtered_sum

# Process a subset of inventory items
result = process_inventory(['apple', 'banana', 'carrot', 'potato'])