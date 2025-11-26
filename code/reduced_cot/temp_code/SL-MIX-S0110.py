def calculate_investment_growth(principal_amount, annual_rate, years):
    # Initial setup with some irrelevant calculations
    initial_deposit = principal_amount * 2.5
    compound_frequency = 4
    monthly_adjustment = annual_rate / 12.0
    
    # Misleading intermediate results
    quarterly_interest = annual_rate / compound_frequency
    daily_rate = annual_rate / 365.0
    
    # Some dead code paths
    if initial_deposit > 10000:
        bonus = 500
    else:
        bonus = 100
    
    # Slicing operations with irrelevant data
    investment_periods = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    selected_periods = investment_periods[1:8:2]
    period_sum = sum(selected_periods)
    
    # Logical operations with bitwise mixing
    rate_modifier = (annual_rate > 5 and annual_rate < 15)
    time_adjustment = (years % 2 == 0) or (years % 3 == 0)
    
    # More misleading calculations
    compounded_amount = principal_amount * (1 + annual_rate/100) ** years
    simple_interest = principal_amount * annual_rate * years / 100
    
    # Key computation with slicing influence
    principal = principal_amount
    rate = annual_rate
    time = years
    
    # The critical statement
    final_balance = principal + (principal * (rate / 100) * time)
    
    # More irrelevant operations after the key statement
    redundant_calculation = final_balance * 0.95
    alternative_result = compounded_amount - simple_interest
    
    print(f"Target result: {final_balance}")
    return final_balance

# Test execution
principal_amount = 1500
annual_rate = 8.5
years = 3
result = calculate_investment_growth(principal_amount, annual_rate, years)