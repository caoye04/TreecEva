# Email Priority Scoring System
# Calculate priority score based on email attributes

def calculate_priority(subject, sender_domain, word_count):
    # Convert subject to lowercase for processing
    subject_lower = subject.lower()
    
    # Initial importance values
    urgency_level = 3
    sender_importance = 5 if "company.com" in sender_domain else 2
    
    # Word count factor (more words generally means more important)
    length_factor = min(word_count // 50, 4)  # Cap at 4
    
    # Check for urgent keywords in subject
    urgent_keywords = ["urgent", "important", "asap", "deadline"]
    keyword_bonus = 0
    
    # Use conditional expression to check for keywords
    keyword_bonus = sum(2 for keyword in urgent_keywords if keyword in subject_lower)
    
    # Calculate base score
    base_score = urgency_level + sender_importance + length_factor + keyword_bonus
    
    # Return the normalized score (scale of 1-10)
    return min(base_score, 10)

# Sample email data: (subject, sender domain, word count)
email_data = [
    ("Project deadline tomorrow", "client.org", 120),
    ("URGENT: Meeting rescheduled", "company.com", 75),
    ("Weekly newsletter", "marketing.com", 350)
]

# Calculate scores for each email
scores = []
for i, (subject, domain, words) in enumerate(email_data):
    email_num = i + 1
    score = calculate_priority(subject, domain, words)
    scores.append(score)
    print(f"Email {email_num} score: {score}")

# Calculate overall priority score
priority_score = sum(scores)
print(f"Result: {priority_score}")
