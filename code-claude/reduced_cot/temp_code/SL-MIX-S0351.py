def calculate_portfolio_metrics(data, include_speculative=False):
    total_value = sum(data.values())
    risk_scores = {
        'low': lambda x: x * 0.05,
        'medium': lambda x: x * 0.12,
        'high': lambda x: x * 0.22,
        'speculative': lambda x: x * 0.45
    }
    
    risk_adjusted = 0
    for category, amount in data.items():
        if category in risk_scores and (include_speculative or category != 'speculative'):
            risk_adjusted += risk_scores[category](amount)
    
    # Unused calculations to track theoretical performance
    theoretical_max = total_value * 0.45
    theoretical_min = total_value * 0.05
    volatility_index = (theoretical_max - theoretical_min) / total_value
    
    return risk_adjusted

def apply_tax_adjustments(value, tax_rates):
    # Complex but mostly irrelevant tax calculations
    base_tax = value * tax_rates.get('base', 0.15)
    progressive_tax = 0
    thresholds = [(1000, 0.05), (5000, 0.08), (20000, 0.12)]
    remaining = value
    
    for threshold, rate in thresholds:
        if remaining > threshold:
            progressive_tax += threshold * rate
            remaining -= threshold
        else:
            progressive_tax += remaining * rate
            remaining = 0
            break
    
    if remaining > 0:
        progressive_tax += remaining * 0.15
    
    # Only the capital_gains_factor is actually used
    capital_gains_factor = 1 - tax_rates.get('capital_gains', 0.25)
    estate_tax = value * tax_rates.get('estate', 0.4) if value > 100000 else 0
    
    return capital_gains_factor

def calculate_optimal_investment(portfolio_data, tax_rates):
    # Several misleading calculations that don't affect the final result
    market_sentiment = {'bullish': 1.2, 'neutral': 1.0, 'bearish': 0.8}
    current_sentiment = market_sentiment.get('neutral')
    inflation_adjustment = 0.97  # 3% inflation reduction
    
    # Distractor variables and calculations
    portfolio_diversity = len(portfolio_data)
    risk_tolerance = 0.75 if portfolio_diversity > 3 else 0.6
    market_volatility = 0.18
    
    # These values are used in the final calculation
    base_value = calculate_portfolio_metrics(portfolio_data)
    tax_factor = apply_tax_adjustments(base_value, tax_rates)
    
    # More distracting calculations
    if risk_tolerance > market_volatility:
        opportunity_cost = base_value * 0.03
    else:
        opportunity_cost = base_value * 0.05
    
    # Unused branching logic
    if current_sentiment == market_sentiment['bullish']:
        market_premium = base_value * 0.08
    elif current_sentiment == market_sentiment['bearish']:
        market_discount = base_value * 0.06
    else:
        market_adjustment = 0
    
    # Calculation with bit operations as distraction
    binary_flag = 0b1101
    binary_mask = 0b1100
    operation_code = (binary_flag & binary_mask) >> 2  # Equals 3
    
    # The actual calculation that determines the result
    raw_investment = (base_value * 0.75) * tax_factor
    adjustment_factor = operation_code / 10  # 3/10 = 0.3
    optimal_investment = raw_investment * (1 + adjustment_factor)
    
    # More unused calculations
    alternative_strategy = raw_investment * (1 - market_volatility)
    conservative_option = base_value * 0.5 * tax_factor
    aggressive_option = base_value * 0.9 * tax_factor
    
    return optimal_investment

# Portfolio data and tax rates
portfolio_data = {
    'low': 12000,
    'medium': 28000,
    'high': 15000,
    'speculative': 5000
}

tax_rates = {
    'base': 0.15,
    'capital_gains': 0.20,
    'estate': 0.4
}

# Calculate and display the optimal investment amount
optimal_investment = calculate_optimal_investment(portfolio_data, tax_rates)
print(f"Result: {optimal_investment}")