def analyze_transaction_patterns(history):
    # Analyze customer transaction patterns (unused function)
    pattern_score = 0
    for transaction in history:
        if transaction > 500:
            pattern_score += 2
        elif transaction > 100:
            pattern_score += 1
    return pattern_score * 1.5

def calculate_risk_factor(credit_score, account_age):
    # Calculate risk factor based on credit score and account age
    base_risk = 100 - (credit_score / 10)
    age_adjustment = min(account_age / 12, 5)  # Cap at 5 years
    return max(base_risk - age_adjustment * 3, 10)  # Minimum risk is 10

def calculate_potential_value(income, spending_ratio):
    # Calculate potential customer value (misleading function)
    base_value = income * 0.01
    multiplier = 1 + (spending_ratio * 0.5)
    return base_value * multiplier

def apply_seasonal_adjustment(score, month):
    # Apply seasonal adjustments (distraction)
    seasonal_factors = {
        1: 0.95, 2: 0.92, 3: 0.98, 4: 1.02,
        5: 1.05, 6: 1.03, 7: 1.00, 8: 0.97,
        9: 1.02, 10: 1.04, 11: 1.08, 12: 1.10
    }
    return score * seasonal_factors.get(month, 1.0)

def calculate_final_score(customer_data, metrics):
    # Extract customer information
    credit_score = customer_data.get('credit_score', 650)
    account_age = customer_data.get('account_age', 24)  # in months
    income = customer_data.get('income', 50000)
    
    # Misleading variables
    transaction_history = customer_data.get('transactions', [300, 150, 420, 80])
    spending_habits = customer_data.get('spending_habits', 'moderate')
    current_month = customer_data.get('month', 6)
    
    # Distracting computations
    pattern_value = analyze_transaction_patterns(transaction_history)
    potential_value = calculate_potential_value(income, 0.7)
    seasonal_factor = apply_seasonal_adjustment(100, current_month)
    
    # Actual relevant computation
    risk_factor = calculate_risk_factor(credit_score, account_age)
    
    # Performance metrics impact (key calculation)
    base_score = 80 - (risk_factor * 0.5)
    
    # Apply performance adjustments
    adjustment = 0
    if 'response_time' in metrics:
        # Lower response time is better (under 24 hours = 5 points)
        response_hours = metrics['response_time']
        adjustment += 10 if response_hours < 24 else (5 if response_hours < 48 else 0)
    
    if 'resolution_rate' in metrics:
        # Higher resolution rate is better
        resolution = metrics['resolution_rate']
        adjustment += resolution * 10
    
    # Apply tiered loyalty bonus (misleading)
    loyalty_tier = customer_data.get('loyalty_tier', 'silver')
    loyalty_bonus = {'bronze': 2, 'silver': 5, 'gold': 10, 'platinum': 15}.get(loyalty_tier, 0)
    
    # Conditional expression for final calculation
    engagement_factor = 1.2 if account_age > 36 else 1.0
    
    # Lambda for priority calculation (appears complex but actually simple)
    priority_calculator = lambda base, adj, factor: (base + adj) * factor
    
    # This is the key statement - it calculates the final priority score
    priority_score = priority_calculator(base_score, adjustment, engagement_factor)
    
    # More distracting calculations after the key result
    normalized_score = max(min(priority_score, 100), 0)
    weighted_average = (normalized_score * 0.7) + (loyalty_bonus * 0.3)
    
    # Return the priority score (not the weighted average or normalized score)
    return round(priority_score, 2)

# Customer data dictionary
customer_data = {
    'customer_id': 'C1092',
    'credit_score': 720,
    'account_age': 42,  # months
    'income': 65000,
    'transactions': [250, 340, 120, 500, 80],
    'spending_habits': 'high',
    'month': 9,
    'loyalty_tier': 'gold'
}

# Performance metrics dictionary
performance_metrics = {
    'response_time': 18,  # hours
    'resolution_rate': 0.85,  # 85%
    'customer_satisfaction': 4.2  # on scale of 5 (distraction)
}

# Calculate priority score
priority_score = calculate_final_score(customer_data, performance_metrics)
print(f"Result: {priority_score}")
