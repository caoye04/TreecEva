def calculate_net_flow(inflows, outflows):
    base_multiplier = 1.0
    adjustment_factor = 0.95
    temp_buffer = []
    total_in = 0
    total_out = 0
    flow_log = {}

    for key in sorted(inflows.keys()):
        if key.startswith('rev'):
            total_in += inflows[key]
            temp_buffer.append(inflows[key] * 0.01)

    for key in sorted(outflows.keys()):
        category = key.split('_')[0]
        amount = outflows[key]
        if category in ['tax', 'opex', 'capex']:
            total_out += amount
            if category not in flow_log:
                flow_log[category] = 0
            flow_log[category] += amount

    # Irrelevant transformation (distractor)
    adjusted_buffer = [round(x * adjustment_factor, 2) for x in temp_buffer]
    avg_buffer = sum(adjusted_buffer) / len(adjusted_buffer) if adjusted_buffer else 0

    # Dummy recursion to add complexity (not affecting final result)
    def recursive_discount(n, rate=0.99):
        if n <= 1:
            return n
        return rate * recursive_discount(n - 1)

    dummy_impact = recursive_discount(5)

    # Core calculation (affected only by total_in and total_out)
    gross_flow = total_in - total_out
    net_flow = gross_flow * base_multiplier

    # Additional irrelevant checks
    if net_flow > 1000:
        surge_tax = net_flow * 0.02
    else:
        surge_tax = 0

    return int(net_flow)

# Main execution
contributions = {'rev_q1': 1200, 'rev_q2': 1400, 'rev_q3': 1600, 'misc_99': 500}
deductions = {'opex_rent': 300, 'opex_sal': 700, 'tax_fed': 400, 'capex_equip': 500, 'irrel_data': 0}

net_flow = 0
intermediate_score = sum(contributions.values()) // len(contributions)
buffer_offset = len(deductions['opex_sal']) if 'opex_sal' in deductions else 0  # meaningless

net_flow = calculate_net_flow(contributions, deductions)
print(f"Result: {net_flow}")