import math

def fibonacci_sequence(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def compute_quarterly_returns(base_return, quarters=8):
    fib_weights = [x for x in fibonacci_sequence(quarters)]
    weighted_returns = [(base_return * weight) for weight in fib_weights]
    return weighted_returns

def volatility_correction(returns):
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return) ** 2 for r in returns) / len(returns)
    std_dev = math.sqrt(variance)
    adjusted_returns = [
        r if abs(r - mean_return) <= std_dev else 
        (mean_return + std_dev) if r > mean_return else (mean_return - std_dev)
        for r in returns
    ]
    return adjusted_returns

def calculate_stability_score(adjusted_returns):
    positive_count = sum(1 for r in adjusted_returns if r > 0)
    negative_count = sum(1 for r in adjusted_returns if r < 0)
    neutral_count = len(adjusted_returns) - positive_count - negative_count
    return positive_count > negative_count and neutral_count <= 2

def main():
    base_return = 0.05
    quarterly_returns = compute_quarterly_returns(base_return)
    adjusted_returns = volatility_correction(quarterly_returns)
    
    stability_achieved = False
    iteration = 0
    max_iterations = 3
    
    while not stability_achieved and iteration < max_iterations:
        adjusted_returns = volatility_correction(adjusted_returns)
        stability_achieved = calculate_stability_score(adjusted_returns)
        iteration += 1
        
        # Early return if stability achieved
        if stability_achieved:
            break
    
    final_mean = sum(adjusted_returns) / len(adjusted_returns)
    final_variance = sum((r - final_mean) ** 2 for r in adjusted_returns) / len(adjusted_returns)
    
    # Ternary operator for final adjustment
    final_adjusted_return = final_mean * 1.1 if final_variance < 0.01 else final_mean * 0.9
    
    print(f"Result: {final_adjusted_return}")
    return final_adjusted_return

final_adjusted_return = main()