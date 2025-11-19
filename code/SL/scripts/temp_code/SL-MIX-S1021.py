import math
from functools import lru_cache

def calculate_adjusted_return(base_rate, years, risk_factor):
    if years <= 0:
        return 1.0
    compounded = (1 + base_rate) ** years
    adjusted = compounded * math.exp(-risk_factor * math.log(years + 1))
    return adjusted

@lru_cache(maxsize=None)
def compute_investment_path(annual_return, time_horizon, volatility):
    if time_horizon == 0:
        return 1000  # Base investment
    prev_value = compute_investment_path(annual_return, time_horizon - 1, volatility)
    growth_factor = calculate_adjusted_return(annual_return, 1, volatility)
    current_value = prev_value * growth_factor
    return current_value

# Investment parameters
initial_capital = 1000
expected_annual_return = 0.08
risk_volatility = 0.15
investment_duration = 10

# Dynamic programming table for memoization
portfolio_values = {}
for year in range(investment_duration + 1):
    portfolio_values[year] = compute_investment_path(expected_annual_return, year, risk_volatility)

# Calculate final portfolio value with lambda adjustment
adjustment_lambda = lambda val, factor: val * (1 + math.log(factor + 1))
final_portfolio_value = adjustment_lambda(portfolio_values[investment_duration], risk_volatility)

print(f"Result: {int(final_portfolio_value)}")