def process_efficiency(ops, down):
    base_throughput = 100
    adjustment_factor = len(ops) * 0.9
    total_ops = sum([op.count('success') for op in ops])
    if total_ops > 5:
        adjustment_factor += 2.5
    operational_hours = 8
    effective_output = (base_throughput * adjustment_factor) / (operational_hours + down)
    efficiency_score = round(effective_output, 3)
    return efficiency_score

# Simulated daily operations log
operations = [
    'success success fail',
    'success success success',
    'fail success',
    'success fail success',
    'success success',
    'success'
]
downtime = 1.5

# Calculation entry point
efficiency_score = process_efficiency(operations, downtime)
print(f"Result: {efficiency_score}")