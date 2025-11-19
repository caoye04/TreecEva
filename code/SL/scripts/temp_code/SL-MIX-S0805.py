def compute_conversion_efficiency():
    # Market volatility modeled with Fibonacci sequence
    def fibonacci(n):
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
    # Valid transaction codes
    valid_codes = {101, 102, 104, 107, 111, 116}
    premium_codes = frozenset({107, 111, 116})
    
    # Conversion rates with dynamic adjustments
    base_rates = {101: 0.85, 102: 0.92, 104: 0.78, 107: 1.15, 111: 1.22, 116: 1.30}
    volatility_factor = {code: fibonacci(i+5) for i, code in enumerate(valid_codes)}
    
    # Calculate adjusted rates
    adjusted_rates = {code: rate * (1 + volatility_factor[code]/1000) 
                     for code, rate in base_rates.items()}
    
    # Merge with premium multipliers
    premium_multipliers = {107: 1.05, 111: 1.08, 116: 1.10}
    final_rates = adjusted_rates | {code: adjusted_rates[code] * premium_multipliers[code] 
                                   for code in premium_codes}
    
    # Efficiency calculation using set intersection
    processed_codes = {101, 104, 107, 111}
    successful_conversions = valid_codes & processed_codes
    
    # Compute weighted efficiency score
    efficiency_components = [final_rates[code] * (i+1) for i, code in enumerate(successful_conversions)]
    final_efficiency_score = int(sum(efficiency_components) * 100)
    
    return final_efficiency_score

final_efficiency_score = compute_conversion_efficiency()
print(f"Result: {final_efficiency_score}")