# Analyzing customer overlap between two retail stores

def calculate_customer_metrics(store_data):
    # Extract loyalty tiers for bonus calculation (not used in main calculation)
    loyalty_tiers = {}
    for store, customers in store_data.items():
        tier_counts = {'bronze': 0, 'silver': 0, 'gold': 0}
        for customer in customers:
            if customer % 3 == 0:
                tier_counts['gold'] += 1
            elif customer % 2 == 0:
                tier_counts['silver'] += 1
            else:
                tier_counts['bronze'] += 1
        loyalty_tiers[store] = tier_counts
    
    # Customer ID processing
    processed_data = {}
    for store, customers in store_data.items():
        # Apply store-specific filtering rules
        if store == 'A':
            filtered = set([c for c in customers if c > 100])
        elif store == 'B':
            filtered = set([c for c in customers if c % 5 != 0])
        else:
            filtered = set(customers)
        processed_data[store] = filtered
    
    return processed_data, loyalty_tiers

# Customer IDs by store
raw_customer_data = {
    'A': [103, 105, 108, 115, 120, 125, 130, 135, 140, 145, 150, 99],
    'B': [101, 108, 115, 122, 129, 136, 143, 150, 157, 164, 171],
    'C': [105, 110, 115, 120, 125, 130, 135]  # Store C data not used in final calculation
}

# Process the customer data
processed_stores, loyalty_breakdown = calculate_customer_metrics(raw_customer_data)

# Extract processed customer sets for stores A and B
store_a_customers = processed_stores['A']
store_b_customers = processed_stores['B']

# Calculate metrics for business analysis
total_unique_customers = len(store_a_customers.union(store_b_customers))
overlapping_customers = len(store_a_customers.intersection(store_b_customers))
exclusive_a_customers = len(store_a_customers - store_b_customers)

# Calculate percentage for reporting (not used in final answer)
if total_unique_customers > 0:
    overlap_percentage = (overlapping_customers / total_unique_customers) * 100
else:
    overlap_percentage = 0

print(f"Result: {overlapping_customers}")