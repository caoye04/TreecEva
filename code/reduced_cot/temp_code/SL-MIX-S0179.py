import heapq
from collections import deque

def exchange_rate_processor(initial_capital, rate_fluctuations):
    # State definitions
    STATE_STABLE = 0
    STATE_VOLATILE = 1
    STATE_CRITICAL = 2
    
    current_state = STATE_STABLE
    portfolio_value = initial_capital
    min_heap = []
    fluctuation_queue = deque(rate_fluctuations)
    
    while fluctuation_queue:
        rate_change = fluctuation_queue.popleft()
        
        # State transition logic
        if abs(rate_change) > 0.05:
            current_state = STATE_VOLATILE
        elif abs(rate_change) > 0.10:
            current_state = STATE_CRITICAL
        else:
            current_state = STATE_STABLE
            
        # Early return conditions
        if current_state == STATE_CRITICAL and portfolio_value < 900:
            return portfolio_value * 0.95  # Emergency liquidation penalty
        
        # Apply rate change
        portfolio_value *= (1 + rate_change)
        
        # Track minimum values in heap
        heapq.heappush(min_heap, portfolio_value)
        
        # Volatility response
        if current_state == STATE_VOLATILE:
            adjustment = 1.0 + (rate_change * 0.1)
            portfolio_value *= adjustment
            heapq.heappush(min_heap, portfolio_value)
    
    # Final adjustment based on minimum value encountered
    lowest_valuation = heapq.heappop(min_heap)
    if lowest_valuation < initial_capital * 0.9:
        portfolio_value -= 50  # Recovery fee
    
    return portfolio_value

# Configuration
initial_investment = 1000.0
market_fluctuations = [0.02, -0.03, 0.06, -0.08, 0.04, -0.02, 0.01]

# Execute processor
final_portfolio_value = exchange_rate_processor(initial_investment, market_fluctuations)
print(f"Result: {final_portfolio_value}")