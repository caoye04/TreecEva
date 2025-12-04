from collections import Counter, defaultdict

def calculate_discount(price, category, inventory_days):
    # Calculate discount based on category and inventory days
    base_discount = 0.05
    if category in ['electronics', 'appliances']:
        base_discount = 0.10 if inventory_days > 90 else 0.07
    elif category in ['clothing', 'accessories']:
        base_discount = 0.15 if inventory_days > 60 else 0.12
    elif category == 'clearance':
        base_discount = 0.25
        
    # Additional discount based on price tiers
    tier_discount = 0
    if price > 1000:
        tier_discount = 0.05
    elif price > 500:
        tier_discount = 0.03
    elif price > 100:
        tier_discount = 0.02
        
    return min(base_discount + tier_discount, 0.30)  # Cap at 30%

def analyze_inventory(products):
    # This function performs various inventory analytics
    category_counts = Counter()
    category_values = defaultdict(float)
    high_value_items = []
    
    for product in products:
        category_counts[product['category']] += 1
        category_values[product['category']] += product['price']
        if product['price'] > 500:
            high_value_items.append(product)
    
    # Calculate average values by category
    avg_values = {}
    for category, count in category_counts.items():
        if count > 0:
            avg_values[category] = category_values[category] / count
    
    return {
        'category_counts': category_counts,
        'high_value_items': len(high_value_items),
        'avg_values': avg_values
    }

def calculate_margin(items, tax_rate):
    total_cost = 0
    total_revenue = 0
    promotion_active = False
    
    # Track items by category for bundle discounts
    category_items = defaultdict(list)
    for item in items:
        category_items[item['category']].append(item)
    
    # Calculate potential bundle discounts
    bundle_categories = ['electronics', 'accessories']
    bundle_discount = 0
    if all(len(category_items[cat]) > 0 for cat in bundle_categories):
        bundle_discount = 0.07
        promotion_active = True
    
    # Process all items
    for item in items:
        # Calculate item cost with supplier discount
        supplier_discount = 0.05 if item['quantity'] > 20 else 0.02
        item_cost = item['cost'] * item['quantity'] * (1 - supplier_discount)
        
        # Apply seasonal adjustment factor (not relevant to final calculation)
        seasonal_factor = 1.1 if item['category'] in ['clothing', 'accessories'] else 1.0
        adjusted_cost = item_cost * seasonal_factor
        
        # Calculate selling price with applicable discounts
        discount = calculate_discount(item['price'], item['category'], item['days_in_inventory'])
        if promotion_active and item['category'] in bundle_categories:
            discount = max(discount, bundle_discount)
        
        # Apply quantity-based revenue calculation
        item_revenue = item['price'] * item['quantity'] * (1 - discount)
        
        # Add to totals
        total_cost += item_cost  # Use actual cost, not adjusted_cost
        total_revenue += item_revenue
    
    # Irrelevant calculations for distraction
    inventory_metrics = analyze_inventory(items)
    logistics_factor = 0.92 if inventory_metrics['high_value_items'] > 2 else 0.96
    avg_category_value = sum(inventory_metrics['avg_values'].values()) / len(inventory_metrics['avg_values'])
    
    # Calculate profit before tax
    profit_before_tax = total_revenue - total_cost
    
    # Apply tax
    taxable_amount = profit_before_tax * 0.85  # Assuming 15% non-taxable expenses
    tax_amount = taxable_amount * tax_rate
    
    # Calculate final profit margin
    profit_after_tax = profit_before_tax - tax_amount
    profit_margin = (profit_after_tax / total_revenue) * 100 if total_revenue > 0 else 0
    
    # Round to 2 decimal places
    return round(profit_margin, 2)

# Sample inventory data
inventory = [
    {'id': 101, 'category': 'electronics', 'price': 799.99, 'cost': 550.00, 'quantity': 15, 'days_in_inventory': 45},
    {'id': 102, 'category': 'accessories', 'price': 59.99, 'cost': 25.00, 'quantity': 30, 'days_in_inventory': 60},
    {'id': 103, 'category': 'clothing', 'price': 129.99, 'cost': 65.00, 'quantity': 25, 'days_in_inventory': 75},
    {'id': 104, 'category': 'clearance', 'price': 299.99, 'cost': 240.00, 'quantity': 5, 'days_in_inventory': 120},
    {'id': 105, 'category': 'electronics', 'price': 1299.99, 'cost': 950.00, 'quantity': 8, 'days_in_inventory': 30},
    {'id': 106, 'category': 'appliances', 'price': 649.99, 'cost': 450.00, 'quantity': 12, 'days_in_inventory': 95}
]

# Filter inventory items for processing
filter_criteria = lambda item: item['days_in_inventory'] > 40 or item['price'] > 500
filtered_items = [item for item in inventory if filter_criteria(item)]

# Tax rates for different regions
tax_rates = {'domestic': 0.21, 'international': 0.15, 'tax_free': 0.0}

# Select applicable tax rate
region_code = 'domestic'
tax_rate = tax_rates.get(region_code, tax_rates['domestic'])

# Perform profit margin calculation
profit_margin = calculate_margin(filtered_items, tax_rate)

# Misleading calculations that don't affect the answer
alternative_margin = 0
if len(filtered_items) > 3:
    weighted_costs = sum(item['cost'] * (item['days_in_inventory'] / 30) for item in filtered_items)
    projected_revenue = sum(item['price'] * 1.2 for item in filtered_items)
    alternative_margin = ((projected_revenue - weighted_costs) / projected_revenue) * 100

# Output the result
print(f"Result: {profit_margin}")