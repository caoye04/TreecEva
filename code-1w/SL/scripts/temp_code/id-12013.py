def analyze_financial_health():
    base_rate = 12.5
    growth_factor = 1.08
    inflation_adjustment = 0.94
    tax_burden = 0.23

    # Simulated quarterly earnings with conditional scaling
    q1_earnings = 45000 * growth_factor
    q2_earnings = 47500 * growth_factor
    q3_earnings = 46200 * growth_factor
    q4_earnings = 49800 * growth_factor

    total_annual_revenue = q1_earnings + q2_earnings + q3_earnings + q4_earnings
    adjusted_revenue = total_annual_revenue * inflation_adjustment

    # Operational cost calculations with bitwise efficiency flag
    base_operational_cost = 120000
    efficiency_bonus = 0b1101 & 0b1011  # Bitwise AND to determine overhead reduction
    overhead_discount = efficiency_bonus * 1500
    operational_cost = base_operational_cost - overhead_discount

    # Tax computation with conditional expression
    taxable_income = adjusted_revenue - operational_cost
    tax_liability = tax_burden * taxable_income if taxable_income > 0 else 0
    net_profit = adjusted_revenue - operational_cost - tax_liability

    # Auxiliary financial indicators (distractor variables)
    liquidity_ratio = net_profit / operational_cost if operational_cost != 0 else 0
    break_even_point = operational_cost / (growth_factor * 0.75)
    projected_loss = not (q1_earnings < q2_earnings < q3_earnings < q4_earnings)

    # Core system integrity check based on sequential performance
    performance_trend = (q4_earnings > q3_earnings) and (q2_earnings > q1_earnings)
    stability_metric = abs(q4_earnings - q1_earnings) / q1_earnings
    system_integrity = performance_trend and stability_metric < 0.25

    revenue_stream = adjusted_revenue if net_profit > 0 else 0

    # Critical statement determining audit outcome
    final_audit = system_integrity and (revenue_stream > operational_cost)

    # Threshold balance derived from audit result and profit-sharing logic
    bonus_pool = net_profit * 0.15 if final_audit else 0
    threshold_balance = int((net_profit - bonus_pool) * 0.01) if net_profit > 0 else 0

    # Dead code path - irrelevant to final result
    if False:
        fallback_reserve = 10000
        threshold_balance += fallback_reserve // 1000

    return threshold_balance

result = analyze_financial_health()
print(f"Result: {result}")