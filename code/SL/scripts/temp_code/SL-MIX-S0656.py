import math

class TransactionTracker:
    def __init__(self):
        self.high_value_logs = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def log_if_significant(self, amount):
        if amount > 1000:
            self.high_value_logs.append(amount)

def audit_call(func):
    calls = []
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calls.append((args, result))
        return result
    wrapper.calls = calls
    return wrapper

@audit_call
def calculate_compound(principal, rate, time):
    return principal * (math.exp(rate * time))

# Initial financial data
portfolio = {
    'account_A': 1500,
    'account_B': 800,
    'account_C': 2000
}

rate_schedule = { acc: 0.05 if acc == 'account_A' else 0.03 for acc in portfolio }
bonus_rate = 0.02 if any(v > 1000 for v in portfolio.values()) else 0

final_yield = 0
with TransactionTracker() as tracker:
    for account, initial_amount in portfolio.items():
        current_rate = rate_schedule[account]
        if initial_amount > 1000:
            adjusted_rate = current_rate + bonus_rate
        else:
            adjusted_rate = current_rate
        
        compounded = calculate_compound(initial_amount, adjusted_rate, 2)
        tracker.log_if_significant(compounded)
        final_yield += compounded

final_yield = round(final_yield)
print(f"Result: {final_yield}")