def calculate_priority(customer):
    # Calculate customer priority score based on multiple factors
    base_score = 100
    loyalty_years = customer.get('years', 0)
    purchase_history = customer.get('purchases', [])
    support_tickets = customer.get('tickets', 0)
    
    # Loyalty bonus calculation
    loyalty_bonus = min(loyalty_years * 15, 75)
    
    # Purchase analysis
    total_spent = sum(purchase_history)
    premium_purchases = len([p for p in purchase_history if p > 200])
    purchase_factor = total_spent / 1000 if total_spent > 0 else 0
    
    # Support ticket penalty
    ticket_penalty = support_tickets * 5
    
    # Seasonal adjustment (not relevant to final score)
    season = 'summer'
    seasonal_boost = 20 if season == 'winter' else 10
    
    # Special promotional flag (distraction)
    promo_eligible = loyalty_years > 2 and total_spent > 5000
    
    # Calculate raw score
    raw_score = base_score + loyalty_bonus + (purchase_factor * 50)
    
    # Apply penalties
    adjusted_score = raw_score - ticket_penalty
    
    # Apply premium customer bonus
    premium_bonus = premium_purchases * 15
    
    # Calculate final score - ignoring seasonal adjustment
    final_score = adjusted_score + premium_bonus
    
    # Apply score thresholds
    if final_score < 0:
        return 0
    elif final_score > 500:
        return 500
    else:
        return round(final_score)

# Customer data
customer_data = {
    'name': 'Alex Johnson',
    'years': 4,
    'purchases': [120, 250, 180, 350, 90],
    'tickets': 2,
    'email': 'alex.j@example.com',  # Irrelevant data
    'last_contact': '2023-05-15'    # Irrelevant data
}

# Calculate customer segments (distraction)
default_segments = ['general', 'promotional']
segments = default_segments + (['premium'] if sum(customer_data.get('purchases', [])) > 1500 else [])

# Process customer data
for i, segment in enumerate(segments):
    print(f"Segment {i+1}: {segment}")

# Calculate the priority score
priority_score = calculate_priority(customer_data)

# Format output with customer name (distraction)
customer_name = customer_data.get('name', 'Unknown')
output_message = f"Customer: {customer_name} | " + ("VIP" if priority_score > 300 else "Standard")

print(f"Result: {priority_score}")