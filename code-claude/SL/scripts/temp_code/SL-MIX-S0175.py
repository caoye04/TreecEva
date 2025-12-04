def analyze_sentiment(text):
    # Sentiment analysis simulation
    positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful'}
    negative_words = {'bad', 'terrible', 'awful', 'horrible', 'poor'}
    
    words = text.lower().split()
    sentiment_score = sum(2 for word in words if word in positive_words) - \
                     sum(2 for word in words if word in negative_words)
    
    return max(-10, min(10, sentiment_score))

def calculate_network_load(servers):
    # Network load simulation
    total_load = 0
    for server, stats in servers.items():
        if stats['active']:
            total_load += stats['connections'] * 0.5
            if stats['cpu_usage'] > 80:
                total_load += 15
            elif stats['cpu_usage'] > 60:
                total_load += 10
    return total_load

def calculate_priority(message_data, system_config):
    # Distractor variables
    system_uptime = 1457.28
    total_memory = system_config.get('memory', 8192)
    backup_status = system_config.get('backup_complete', False)
    network_stability = 0.95
    
    # Critical path starts here
    urgency = message_data.get('urgency', 0)
    importance = message_data.get('importance', 0)
    
    # Distractor calculation
    potential_impact = urgency * importance * 0.5
    if potential_impact > 50:
        risk_factor = 2.5
    else:
        risk_factor = 1.2
    
    # This calculation is unused
    server_metrics = {
        'server1': {'active': True, 'connections': 120, 'cpu_usage': 85},
        'server2': {'active': True, 'connections': 90, 'cpu_usage': 65},
        'server3': {'active': False, 'connections': 0, 'cpu_usage': 5}
    }
    network_load = calculate_network_load(server_metrics)
    
    # More distractors
    message_length = len(message_data.get('content', ''))
    is_encrypted = message_data.get('encrypted', False)
    sentiment = analyze_sentiment(message_data.get('content', ''))
    
    # Distractor conditional path
    if is_encrypted and message_length > 1000:
        security_factor = 3
    elif is_encrypted:
        security_factor = 2
    else:
        security_factor = 1
    
    # Actual priority calculation - key statement
    base_priority = urgency * 0.7 + importance * 0.3
    category_weight = {'system': 2.5, 'user': 1.0, 'info': 0.5}
    message_category = message_data.get('category', 'info')
    
    # This is the actual calculation that matters
    priority_level = base_priority * category_weight.get(message_category, 1.0)
    
    # More distractors
    if message_data.get('from_admin', False):
        admin_override = priority_level * 1.5
    else:
        admin_override = priority_level
    
    # Misleading return value setup
    if system_config.get('maintenance_mode', False):
        return min(5, priority_level + 2)
    
    # The actual return value
    return priority_level

# Test data
message_data = {
    'urgency': 8,
    'importance': 7,
    'category': 'system',
    'content': 'Database connection failed with error code 5123. Backup systems activated.',
    'from_admin': True,
    'encrypted': True
}

system_config = {
    'memory': 16384,
    'backup_complete': True,
    'maintenance_mode': False,
    'debug_level': 3
}

# Calculate priority
priority_level = calculate_priority(message_data, system_config)
print(f"Result: {priority_level}")