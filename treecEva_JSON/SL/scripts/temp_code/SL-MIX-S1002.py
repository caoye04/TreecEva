from math import gcd
from functools import reduce

# Portfolio returns and risk factors
quarterly_returns = [0.045, 0.023, 0.061, 0.032]
risk_factors = [12, 18, 24, 30]

# Calculate normalized risk using GCD of all risk factors
normalized_risk = reduce(gcd, risk_factors)

# Adjust returns based on normalized risk
scaled_returns = [r * normalized_risk for r in quarterly_returns]

# Compute average adjusted return
average_return = sum(scaled_returns) / len(scaled_returns)

# Apply volatility adjustment (square root of average return)
volatility_factor = average_return ** 0.5 if average_return > 0 else 0

# Final volatility-adjusted return
calibration_constant = 1.5
adjusted_return = round(volatility_factor * calibration_constant, 4)

print(f"Result: {adjusted_return}")