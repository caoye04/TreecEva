import math

def log_steps(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def calculate_tier_rate(principal, tier):
    rates = [0.02, 0.03, 0.05, 0.07]
    if tier >= len(rates):
        return rates[-1]
    return rates[tier]

@log_steps
def compound_yield(amt, years, tier=0):
    if years <= 0:
        return amt
    if amt < 1000:
        current_rate = calculate_tier_rate(amt, tier)
        return compound_yield(amt * (1 + current_rate), years - 1, tier + 1)
    else:
        half_years = years // 2
        first_half = compound_yield(amt, half_years, tier)
        second_half = compound_yield(first_half, years - half_years, tier + 1)
        return second_half

investment_portfolio = 850.0
holding_duration = 5
final_yield = compound_yield(investment_portfolio, holding_duration)
print(f'Result: {round(final_yield, 2)}')