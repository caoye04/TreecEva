def calculate_customer_priority(customer_data):
    # Extract customer information
    customer_names = [c.split(':')[0] for c in customer_data]
    loyalty_points = [int(c.split(':')[1]) for c in customer_data]
    purchase_history = [float(c.split(':')[2]) for c in customer_data]
    
    # Calculate support metrics (not directly used for priority)
    support_tickets = [3, 1, 4, 1, 5, 9, 2]
    avg_response_time = sum(support_tickets) / len(support_tickets)
    
    # Generate priority scores
    raw_priorities = []
    normalized_priorities = []
    
    for i, (name, points, history) in enumerate(zip(customer_names, loyalty_points, purchase_history)):
        # Calculate raw priority score
        raw_score = points * 0.4 + history * 0.6
        raw_priorities.append(raw_score)
        
        # Apply name-based adjustment (not affecting final priority)
        name_factor = sum(1 for c in name.lower() if c in 'aeiou')
        adjusted_score = raw_score + name_factor
        
        # Store normalized priority
        normalized = round(raw_score * 10)
        normalized_priorities.append(normalized)
    
    # Process priorities
    sorted_priorities = sorted(normalized_priorities, reverse=True)
    
    # Find position of customer with highest loyalty
    max_loyalty_index = loyalty_points.index(max(loyalty_points))
    max_loyalty_priority = normalized_priorities[max_loyalty_index]
    
    # Calculate target position
    target_position = sorted_priorities.index(max_loyalty_priority)
    
    # Record some analytics (not used for final calculation)
    priority_distribution = {}
    for p in normalized_priorities:
        if p in priority_distribution:
            priority_distribution[p] += 1
        else:
            priority_distribution[p] = 1
    
    # Get the priority value at the target position
    priority_value = sorted_priorities[target_position]
    
    print(f"Result: {priority_value}")
    return priority_value

# Sample customer data (format: "name:loyalty_points:purchase_history")
customers = [
    "Alice:120:305.75",
    "Bob:85:210.25",
    "Charlie:150:420.50",
    "Diana:95:180.30",
    "Edward:65:150.40"
]

calculate_customer_priority(customers)