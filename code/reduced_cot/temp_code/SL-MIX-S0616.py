from collections import defaultdict

def account_processor(principal, withdrawals):
    # Distractor variables - misleading calculations
    compounding_rate = 1.08  # Irrelevant for this calculation
    service_fee = lambda x: x * 0.02  # Unused lambda
    
    # Actual processing logic
    total_withdrawn = sum(withdrawals.values())
    remaining = principal - total_withdrawn
    
    # Misleading intermediate operations
    projected_growth = remaining * compounding_rate  # Never used
    fee_calculation = service_fee(remaining)  # Never used
    
    # Dead code path - conditional that never executes
    if remaining < -10000:
        penalty = remaining * 0.1  # This branch never runs
        remaining -= penalty
    
    # Final adjustment with misleading name
    adjusted_balance = remaining * 0.99  # Actually used
    
    return int(adjusted_balance)

# Main execution with distractors
initial_deposit = 5000
monthly_cashflow = [1200, -300, 450, -200]  # Misleading list - not used

# Complex dictionary with irrelevant entries
monthly_withdrawals = defaultdict(int)
monthly_withdrawals['january'] = 850
monthly_withdrawals['february'] = 320
monthly_withdrawals['march'] = 610
monthly_withdrawals['april'] = 280  # This key is never accessed

# Irrelevant calculations
quarterly_sum = sum([x for x in monthly_cashflow if x > 0])  # Never used
annual_projection = initial_deposit * 1.12  # Completely misleading

# Critical execution point
final_balance = account_processor(initial_deposit, monthly_withdrawals)

# Print the target result
print(f"Result: {final_balance}")