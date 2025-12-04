def process_permissions(permissions_list):
    # Process user permission strings into numerical values
    # Higher values indicate more sensitive permissions
    processed = {}
    for perm in permissions_list:
        if 'admin' in perm:
            processed[perm] = 100
        elif 'write' in perm:
            processed[perm] = 50
        elif 'read' in perm:
            processed[perm] = 10
        else:
            processed[perm] = 1
    return processed

def analyze_threat_level(user_data):
    # Completely unrelated function for threat analysis
    threat_score = 0
    suspicious_patterns = ['backdoor', 'exploit', 'overflow']
    for pattern in suspicious_patterns:
        if pattern in user_data.get('recent_activities', ''):
            threat_score += 25
    return threat_score

def calculate_hash(input_str):
    # Simple hash function - not used in final calculation
    hash_val = 0
    for char in input_str:
        hash_val = (hash_val * 31 + ord(char)) % 10000
    return hash_val

def calculate_security_level(user_permissions):
    # Calculate security clearance based on permissions
    processed_perms = process_permissions(user_permissions)
    
    # Extract only permission values
    perm_values = list(processed_perms.values())
    
    # Misleading operations that aren't used
    perm_xor = 0
    for val in perm_values:
        perm_xor ^= val
    
    # More misleading calculations
    hash_total = sum([calculate_hash(perm) for perm in user_permissions])
    potential_risk_factor = len(user_permissions) * 5
    
    # The actual security level calculation
    base_level = sum(perm_values)
    
    # Apply modifiers based on specific permission combinations
    has_admin = any('admin' in p for p in user_permissions)
    has_write = any('write' in p for p in user_permissions)
    
    # This lambda function is a distraction
    risk_calculator = lambda x, y: (x * y) // 10 if x > y else (x + y) // 2
    
    # More distractions
    special_conditions = {
        'network': 15,
        'database': 25,
        'system': 35
    }
    
    # Misleading slicing operations
    if len(perm_values) > 2:
        subset_analysis = perm_values[1:3]
        subset_product = subset_analysis[0] * subset_analysis[-1]
    else:
        subset_product = 0
    
    # This is where the actual calculation happens
    modifier = 0
    if has_admin and has_write:
        modifier = 30
    elif has_admin:
        modifier = 20
    elif has_write:
        modifier = 10
    
    # Another distraction
    for perm in user_permissions:
        for domain, value in special_conditions.items():
            if domain in perm:
                # This looks important but isn't used in final result
                domain_factor = value
                break
        else:
            domain_factor = 0
    
    # The actual calculation that matters
    security_level = (base_level + modifier) // 10
    
    return security_level

# Test data
user_data = {
    'id': 'usr_12345',
    'name': 'John Developer',
    'recent_activities': 'code_review, merge_request, database_query',
    'login_count': 27
}

# These permissions will be used for calculation
user_permissions = ['read_logs', 'write_data', 'admin_dashboard', 'read_metrics']

# Distraction variables
threat_level = analyze_threat_level(user_data)
user_hash = calculate_hash(user_data['name'])
security_token = f"{user_hash:04d}-{threat_level:02d}"

# This is the statement in question
actual_security_level = calculate_security_level(user_permissions)

# More distractions after the key calculation
adjusted_threat = threat_level - (actual_security_level // 2)
final_risk_score = threat_level * 2 if adjusted_threat > 10 else threat_level

print(f"User: {user_data['name']}")
print(f"Security Token: {security_token}")
print(f"Threat Level: {threat_level}")
print(f"Result: {actual_security_level}")