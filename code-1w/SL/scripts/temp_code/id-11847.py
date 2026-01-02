from collections import Counter

def calculate_final_score(log_entries):
    event_counter = Counter(log_entries)
    
    # Extract counts for specific events
    login_count = event_counter.get('LOGIN', 0)
    logout_count = event_counter.get('LOGOUT', 0)
    transfer_count = event_counter.get('TRANSFER', 0)
    
    # Compute weighted score using modular arithmetic
    base_score = (login_count * 2 + logout_count * 1) % 100
    bonus = transfer_count // 3 if transfer_count >= 3 else 0
    adjustment = (lambda x: x * (x + 1) // 2)(bonus)  # Triangular number bonus
    
    final_score = base_score + adjustment
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_debug = login_count - logout_count  # Not used further
    
    return final_score

# Simulated user activity log
data = ['LOGIN', 'LOGIN', 'TRANSFER', 'TRANSFER', 'TRANSFER', 'LOGOUT', 'TRANSFER']
final_score = calculate_final_score(data)
print(f"Result: {final_score}")