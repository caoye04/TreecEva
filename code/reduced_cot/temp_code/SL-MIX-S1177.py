def log_computation_steps(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.steps.append(result)
        return result
    wrapper.steps = []
    return wrapper

def compute_volatility(market_returns, weights):
    @log_computation_steps
    def weighted_return(index):
        return market_returns[index] * weights[index]
    
    @log_computation_steps
    def squared_deviation(index):
        wr = weighted_return(index)
        mean_wr = sum(weighted_return.steps) / len(weighted_return.steps)
        return (wr - mean_wr) ** 2 if index > 0 else 0
    
    n = len(market_returns)
    dp = [0] * n
    dp[0] = squared_deviation(0)
    
    for i in range(1, n):
        dp[i] = dp[i-1] + squared_deviation(i)
        if i >= 2 and dp[i] > dp[i-1] and dp[i-1] > dp[i-2]:
            dp[i] *= 1.5  # Amplify trend confirmation
    
    avg_squared_dev = dp[-1] / n
    risk_adjustment = 1.0
    
    # Binary search for optimal risk adjustment factor
    low, high = 0.5, 2.0
    for _ in range(10):  # 10 iterations for precision
        mid = (low + high) / 2
        adjusted_risk = avg_squared_dev * mid
        if adjusted_risk > 0.04:
            high = mid
        else:
            low = mid
        
        # Short-circuit to prevent over-adjustment
        if abs(high - low) < 1e-6:
            break
    
    risk_adjustment = (low + high) / 2
    final_risk_score = avg_squared_dev * risk_adjustment
    
    return final_risk_score

# Market data simulation
market_returns = [0.02, -0.01, 0.03, -0.02, 0.01, 0.04, -0.03, 0.02]
weights = [0.15, 0.10, 0.20, 0.10, 0.05, 0.25, 0.10, 0.05]

final_risk_score = compute_volatility(market_returns, weights)
print(f"Result: {final_risk_score}")