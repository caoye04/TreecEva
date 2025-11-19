from functools import reduce

daily_rate_lambda = lambda annual_rate: annual_rate / 365.0
compound_factor = lambda rate, periods: (1 + rate) ** periods

initial_principal = 1000.0
nominal_annual_rate = 0.05
compounding_periods = 365 * 2

daily_rate = daily_rate_lambda(nominal_annual_rate)
final_amount = initial_principal * compound_factor(daily_rate, compounding_periods)

print(f'Result: {final_amount:.2f}')