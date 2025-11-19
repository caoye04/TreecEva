import itertools
from functools import reduce
import statistics

def calculate_portfolio_variance(weights, covariance_matrix):
    return sum(weights[i] * weights[j] * covariance_matrix[i][j] 
               for i in range(len(weights)) 
               for j in range(len(weights)))

def optimize_portfolio(returns_history, covariance_matrix):
    n_assets = len(returns_history)
    time_periods = len(returns_history[0])
    
    # Dynamic programming table for optimal allocations
    dp_table = [[0.0 for _ in range(time_periods)] for _ in range(n_assets)]
    
    # Initialize first period with equal weights
    initial_weights = [1.0/n_assets for _ in range(n_assets)]
    dp_table[0][0] = calculate_portfolio_variance(initial_weights, covariance_matrix)
    
    # Fill DP table using statistical analysis
    for t in range(1, time_periods):
        period_returns = [returns_history[i][t] for i in range(n_assets)]
        mean_return = statistics.mean(period_returns)
        
        # Generate candidate weight combinations
        weight_candidates = []
        for combo in itertools.combinations_with_replacement(range(n_assets), n_assets):
            weights = [0.0] * n_assets
            for idx in combo:
                weights[idx] += 1.0/n_assets
            weight_candidates.append(weights)
        
        # Find optimal allocation for this period
        min_variance = float('inf')
        optimal_weights = None
        
        for weights in weight_candidates:
            variance = calculate_portfolio_variance(weights, covariance_matrix)
            if variance < min_variance:
                min_variance = variance
                optimal_weights = weights
        
        # Update DP table
        for i in range(n_assets):
            dp_table[i][t] = dp_table[i][t-1] + optimal_weights[i] * mean_return
    
    # Find optimal allocation index
    final_variances = [dp_table[i][-1] for i in range(n_assets)]
    optimal_allocation_index = final_variances.index(min(final_variances))
    
    return optimal_allocation_index

# Asset returns history (3 assets, 4 time periods)
asset_returns = [
    [0.05, 0.02, -0.01, 0.03],
    [0.03, 0.04, 0.02, -0.02],
    [-0.02, 0.01, 0.04, 0.01]
]

# Covariance matrix
cov_matrix = [
    [0.002, 0.001, 0.0005],
    [0.001, 0.003, 0.001],
    [0.0005, 0.001, 0.002]
]

optimal_allocation_index = optimize_portfolio(asset_returns, cov_matrix)
print(f"Result: {optimal_allocation_index}")