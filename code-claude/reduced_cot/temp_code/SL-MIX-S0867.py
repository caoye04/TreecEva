from collections import Counter
import itertools

def analyze_network_traffic(log_entries):
    # Parse network log entries
    connection_data = []
    error_count = 0
    max_retries = 3
    
    # Process each log entry
    for entry in log_entries:
        parts = entry.split(':')
        if len(parts) < 2:
            error_count += 1
            continue
            
        ip_address = parts[0]
        status = parts[1]
        
        # Track connection attempts even for errors
        connection_data.append(ip_address)
        
        # Count retries for monitoring purposes
        if status == 'retry':
            retry_count = min(max_retries, error_count)
            error_count = (error_count + 1) % max_retries
    
    # Calculate metrics (some are for monitoring only)
    connection_counter = Counter(connection_data)
    unique_ips = len(connection_counter)
    
    # Filter out inactive connections (status = 'closed')
    active_ips = [ip for ip in connection_data if not ip.endswith('.0')]
    potential_threats = itertools.islice(active_ips, 0, 5)
    threat_score = sum(1 for _ in potential_threats)
    
    # Calculate active connections - this is our target value
    active_connections = len(connection_counter)
    
    # Calculate some additional metrics for the report
    connection_density = unique_ips / (len(connection_data) or 1)
    max_connections = max(connection_counter.values()) if connection_counter else 0
    
    print(f"Result: {active_connections}")
    return active_connections

# Sample network log data
log_entries = [
    "192.168.1.5:connected",
    "10.0.0.1:retry",
    "172.16.0.1:connected",
    "192.168.1.5:disconnected",
    "10.0.0.0:error",
    "172.16.0.2:connected",
    "192.168.1.6:connected",
    "10.0.0.1:connected"
]

# Analyze the network traffic
result = analyze_network_traffic(log_entries)