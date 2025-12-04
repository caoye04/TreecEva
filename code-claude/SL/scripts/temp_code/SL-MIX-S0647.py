import itertools

def process_ticket_queue(tickets, priority_levels):
    # Calculate average severity for reporting
    avg_severity = sum(ticket['severity'] for ticket in tickets) / len(tickets)
    
    # Sort tickets by priority and timestamp
    sorted_tickets = sorted(tickets, key=lambda x: (x['priority'], x['timestamp']))
    
    # Extract only active tickets
    active_tickets = [t for t in sorted_tickets if t['status'] == 'active']
    
    # Process tickets in batches of priority levels
    priority_batches = {}
    for level in priority_levels:
        # Filter tickets by priority level
        level_tickets = [t for t in active_tickets if t['priority'] == level]
        
        # Track some metrics for reporting
        response_times = [t['timestamp'] % 100 for t in level_tickets]
        avg_response = sum(response_times) / len(response_times) if response_times else 0
        
        # Store batch information
        priority_batches[level] = {
            'count': len(level_tickets),
            'avg_response': avg_response,
            'severity_sum': sum(t['severity'] for t in level_tickets)
        }
    
    # Calculate priority score based on ticket metrics
    priority_score = 0
    for level, batch in priority_batches.items():
        # Higher priority levels contribute more to the score
        level_factor = priority_levels.index(level) + 1
        severity_impact = batch['severity_sum'] * 0.5
        count_impact = batch['count'] * 2
        
        # Calculate priority contribution from this level
        priority_score += (level_factor * (severity_impact + count_impact))
    
    # Apply some normalization factors for readability
    normalized_score = int(priority_score / len(priority_levels))
    
    # Generate report IDs for auditing (not used in final calculation)
    report_ids = ['REP-' + str(100 + i) for i in range(len(tickets))]
    
    # Calculate potential capacity based on ticket distribution
    capacity = sum(priority_batches[level]['count'] for level in priority_levels)
    capacity_factor = min(capacity / 10, 5) if capacity > 0 else 1
    
    # Final priority is the normalized score adjusted by capacity
    final_priority = normalized_score
    
    return final_priority

# Test data
tickets = [
    {'id': 'T1', 'priority': 'high', 'severity': 8, 'timestamp': 1623, 'status': 'active'},
    {'id': 'T2', 'priority': 'medium', 'severity': 5, 'timestamp': 1845, 'status': 'active'},
    {'id': 'T3', 'priority': 'low', 'severity': 3, 'timestamp': 1532, 'status': 'active'},
    {'id': 'T4', 'priority': 'high', 'severity': 7, 'timestamp': 1702, 'status': 'resolved'},
    {'id': 'T5', 'priority': 'medium', 'severity': 4, 'timestamp': 1920, 'status': 'active'},
    {'id': 'T6', 'priority': 'high', 'severity': 9, 'timestamp': 1550, 'status': 'active'}
]

priority_levels = ['high', 'medium', 'low']

# Process the ticket queue
final_priority = process_ticket_queue(tickets, priority_levels)
print(f"Result: {final_priority}")