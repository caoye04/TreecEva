from collections import defaultdict

def calculate_portfolio_adjustments(daily_changes):
    adjustments = defaultdict(int)
    cumulative = 0
    final_adjustment = 0
    
    for idx, change in enumerate(daily_changes):
        if idx % 2 == 0:
            adjustments[idx] = change * 2
        else:
            adjustments[idx] = change - 3
            
        cumulative += adjustments[idx]
        
        if cumulative > 100:
            final_adjustment = cumulative // idx if idx != 0 else 0
            break
        elif idx == len(daily_changes) - 1:
            final_adjustment = cumulative % 10
            
    return final_adjustment

# Daily changes in portfolio value
market_data = [5, 12, 8, 20, 15, 25, 30, 18, 22, 35]

result = calculate_portfolio_adjustments(market_data)
print(f"Result: {result}")