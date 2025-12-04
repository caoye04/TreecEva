from collections import Counter, defaultdict

def analyze_system_logs(logs):
    # Parse system logs for errors
    error_counts = Counter()
    for entry in logs:
        if 'ERROR' in entry:
            error_counts[entry.split(':')[0]] += 1
    return error_counts

def extract_metadata(ticket):
    # Extract ticket metadata
    metadata = {}
    fields = ticket.split('|')
    if len(fields) >= 3:
        metadata['id'] = fields[0]
        metadata['severity'] = int(fields[1])
        metadata['component'] = fields[2]
    return metadata

def calculate_priority(ticket_data):
    # Calculate ticket priority based on various factors
    base_score = 0
    severity_map = {1: 5, 2: 15, 3: 30, 4: 60, 5: 100}
    component_weights = defaultdict(lambda: 1.0, {
        'network': 1.2,
        'database': 1.5,
        'security': 2.0,
        'ui': 0.8
    })
    
    # Process fake log data (distractor)
    fake_logs = ['NETWORK:ERROR:Connection timeout', 'DATABASE:ERROR:Query failed']
    log_analysis = analyze_system_logs(fake_logs)
    
    # Calculate factors that don't matter (distractor)
    historical_factor = sum([ord(c) % 5 for c in ticket_data['id']]) / 10
    weather_impact = lambda temp: 0.05 * (temp - 20) if temp > 25 else 0
    weather_coefficient = weather_impact(32)
    
    # Extract actual components for calculation
    severity = ticket_data['severity']
    component = ticket_data['component']
    
    # Calculate priority using a complex but misleading formula first (distractor)
    misleading_priority = severity_map.get(severity, 0) * 1.5
    misleading_priority *= (1 + historical_factor)
    
    # Another misleading calculation (distractor)
    if component in ('network', 'security'):
        misleading_priority += 25
    elif component == 'database':
        misleading_priority *= 1.2
    
    # The actual priority calculation
    real_severity = severity_map.get(severity, 0)
    component_factor = component_weights[component]
    base_score = real_severity * component_factor
    
    # Adjustment based on bit operations (seems important but is a distractor)
    bit_flags = 0b101010
    if severity > 3:
        bit_flags = bit_flags | (1 << 3)
    bit_adjustment = bin(bit_flags).count('1') - 2
    
    # Final calculation with tuples and sets (the actual logic)
    impact_factors = (1.0, 0.8, 1.2, 0.9, 1.5)
    selected_impacts = {0, 2, 4} if severity > 3 else {1, 3}
    final_factor = sum(impact_factors[i] for i in selected_impacts) / len(selected_impacts)
    
    priority_value = round(base_score * final_factor)
    return priority_value

# Main execution
ticket = "TCKT-1234|4|database|urgent|John Doe"
ticket_data = extract_metadata(ticket)

# Some misleading operations on the data
processed_data = {k: v for k, v in ticket_data.items()}
processed_data['timestamp'] = 1635784800
processed_data['status'] = 'open'

# Calculate priority score using the actual ticket data
final_priority = calculate_priority(ticket_data)

# More distractor calculations that seem to modify the priority
temporal_adjustment = lambda h: h % 12 / 24
hour_factor = temporal_adjustment(14)
adjusted_priority = final_priority * (1 + hour_factor)
scaled_priority = int(adjusted_priority * 0.9)

print(f"Result: {final_priority}")