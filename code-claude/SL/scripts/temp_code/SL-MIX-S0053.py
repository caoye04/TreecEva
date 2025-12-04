def check_spam_indicators(text):
    spam_words = ['free', 'discount', 'offer', 'limited']
    count = 0
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    for word in spam_words:
        if word in text_lower:
            count += 1
    
    # This calculation doesn't affect the result
    spam_factor = len(text) / 100 if len(text) > 0 else 0
    return count

def extract_domain(email_address):
    # Extract domain from email address
    if '@' in email_address:
        return email_address.split('@')[1]
    return ''

def calculate_email_priority(content, sender_domain):
    # Check content length and initialize variables
    content_length = len(content)
    priority_score = 50
    
    # Apply length modifier (irrelevant calculation)
    length_modifier = min(content_length // 20, 10)
    
    # Check for spam indicators
    spam_count = check_spam_indicators(content)
    
    # Domain trust factors - higher values for trusted domains
    trusted_domains = {
        'company.com': 10,
        'partner.org': 8,
        'client.net': 5
    }
    
    # Calculate domain trust bonus
    domain_bonus = trusted_domains.get(sender_domain, 0)
    
    # Check for urgency keywords
    urgency_words = ['urgent', 'immediate', 'asap', 'important']
    urgency_count = 0
    
    for word in urgency_words:
        if word in content.lower():
            urgency_count += 1
    
    # Calculate priority
    if spam_count >= 2:
        # Reduce priority for potential spam
        priority_score -= spam_count * 5
    
    # Add domain trust bonus
    priority_score += domain_bonus
    
    # Add urgency bonus (if any urgency words found)
    priority_score += urgency_count * 7
    
    # Apply caps
    return max(min(priority_score, 100), 0)

# Example email content and sender
email_content = "URGENT: Important meeting tomorrow with client. Please prepare the presentation ASAP."
sender_email = "manager@company.com"

# Process email address to get domain
sender_domain = extract_domain(sender_email)

# Calculate message length (irrelevant calculation)
msg_len = len(email_content)
word_count = len(email_content.split())
char_ratio = msg_len / (word_count if word_count > 0 else 1)

# Analyze email content capitalization (irrelevant)
caps_count = sum(1 for c in email_content if c.isupper())
caps_percentage = (caps_count / msg_len) * 100 if msg_len > 0 else 0

# This is just a distraction - not used in the result
temp_priority = 45 + (caps_percentage // 10)

# Calculate the final priority score
final_priority = calculate_email_priority(email_content, sender_domain)

# Print the result
print(f"Email priority score: {final_priority}")