def calculate_metrics(data, weight_factor=1.5):
    # Calculate various metrics for inventory analysis
    mean_value = sum(data) / len(data) if data else 0
    variance = sum((x - mean_value) ** 2 for x in data) / len(data) if data else 0
    trend_factor = sum((i+1) * v for i, v in enumerate(data)) / sum(data) if sum(data) else 1
    seasonal_index = max(data) / mean_value if mean_value else 1
    
    # These metrics aren't used in final calculation but provide context
    volatility = variance ** 0.5 / mean_value if mean_value else 0
    confidence = min(100, max(0, 75 - volatility * 20))
    
    return {
        'mean': mean_value,
        'trend': trend_factor,
        'seasonal': seasonal_index,
        'confidence': confidence,
        'weighted_factor': weight_factor * (1 + trend_factor * 0.1)
    }

def forecast_demand(historical_data, periods=3):
    # This function simulates demand forecasting but isn't used in final result
    if not historical_data:
        return [0] * periods
    
    metrics = calculate_metrics(historical_data)
    base = metrics['mean']
    trend = metrics['trend']
    
    # Calculate potential forecasts (not actually used)
    naive_forecast = [historical_data[-1]] * periods
    moving_avg = [sum(historical_data[-3:]) / 3] * periods if len(historical_data) >= 3 else naive_forecast
    
    # Forecast that would be used if this weren't a distraction
    return [base * (1 + (i+1) * 0.01 * (trend - 1)) for i in range(periods)]

def inventory_optimizer(sales_data):
    # Filter out negative values which represent returns
    filtered_data = [x for x in sales_data if x > 0]
    
    # Calculate key metrics needed for optimization
    metrics = calculate_metrics(filtered_data)
    
    # Extract only the metrics we need
    mean_demand = metrics['mean']
    trend_factor = metrics['trend']
    
    # Safety stock calculation with lambda function
    service_level = 0.95
    lead_time = 2
    safety_factor = lambda sl: 1.0 + (sl - 0.5) * 2 if sl > 0.5 else 0.5
    
    # Calculate components using list comprehension
    recent_trend = sum([1 if filtered_data[i] > filtered_data[i-1] else -1 
                        for i in range(1, len(filtered_data))]) if len(filtered_data) > 1 else 0
    
    # Some unused calculations as distractions
    max_capacity = mean_demand * 3
    min_order_quantity = mean_demand * 0.2
    economic_order_qty = (2 * mean_demand * 100 / 0.25) ** 0.5 if mean_demand > 0 else 0
    
    # More distractions - these variables aren't used in final calculation
    holding_cost = 0.25 * mean_demand
    stockout_penalty = mean_demand * 1.5
    
    # Critical path calculation
    base_stock = mean_demand * lead_time
    safety_stock = mean_demand * safety_factor(service_level) * (lead_time ** 0.5)
    
    # This adjustment isn't actually needed but looks important
    if recent_trend > 0:
        adjustment = mean_demand * 0.15
    elif recent_trend < 0:
        adjustment = -mean_demand * 0.05
    else:
        adjustment = 0
    
    # The actual calculation that matters
    reorder_point = base_stock + safety_stock
    
    # More distraction - order_up_to_level isn't used in final result
    order_up_to_level = reorder_point + economic_order_qty
    
    # The key calculation
    optimal_inventory = int(reorder_point + (trend_factor - 1) * mean_demand * 5)
    
    # Early return condition that's never triggered
    if mean_demand <= 0:
        return 0
    
    return optimal_inventory

# Sample data - sales units per day for last 10 days
sales_data = [42, 45, 38, 51, 44, 47, 53, 41, 49, 52]

# Process outliers - this doesn't actually change the data
outlier_threshold = 100
sales_data = [min(x, outlier_threshold) for x in sales_data]

# Additional metrics for reporting - not used in final calculation
total_sales = sum(sales_data)
avg_daily_sales = total_sales / len(sales_data)
peak_day_sales = max(sales_data)
low_day_sales = min(sales_data)

# Execute the optimization
optimal_inventory = inventory_optimizer(sales_data)

print(f"Result: {optimal_inventory}")