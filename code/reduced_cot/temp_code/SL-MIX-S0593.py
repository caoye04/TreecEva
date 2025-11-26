def calculate_business_metrics(transactions):
    total_revenue = sum([t['amount'] for t in transactions if t['type'] == 'sale'])
    operating_costs = sum([t['amount'] for t in transactions if t['type'] == 'expense'])
    
    # Distractor calculations that don't affect final profit
    transaction_count = len(transactions)
    avg_transaction = total_revenue / transaction_count if transaction_count > 0 else 0
    
    # Additional intermediate variables
    revenue_tax = total_revenue * 0.18  # Not actually used
    cost_analysis = operating_costs * 1.1  # Distractor
    
    gross_profit = total_revenue - operating_costs
    overhead_fixed = 2500  # Fixed overhead costs
    
    # Using enumerate to iterate with index (mandatory feature)
    profit_adjustments = []
    for idx, transaction in enumerate(transactions):
        if transaction['type'] == 'sale':
            adjustment = transaction['amount'] * 0.95
            profit_adjustments.append(adjustment)
    
    adjusted_revenue = sum(profit_adjustments)
    net_profit = adjusted_revenue - operating_costs - overhead_fixed
    
    # Final calculation (key statement)
    final_calculation = net_profit * 1.0
    print(f"Result: {net_profit}")

# Sample transaction data
transaction_data = [
    {'type': 'sale', 'amount': 15000},
    {'type': 'sale', 'amount': 8500},
    {'type': 'expense', 'amount': 3200},
    {'type': 'sale', 'amount': 11200},
    {'type': 'expense', 'amount': 1800},
    {'type': 'expense', 'amount': 950}
]

calculate_business_metrics(transaction_data)