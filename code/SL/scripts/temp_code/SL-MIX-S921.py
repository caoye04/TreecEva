from collections import defaultdict

def process_transaction_log():
    clearance_map = defaultdict(int)
    clearance_map['alpha'] = 3
    clearance_map['beta'] = 7
    clearance_map['gamma'] = 11
    
    transaction_flags = [True, False, True, True]
    modifier = 0
    
    # First logical chain
    if transaction_flags[0] and transaction_flags[1]:
        modifier += 5
    elif not transaction_flags[0] or transaction_flags[2]:
        modifier += 3
    else:
        modifier += 1
        
    # Second logical chain with short-circuit
    security_check = False
    if (clearance_map['alpha'] > 2 and 
        (transaction_flags[3] or clearance_map['beta'] < 5) and
        not security_check):
        modifier *= 2
    
    # Third logical chain
    access_level = 'gamma'
    final_clearance_level = 0
    
    match access_level:  # Python 3.10+ style match-case
        case 'alpha':
            final_clearance_level = modifier + clearance_map['alpha']
        case 'beta':
            final_clearance_level = modifier + clearance_map['beta']
        case 'gamma':
            final_clearance_level = modifier + clearance_map['gamma']
        case _:
            final_clearance_level = modifier
    
    # Final adjustment with logical operation
    if not (modifier == 0 and security_check):
        final_clearance_level += 1
    
    return final_clearance_level

final_clearance_level = process_transaction_log()
print(f"Result: {final_clearance_level}")