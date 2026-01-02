from collections import defaultdict
import itertools

# Simulate financial transaction flows across departments
department_txns = [
    ('sales', [120, -30, 200, -150]),
    ('marketing', [-500, 300, -50, -80]),
    ('engineering', [-700, 200, 150, -40, 300]),
    ('hr', [-200, 50, -30, -90])
]

# Irrelevant helper: counts transaction frequency per department (not used in final result)
txn_frequency = {}
for dept, txns in department_txns:
    txn_frequency[dept] = len(txns)

# Compute net flow per department
net_per_dept = {}
for dept, txns in department_txns:
    net_per_dept[dept] = sum(txns)

# Aggregate total net flow across all departments
total_inflow = sum(max(0, x) for _, txns in department_txns for x in txns)
total_outflow = sum(abs(x) for _, txns in department_txns for x in txns if x < 0)
net_flow = sum(net_per_dept.values())

# Misleading intermediate: unused capacity ratio
capacity_ratio = total_inflow / (total_outflow + 1) if total_outflow else 0

# Simulate projected growth over time
years = 3
interest_rate = 0.045  # Annual compound rate

# Key computation point
compound_factor = (1 + interest_rate) ** years
threshold_balance = net_flow * compound_factor

# Dead code branch: never executed but adds cognitive load
if False:
    backup_system = defaultdict(int)
    for k, v in net_per_dept.items():
        backup_system[k] += v * 2

# Unused itertools example: generates combinations but doesn't affect result
useless_combinations = list(itertools.combinations(['low', 'medium', 'high'], 2))

# Final output
print(f"Result: {threshold_balance}")