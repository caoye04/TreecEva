import math

def calculate_adjusted_compound(principal, rate, time, adjustment_factor, depth=0):
    if depth > 3:
        return principal
    adjusted_rate = rate + math.sin(depth) * 0.01
    compounded = principal * (1 + adjusted_rate) ** time
    correction = (compounded - principal) * adjustment_factor
    corrected_value = compounded - correction
    return calculate_adjusted_compound(corrected_value, rate, time, adjustment_factor, depth + 1)

initial_investment = 10000.0
interest_rate = 0.05
investment_period = 2.5
market_volatility = 0.02

portfolio_values = [calculate_adjusted_compound(initial_investment, interest_rate, investment_period, market_volatility)]
adjusted_values = [val * (1 + math.log(1 + idx * 0.01)) for idx, val in enumerate(portfolio_values)]
final_portfolio_value = sum(adjusted_values) + (lambda x: x ** 0.5 if x > 0 else 0)(sum(adjusted_values) - 10000)
print(f"Result: {final_portfolio_value}")