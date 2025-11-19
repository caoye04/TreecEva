import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

class PortfolioMetrics:
    def __init__(self, returns_data):
        self.returns = returns_data
        self.prime_periods = []
    
    def __enter__(self):
        # Find prime periods in the first 20 indices
        self.prime_periods = [i for i in range(2, min(21, len(self.returns))) if is_prime(i)]
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def calculate_weighted_returns(self):
        weighted_scores = []
        for idx in self.prime_periods:
            if idx < len(self.returns):
                # Exponential weighting with natural log of index
                weight = math.log(idx) * self.returns[idx-1]
                weighted_scores.append(weight)
        return weighted_scores
    
    def greedy_rebalancing_score(self, scores):
        # Greedy algorithm to select non-adjacent periods maximizing sum
        if not scores:
            return 0
        if len(scores) == 1:
            return scores[0]
        
        prev_prev = scores[0]
        prev = max(scores[0], scores[1])
        
        for i in range(2, len(scores)):
            current = max(prev, prev_prev + scores[i])
            prev_prev = prev
            prev = current
        
        return prev

# Simulated cryptocurrency returns data
portfolio_returns = [0.02, -0.01, 0.03, 0.05, -0.02, 0.04, 0.01, -0.03, 0.06, 0.02, 
                    -0.01, 0.04, 0.03, -0.02, 0.05, 0.01, -0.04, 0.02, 0.03, -0.01,
                    0.04, -0.02, 0.01, 0.03, -0.03]

with PortfolioMetrics(portfolio_returns) as analyzer:
    weighted_performance = analyzer.calculate_weighted_returns()
    optimal_rebalance_score = analyzer.greedy_rebalancing_score(weighted_performance)
    
    # Apply final transformation using LCM with fixed value
    final_lcm = lcm(12, 18)
    optimal_rebalance_score = round(optimal_rebalance_score * final_lcm, 6)

print(f"Result: {optimal_rebalance_score}")