# Calculate sales bonus based on performance metrics

def initialize_metrics():
    # Initial sample data for tracking
    return [120, 85, 150, 95, 200]

# Main sales data for analysis
sales_data = [110, 95, 145, 80, 175, 200]
performance_threshold = 100
base_multiplier = 0.5

# Function to process sales performance
def bonus_calculator(sales):
    # Sort sales in descending order to prioritize top performers
    sorted_sales = sorted(sales, reverse=True)
    
    # Calculate average of top 3 sales
    top_sales_avg = sum(sorted_sales[:3]) / 3
    
    # Apply performance adjustment
    if top_sales_avg > 150:
        adjustment = 1.2
    else:
        adjustment = 1.0
    
    # Calculate bonus using lambda function
    bonus_formula = lambda x, y: (x - performance_threshold) * base_multiplier * y
    return bonus_formula(top_sales_avg, adjustment)

# Compute the sales bonus
sales_bonus = bonus_calculator(sales_data)
print(f"Result: {sales_bonus}")