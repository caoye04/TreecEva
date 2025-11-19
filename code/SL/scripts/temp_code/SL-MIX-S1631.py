import math

def compute_adjusted_compound_interest(principal, rate, years, depth=0):
    if years <= 0:
        return principal
    
    # Volatility correction lambda
    volatility_correction = lambda p, d: p * (1 + 0.01 * math.sin(d))
    
    # Apply interest
    new_principal = principal * (1 + rate)
    
    # Apply volatility correction based on depth
    corrected_principal = volatility_correction(new_principal, depth)
    
    # Recursive call with decremented years and incremented depth
    return compute_adjusted_compound_interest(corrected_principal, rate, years - 1, depth + 1)

# Initial parameters
initial_principal = 1000.0
annual_rate = 0.05
investment_years = 4

# Compute final balance
adjusted_balance = compute_adjusted_compound_interest(initial_principal, annual_rate, investment_years)
print(f"Result: {adjusted_balance:.6f}")