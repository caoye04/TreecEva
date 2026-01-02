def analyze_financial_flow(transactions, baseline):
    inflows = [t for t in transactions if t > 0]
    outflows = [abs(t) for t in transactions if t < 0]
    total_inflow = sum(inflows)
    total_outflow = sum(outflows)
    
    growth_trend = []
    for i in range(1, len(inflows)):
        growth_trend.append(inflows[i] - inflows[i-1])
    
    avg_growth = sum(growth_trend) / len(growth_trend) if growth_trend else 0
    
    surplus = total_inflow - total_outflow
    reserve_ratio = surplus / total_inflow if total_inflow > 0 else 0
    
    # Irrelevant computation: simulating deprecated metric
    deprecated_metric = 0
    for x in outflows:
        deprecated_metric += x * 0.1
        if deprecated_metric > 100:
            break
    
    # Another distraction: historical peak tracking (not used)
    peak_inflow = max(inflows) if inflows else 0
    historical_highs = [p for p in inflows if p > baseline * 1.5]
    
    net_inflows = [inflows[i] - (outflows[i] if i < len(outflows) else 0) for i in range(max(len(inflows), len(outflows)))]
    
    adjustment_factor = 1.0
    if reserve_ratio > 0.3:
        adjustment_factor = 1.25
    elif reserve_ratio < 0.1:
        adjustment_factor = 0.75
    
    # Key statement with target variable
    threshold_balance = net_inflows[-1] * adjustment_factor if net_inflows else 0
    
    # Dead code path (never executed under normal input)
    if False:
        fallback_value = sum(net_inflows) // len(net_inflows)
        threshold_balance = fallback_value

    return threshold_balance

# Simulate execution
transaction_data = [120, -45, 200, -80, 50, 300, -150, -30]
baseline_target = 100
result = analyze_financial_flow(transaction_data, baseline_target)
print(f"Result: {result}")