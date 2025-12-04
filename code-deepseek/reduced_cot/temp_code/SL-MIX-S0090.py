from collections import Counter

def compute_final_balance(principal, contributions, interest_ops):
    # Distractor: unused investment calculations
    investment_pool = principal * 3
    speculative_gains = investment_pool // 2
    
    # Actual interest calculation
    monthly_rate = 0.008
    balance = principal
    
    # Misleading intermediate result
    temp_adjustment = balance * 0.1 if balance > 5000 else balance * 0.05
    
    for month in range(interest_ops):
        # Main compounding logic
        interest = balance * monthly_rate
        balance += interest
        balance += contributions
        
        # Distractor: unused fee calculation
        account_fee = balance * 0.002 if month % 3 == 0 else 0
        
        # Misleading counter update
        transaction_count = month + contributions
    
    # Final adjustment with conditional expression
    final_adjustment = balance * 0.02 if balance > 10000 else balance * 0.01
    balance -= final_adjustment
    
    # Dead code path
    if balance < principal:
        emergency_fund = principal * 0.1
        balance += emergency_fund
    
    return round(balance, 2)

# Initial setup
initial_deposit = 7500
monthly_contributions = 300
interest_calculations = 12

# Distractor variables
investment_target = 15000
risk_factor = 0.15
portfolio_diversity = 5

# Key execution
final_balance = compute_final_balance(initial_deposit, monthly_contributions, interest_calculations)

# Print result
print(f"Result: {final_balance}")