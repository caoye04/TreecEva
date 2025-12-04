def analyze_file_permissions(permissions):
    # Convert octal permissions to binary representation
    binary_repr = bin(int(permissions, 8))[2:].zfill(9)
    
    # Extract user, group, and others permissions
    user = binary_repr[:3]
    group = binary_repr[3:6]
    others = binary_repr[6:]
    
    # Calculate weighted scores based on permissions
    user_score = int(user, 2) * 100
    group_score = int(group, 2) * 10
    others_score = int(others, 2)
    
    return user_score + group_score + others_score

def filter_sensitive_files(files_data):
    high_risk = []
    medium_risk = []
    low_risk = []
    
    for file_info in files_data:
        if 'config' in file_info['name'] and file_info['score'] > 600:
            high_risk.append(file_info)
        elif file_info['extension'] in ['.env', '.key'] or file_info['score'] > 700:
            medium_risk.append(file_info)
        else:
            low_risk.append(file_info)
            
    return {'high': high_risk, 'medium': medium_risk, 'low': low_risk}

def calculate_priority():
    # Define file permissions in octal notation
    permission_map = {
        'user_config.json': '644',
        'system.env': '640',
        'backup.key': '600',
        'public_data.xml': '644',
        'admin_settings.conf': '600'
    }
    
    # Calculate permission scores
    file_data = []
    for filename, permission in permission_map.items():
        name, extension = filename.split('.') if '.' in filename else (filename, '')
        extension = f'.{extension}' if extension else ''
        
        # Calculate a score based on permissions
        perm_score = analyze_file_permissions(permission)
        
        # Store file information
        file_data.append({
            'name': name,
            'extension': extension,
            'permissions': permission,
            'score': perm_score
        })
    
    # This sorting is not used in final calculation
    sorted_files = sorted(file_data, key=lambda x: x['score'], reverse=True)
    
    # Filter files based on sensitivity
    risk_categories = filter_sensitive_files(file_data)
    
    # Calculate risk metrics
    security_metric = len(risk_categories['high']) * 5 + len(risk_categories['medium']) * 3
    
    # Distracting calculation that isn't used
    potential_risk = sum(f['score'] for f in risk_categories['high']) / 100
    
    # Calculate base priority using bitwise operations
    base_priority = (security_metric << 2) | (1 if len(risk_categories['high']) > 0 else 0)
    
    # More distracting calculations
    alternative_priority = sum(len(files) for files in risk_categories.values())
    weighted_alternative = alternative_priority * 2 - security_metric
    
    # Lambda for priority adjustment based on high-risk files
    priority_adjust = lambda x: x + 3 if len(risk_categories['high']) > 1 else x
    
    # Final calculation (the actual answer path)
    result = priority_adjust(base_priority)
    
    # Misleading calculation that isn't returned
    final_risk_score = (result * alternative_priority) // 2
    
    return result

# Execute the function and store the result
priority_level = calculate_priority()
print(f"Result: {priority_level}")