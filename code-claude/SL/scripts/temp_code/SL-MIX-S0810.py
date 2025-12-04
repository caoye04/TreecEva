def calculate_engagement(history):
    # Calculate customer engagement metrics
    click_rate = sum(h.get('clicks', 0) for h in history) / max(1, len(history))
    conversion = sum(1 for h in history if h.get('purchased', False))
    abandoned = sum(1 for h in history if h.get('cart_abandoned', False))
    
    # Complex but irrelevant engagement formula
    engagement = (click_rate * 100) + (conversion * 50) - (abandoned * 15)
    return engagement

def apply_seasonal_boost(base_value, month):
    # Irrelevant seasonal adjustments
    seasonal_factors = {
        1: 1.1,  # January
        2: 0.9,  # February
        3: 1.05, # March
        4: 1.0,  # April
        5: 1.15, # May
        6: 1.2,  # June
        7: 1.25, # July
        8: 1.3,  # August
        9: 1.1,  # September
        10: 1.05, # October
        11: 1.3,  # November
        12: 1.4   # December
    }
    return base_value * seasonal_factors.get(month, 1.0)

def calculate_priority(customer_data, is_premium):
    # Extract relevant customer information
    purchase_history = customer_data.get('purchase_history', [])
    browsing_history = customer_data.get('browsing_history', [])
    support_tickets = customer_data.get('support_tickets', [])
    current_month = customer_data.get('current_month', 6)
    
    # Calculate spending metrics (relevant)
    total_spent = sum(purchase.get('amount', 0) for purchase in purchase_history)
    avg_purchase = total_spent / max(1, len(purchase_history))
    
    # Calculate irrelevant metrics
    engagement_score = calculate_engagement(browsing_history)
    support_level = len(support_tickets) * 5
    seasonal_engagement = apply_seasonal_boost(engagement_score, current_month)
    
    # Define scoring weights using lambda functions
    spending_weight = lambda x: 0.6 if x > 1000 else 0.4
    premium_multiplier = lambda status: 1.5 if status else 1.0
    loyalty_factor = lambda years: min(years * 0.1, 0.5)
    
    # Extract key values for calculation
    recent_purchases = [p for p in purchase_history if p.get('days_ago', 100) < 30]
    loyalty_years = customer_data.get('years_active', 0)
    
    # Complex but mostly irrelevant condition
    if engagement_score > 500 and seasonal_engagement > 600:
        potential_score = 85 + (support_level / 10)
    elif len(recent_purchases) > 5 and total_spent > 2000:
        potential_score = 75 - (support_level / 20)
    else:
        potential_score = 60 + (seasonal_engagement / 100)
    
    # The actual relevant calculation is here
    base_score = 50
    if len(recent_purchases) >= 3:
        base_score += 15
    
    if total_spent > 500:
        base_score += 10
    
    # Apply weights and calculate final score
    weighted_score = base_score * spending_weight(total_spent)
    loyalty_bonus = loyalty_factor(loyalty_years) * 100
    
    # This is the critical calculation
    priority_score = int(weighted_score + loyalty_bonus * premium_multiplier(is_premium))
    
    # More irrelevant calculations
    adjusted_score = priority_score + (engagement_score / 50) - (support_level / 2)
    seasonal_score = apply_seasonal_boost(adjusted_score, current_month)
    
    return priority_score

# Sample customer data with various metrics
customer_data = {
    'purchase_history': [
        {'amount': 120, 'days_ago': 5},
        {'amount': 85, 'days_ago': 12},
        {'amount': 210, 'days_ago': 25},
        {'amount': 150, 'days_ago': 45}
    ],
    'browsing_history': [
        {'clicks': 15, 'purchased': True, 'cart_abandoned': False},
        {'clicks': 8, 'purchased': False, 'cart_abandoned': True},
        {'clicks': 22, 'purchased': True, 'cart_abandoned': False}
    ],
    'support_tickets': [
        {'type': 'delivery', 'resolved': True},
        {'type': 'product', 'resolved': False}
    ],
    'years_active': 3,
    'current_month': 7
}

# Calculate customer priority
is_premium = True
priority_score = calculate_priority(customer_data, is_premium)

# Distracting final calculations that aren't used
final_engagement = calculate_engagement(customer_data['browsing_history'])
seasonal_factor = apply_seasonal_boost(100, customer_data['current_month'])
weighted_engagement = final_engagement * seasonal_factor / 100

print(f"Result: {priority_score}")