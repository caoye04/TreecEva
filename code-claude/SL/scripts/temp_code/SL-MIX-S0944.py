# Email Priority Scoring System
# This system calculates a priority score for emails based on various factors

# Sender domains and their base importance
domain_importance = {
    'work.com': 5,
    'client.org': 4,
    'newsletter.com': 1,
    'social.net': 2,
    'personal.edu': 3
}

# Email metadata
emails = [
    {'sender': 'boss@work.com', 'subject': 'Urgent Report', 'read': False, 'time_received': 9},
    {'sender': 'friend@personal.edu', 'subject': 'Weekend Plans', 'read': True, 'time_received': 2},
    {'sender': 'updates@newsletter.com', 'subject': 'Daily News', 'read': True, 'time_received': 1},
    {'sender': 'contact@client.org', 'subject': 'Project Discussion', 'read': False, 'time_received': 7}
]

# Words that might indicate importance
important_keywords = ['urgent', 'important', 'critical', 'deadline']
informal_keywords = ['hello', 'hey', 'chat', 'plans']

# Process emails to calculate scores
scores = []
total_emails = len(emails)
filtered_count = 0

for i, email in enumerate(emails):
    # Extract domain from sender email
    domain = email['sender'].split('@')[1]
    
    # Base score from domain importance
    base_score = domain_importance.get(domain, 0)
    
    # Adjust score if email is unread
    unread_modifier = 2 if not email['read'] else 0
    
    # Check for important keywords in subject
    keyword_score = 0
    subject_lower = email['subject'].lower()
    
    # Process keywords
    for keyword in important_keywords:
        if keyword in subject_lower:
            keyword_score += 3
    
    # This loop doesn't affect the final priority score
    for keyword in informal_keywords:
        if keyword in subject_lower:
            filtered_count += 1
    
    # Time factor - more recent emails get higher scores
    time_factor = min(email['time_received'] / 2, 5)
    
    # Calculate final score for this email
    email_score = base_score + unread_modifier + keyword_score + time_factor
    
    # Track some statistics that won't be used in final calculation
    avg_score_so_far = sum(scores) / (i + 1) if scores else 0
    relative_importance = email_score / (avg_score_so_far + 0.01)
    
    scores.append(email_score)

# These operations don't affect the final priority score
max_possible = max(domain_importance.values()) * 2 * total_emails
percentage = (sum(scores) / max_possible) * 100 if max_possible > 0 else 0

# Calculate the priority score
priority_score = sum(scores)

# Some additional processing that doesn't change the answer
unread_emails = [email for email in emails if not email['read']]
urgent_count = len([email for email in emails if 'urgent' in email['subject'].lower()])

# Final normalization - doesn't affect our target variable
normalized_score = round(priority_score / total_emails, 2) if total_emails > 0 else 0

print(f"Result: {priority_score}")