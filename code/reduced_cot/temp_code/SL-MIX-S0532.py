import re
from functools import reduce

def calculate_threat_score(log_entries):
    # Define suspicious patterns
    patterns = {
        'sql_injection': r'(UNION|SELECT|INSERT).*',
        'xss': r'<script.*?>.*?</script>',
        'file_traversal': r'\.\./',
        'admin_access': r'/admin/'
    }
    
    # Initialize scores
    base_scores = {'sql_injection': 10, 'xss': 15, 'file_traversal': 8, 'admin_access': 5}
    
    # Calculate pattern matches
    matched_patterns = [
        pattern for entry in log_entries 
        for pattern, regex in patterns.items() 
        if re.search(regex, entry, re.IGNORECASE)
    ]
    
    # Apply scoring logic
    threat_contributions = {
        pattern: base_scores[pattern] + (2 if pattern == 'sql_injection' and any('DROP' in e for e in log_entries) else 0)
        for pattern in matched_patterns
    }
    
    # Compute final score with bonus logic
    total_score = sum(threat_contributions.values())
    bonus = 5 if total_score > 20 and 'admin_access' in matched_patterns else 0
    
    return total_score + bonus

# Log entries to analyze
logs = [
    "SELECT * FROM users WHERE id = 1",
    "<script>alert('XSS')</script>",
    "../../etc/passwd",
    "/admin/login"
]

# Calculate the threat score
final_threat_score = calculate_threat_score(logs)
print(f"Result: {final_threat_score}")