import math

def build_dependency_tree(loan_ids):
    if len(loan_ids) <= 1:
        return loan_ids[0] if loan_ids else None
    mid = len(loan_ids) // 2
    node = {
        'id': f"node_{loan_ids[mid]}",
        'left': build_dependency_tree(loan_ids[:mid]),
        'right': build_dependency_tree(loan_ids[mid+1:])
    }
    return node

def calculate_risk_at_node(node, risk_map):
    if not node or not isinstance(node, dict):
        return risk_map.get(node, 0.0)
    left_risk = calculate_risk_at_node(node['left'], risk_map)
    right_risk = calculate_risk_at_node(node['right'], risk_map)
    base_risk = risk_map.get(node['id'], 0.0)
    combined = (left_risk + right_risk) * (1.0 + base_risk)
    return round(combined, 4)

portfolio_loans = [1001, 1002, 1003, 1004, 1005]
dependency_tree = build_dependency_tree(portfolio_loans)
risk_factors = {
    'node_1003': 0.05,
    'node_1002': 0.02,
    'node_1004': 0.03,
    1001: 0.01,
    1005: 0.04
}

# Risk amplification through interconnected defaults
amplification_factors = {loan_id: 1.0 + (loan_id % 10) * 0.01 for loan_id in portfolio_loans}
for key in list(risk_factors.keys()):
    if key in amplification_factors:
        risk_factors[key] *= amplification_factors[key]

systemic_risk_score = calculate_risk_at_node(dependency_tree, risk_factors)
print(f"Result: {systemic_risk_score}")