def calculate_ticket_urgency(ticket):
    # Higher values indicate more urgent tickets
    severity = ticket.get('severity', 1)
    days_open = ticket.get('days_open', 0)
    customer_tier = ticket.get('customer_tier', 3)
    
    # Misleading calculation that isn't used
    raw_score = severity * 10 + days_open * 2 + (5 - customer_tier) * 15
    
    # The actual calculation used
    return severity * 5 + max(0, days_open - 1) * 3 + (5 - customer_tier) * 7

def sort_by_category(tickets):
    # Distraction function that isn't used in final calculation
    categories = {}
    for ticket in tickets:
        cat = ticket.get('category', 'general')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(ticket)
    
    sorted_tickets = []
    for cat in sorted(categories.keys()):
        sorted_tickets.extend(sorted(categories[cat], key=lambda x: x.get('severity', 0), reverse=True))
    
    return sorted_tickets

def filter_relevant_tickets(tickets, threshold=20):
    # This function actually matters for the final result
    urgent = []
    standard = []
    
    for i, ticket in enumerate(tickets):
        urgency = calculate_ticket_urgency(ticket)
        
        # Distraction calculation
        weighted_priority = urgency * (i % 3 + 1)
        
        if urgency > threshold:
            urgent.append(ticket)
        else:
            standard.append(ticket)
    
    # Return only the urgent tickets that meet threshold
    return urgent

def calculate_final_priority(tickets):
    if not tickets:
        return 0
    
    # Calculate the base score
    base_score = sum(calculate_ticket_urgency(t) for t in tickets)
    
    # Distraction variables and calculations
    potential_multipliers = [0.8, 1.0, 1.2, 1.5]
    category_weights = {'bug': 1.2, 'feature': 0.9, 'security': 1.5, 'general': 1.0}
    
    # Extract categories and create a misleading dictionary
    categories = [t.get('category', 'general') for t in tickets]
    category_counts = {cat: categories.count(cat) for cat in set(categories)}
    
    # This looks important but isn't used in final calculation
    adjusted_scores = {}
    for i, ticket in enumerate(tickets):
        cat = ticket.get('category', 'general')
        weight = category_weights.get(cat, 1.0)
        adjusted_scores[i] = calculate_ticket_urgency(ticket) * weight
    
    # The actual calculation that matters
    priority_factor = 1.0
    if len(tickets) >= 5:
        priority_factor = 1.25
    elif len(tickets) >= 3:
        priority_factor = 1.1
    
    # More distraction
    for cat, count in category_counts.items():
        if cat == 'security' and count >= 2:
            # This branch is actually dead code - none of our tickets are 'security'
            priority_factor = 1.5
            break
    
    # Calculate and return the final score
    return int(base_score * priority_factor)

# Initialize ticket data
all_tickets = [
    {'id': 101, 'severity': 3, 'days_open': 5, 'customer_tier': 1, 'category': 'bug'},
    {'id': 102, 'severity': 2, 'days_open': 8, 'customer_tier': 2, 'category': 'feature'},
    {'id': 103, 'severity': 4, 'days_open': 2, 'customer_tier': 1, 'category': 'bug'},
    {'id': 104, 'severity': 1, 'days_open': 12, 'customer_tier': 3, 'category': 'general'},
    {'id': 105, 'severity': 3, 'days_open': 3, 'customer_tier': 2, 'category': 'bug'}
]

# Distraction - this sorted list isn't used for the final calculation
sorted_tickets = sort_by_category(all_tickets)

# This is what's actually used
filtered_tickets = filter_relevant_tickets(all_tickets, threshold=25)

# Calculate the final priority score
priority_score = calculate_final_priority(filtered_tickets)

print(f"Result: {priority_score}")