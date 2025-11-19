from functools import reduce

def compute_total_revenue():
    prices = [2.50, 3.00, 2.75]
    quantities = [40, 25, 30]
    
    # Calculate revenue per item using map
    revenues = list(map(lambda p, q: p * q, prices, quantities))
    
    # Sum up all revenues using reduce
    total_revenue = reduce(lambda x, y: x + y, revenues)
    
    return total_revenue

# Execution point
final_revenue = compute_total_revenue()
print(f"Result: {final_revenue}")