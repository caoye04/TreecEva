def process_sales_data(sales_records):
    # Initialize variables
    base_threshold = 100
    premium_threshold = 250
    discount_rate = 0.15
    tax_rate = 0.08
    factor = 0.75
    
    # Process each record
    processed_totals = []
    for record in sales_records:
        # Extract data from record
        item_count = record['quantity']
        unit_price = record['price']
        
        # Calculate raw total
        raw_total = item_count * unit_price
        
        # Apply discount if eligible
        if raw_total > premium_threshold:
            discounted = raw_total * (1 - discount_rate)
        elif raw_total > base_threshold:
            discounted = raw_total * (1 - discount_rate/2)
        else:
            discounted = raw_total
        
        # Calculate tax
        with_tax = discounted * (1 + tax_rate)
        
        # Round to 2 decimal places
        final_total = round(with_tax, 2)
        processed_totals.append(final_total)
    
    # Additional metrics (not directly used in final calculation)
    avg_total = sum(processed_totals) / len(processed_totals) if processed_totals else 0
    max_total = max(processed_totals) if processed_totals else 0
    min_total = min(processed_totals) if processed_totals else 0
    
    # Filter totals based on average
    valid_totals = [total for total in processed_totals if total > min_total + 50]
    
    # Calculate weighted sum of valid totals
    filtered_sum = sum([total * factor for total in valid_totals])
    
    # Additional calculations that don't affect the result
    potential_revenue = sum(processed_totals) * (1 + discount_rate)
    projected_growth = potential_revenue * 1.25
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Sample data
sales_data = [
    {'quantity': 5, 'price': 20},    # 100 -> 100 -> 108 -> 108.0
    {'quantity': 3, 'price': 100},   # 300 -> 255 -> 275.4 -> 275.4
    {'quantity': 2, 'price': 75},    # 150 -> 142.5 -> 153.9 -> 153.9
    {'quantity': 1, 'price': 90}     # 90 -> 90 -> 97.2 -> 97.2
]

result = process_sales_data(sales_data)
