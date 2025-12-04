import itertools

def process_supplier_data(data):
    # This function processes supplier data but isn't used in the main flow
    processed = {}
    for supplier, items in data.items():
        processed[supplier] = sum(item['value'] for item in items)
    return processed

def calculate_depreciation(age, original_value):
    # Calculate depreciation based on age
    depreciation_factor = min(0.8, age * 0.1)
    return original_value * (1 - depreciation_factor)

def apply_market_adjustment(items, market_trend):
    # Apply market adjustment to items - not used in final calculation
    for item in items:
        item['adjusted_value'] = item['value'] * market_trend
    return items

def calculate_inventory_value(inventory):
    # Core function that calculates the actual inventory value
    total = 0
    priority_items = ['electronics', 'tools']
    
    # First pass - calculate basic value
    for item_id, details in inventory.items():
        if details['category'] in priority_items:
            # Apply priority multiplier for electronics and tools
            value = details['quantity'] * details['unit_price'] * 1.15
        else:
            value = details['quantity'] * details['unit_price']
        
        # Apply age-based depreciation
        value = calculate_depreciation(details['age'], value)
        total += value
    
    # Apply tax deduction if total exceeds threshold
    if total > 10000:
        total = total * 0.92  # 8% tax deduction
    
    return round(total, 2)

# Initialize inventory data
inventory = {
    'A101': {'category': 'electronics', 'quantity': 15, 'unit_price': 399.99, 'age': 1},
    'B202': {'category': 'furniture', 'quantity': 5, 'unit_price': 799.50, 'age': 3},
    'C303': {'category': 'tools', 'quantity': 25, 'unit_price': 129.75, 'age': 2},
    'D404': {'category': 'office', 'quantity': 100, 'unit_price': 12.50, 'age': 4},
    'E505': {'category': 'electronics', 'quantity': 8, 'unit_price': 599.99, 'age': 0}
}

# Market trend data - not actually used in final calculation
market_trends = {
    'electronics': 0.95,  # declining market
    'furniture': 1.02,    # slightly increasing
    'tools': 1.00,        # stable
    'office': 0.98        # slightly declining
}

# Supplier reliability scores - distractor data
supplier_scores = {
    'SupplierA': 0.95,
    'SupplierB': 0.87,
    'SupplierC': 0.92
}

# Calculate potential combinations for inventory optimization - not used
optimization_options = list(itertools.combinations(['price', 'age', 'quantity', 'category'], 2))

# Filter inventory based on various conditions
def filter_inventory(inv, min_quantity=0, max_age=10, categories=None):
    filtered = {}
    for item_id, details in inv.items():
        if details['quantity'] > min_quantity and details['age'] <= max_age:
            if categories is None or details['category'] in categories:
                filtered[item_id] = details
    return filtered

# Calculate potential revenue - distractor calculation
potential_revenue = sum(details['quantity'] * details['unit_price'] * 1.25 
                       for details in inventory.values())

# Apply various filters - most not used in final calculation
high_quantity_items = filter_inventory(inventory, min_quantity=20)
low_age_items = filter_inventory(inventory, max_age=1)
electronics_items = filter_inventory(inventory, categories=['electronics'])

# This is the filter actually used for the final calculation
filtered_inventory = filter_inventory(inventory, min_quantity=0, max_age=5)

# Calculating weighted scores - distractor calculation
weighted_scores = {}
for item_id, details in inventory.items():
    score = (details['unit_price'] * 0.4 + 
             (5 - details['age']) * 100 * 0.3 + 
             details['quantity'] * 0.3)
    weighted_scores[item_id] = score

# Calculate total inventory value using the filtered inventory
final_stock = calculate_inventory_value(filtered_inventory)

# Distractor calculations after the target variable is set
adjusted_inventory = apply_market_adjustment(
    [{'id': k, 'value': v['unit_price'] * v['quantity']} for k, v in inventory.items()],
    1.05
)

# Final adjustment that doesn't affect our target variable
if sum(supplier_scores.values()) > 2.5:
    market_adjustment = 1.02
else:
    market_adjustment = 0.98

print(f"Result: {final_stock}")