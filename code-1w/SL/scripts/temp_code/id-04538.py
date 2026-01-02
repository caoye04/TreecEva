def analyze_financial_data(data):
    # Irrelevant variables (distractors)
    dummy_counter = 0
    temp_result = []
    metadata_log = {}
    backup_flag = False
    
    # Relevant initialization
    base_profit = 0
    tax_rate = 0.15
    overhead_costs = {}
    growth_factor = 1.07
    adjustment_factor = 0.93
    revenue_balance = 0
    
    # Simulate processing of financial quarters
    for quarter, records in data.items():
        quarterly_total = 0
        deduction_pool = 0
        
        for item in records:
            if 'type' not in item:
                continue
            if item['type'] == 'income':
                base_profit += item['amount']
                quarterly_total += item['amount']
            elif item['type'] == 'expense':
                deduction_pool += item['amount']
                if item['amount'] > 1000:
                    metadata_log[quarter] = True  # red herring
            
        # Dead code path (never executed due to structure)
        if len(records) > 100:
            backup_flag = True
            for i in range(len(temp_result)):
                dummy_counter += 1

    # Bit manipulation decoy (unrelated to final result)
    magic_key = 0b1101
    for i in range(5):
        magic_key ^= (i + 0b1010)
        magic_key &= 0b1111
    
    # Destructuring distraction
    config_settings = ('USD', 2023, 'Q4')
    currency, year, _ = config_settings
    
    # Real computation begins
    gross_income = base_profit
    net_expenses = sum(data[q][0]['amount'] for q in data if data[q])  # uses only first expense
    taxable_income = gross_income - net_expenses * 0.6
    pre_tax_profit = taxable_income - (overhead_costs.get('misc', 120) * 2)
    
    # Conditional branch with early exit red herring
    if pre_tax_profit < 0:
        final_profit = 0
        return None  # unused return
    else:
        final_profit = pre_tax_profit * (1 - tax_rate)
    
    # Key statement: answer depends on this
    revenue_balance = final_profit * adjustment_factor
    
    # More irrelevant operations
    report_summary = {
        'version': '2.1',
        'entries_processed': dummy_counter,
        'flags': [backup_flag],
        'checksum': magic_key ^ 17
    }
    
    # Unused recursive function (decoy)
    def validate_hierarchy(node_id, depth=0):
        if depth > 3:
            return False
        return validate_hierarchy(node_id + 1, depth + 1)
    
    # Final output
    print(f"Result: {revenue_balance}")
    return revenue_balance

# Input data
financial_data = {
    'Q1': [
        {'type': 'income', 'amount': 12500},
        {'type': 'expense', 'amount': 3200}
    ],
    'Q2': [
        {'type': 'income', 'amount': 14200},
        {'type': 'expense', 'amount': 4100}
    ],
    'Q3': [
        {'type': 'income', 'amount': 13800},
        {'type': 'expense', 'amount': 3800}
    ],
    'Q4': [
        {'type': 'income', 'amount': 15500},
        {'type': 'expense', 'amount': 4400}
    ]
}

# Execute
analyze_financial_data(financial_data)