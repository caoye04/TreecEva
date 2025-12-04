def calculate_priority(customer_data, tier):
    base_points = 100
    tier_multipliers = {
        "Bronze": 1.0,
        "Silver": 1.5,
        "Gold": 2.0,
        "Platinum": 3.0
    }
    
    activity_score = 0
    loyalty_bonus = 0
    seasonal_factor = 1.2  # Current seasonal promotion
    
    # Extract customer information
    purchases = customer_data.get("purchases", 0)
    returns = customer_data.get("returns", 0)
    years = customer_data.get("loyalty_years", 0)
    
    # Calculate activity score based on purchase history
    if purchases > 0:
        activity_ratio = max(0, (purchases - returns) / purchases)
        activity_score = int(purchases * activity_ratio)
    
    # Apply loyalty bonus for customers with more than 2 years
    if years > 2:
        loyalty_bonus = years * 5
        seasonal_discount = seasonal_factor * 0.1  # Not used in final calculation
    
    # Special promotion check - not affecting final score
    promo_eligible = tier in ["Gold", "Platinum"] and purchases > 10
    promo_code = "SPR2023" if promo_eligible else ""  
    
    # Calculate final priority score
    tier_factor = tier_multipliers.get(tier, 1.0)
    potential_value = base_points * tier_factor + activity_score + loyalty_bonus
    
    # Additional metrics for reporting - not used in final calculation
    engagement_metric = (purchases * 2) - returns
    retention_risk = "Low" if years > 3 and returns < purchases * 0.2 else "Medium"
    
    return int(potential_value)

# Customer data dictionary
customer_data = {
    "customer_id": "C12345",
    "name": "John Smith",
    "purchases": 15,
    "returns": 3,
    "loyalty_years": 4,
    "preferred_contact": "email"
}

# Calculate priority score for Gold tier
priority_score = calculate_priority(customer_data, "Gold")
print(f"Result: {priority_score}")