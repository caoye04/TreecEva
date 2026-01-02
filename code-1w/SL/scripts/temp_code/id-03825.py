def calculate_remaining(resources, log):
    capacity = resources.get('total', 0)
    used = 0
    for entry in log:
        operation = entry['op']
        amount = entry['amount']
        threshold = resources['threshold'] if 'threshold' in resources else 0
        # Conditional expression to handle overflow scenarios
        adjustment = amount * 0.9 if operation == 'write' and amount > threshold else amount
        used += adjustment if operation in ['write', 'modify'] else 0
    
    # Destructuring assignment for auxiliary settings
    (grace, bonus) = (resources['grace'], resources['bonus']) if 'grace' in resources else (0, 0)
    
    remaining = capacity - used + bonus
    final_capacity = max(remaining, grace)  # Ensure minimum graceful capacity
    return final_capacity

# Resource configuration with meaningful parameters
resources_config = {
    'total': 500,
    'threshold': 50,
    'bonus': 20,
    'grace': 10
}

# Log of operations simulating system activity
usage_records = [
    {'op': 'read', 'amount': 30},
    {'op': 'write', 'amount': 60},
    {'op': 'modify', 'amount': 40},
    {'op': 'write', 'amount': 70}
]

# Execute calculation
final_capacity = calculate_remaining(resources_config, usage_records)
print(f"Result: {final_capacity}")