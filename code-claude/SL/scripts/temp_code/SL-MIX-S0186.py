def domain_filter(domain):
    # Check if domain meets security criteria
    suspicious_keywords = ['free', 'win', 'prize']
    domain_parts = domain.lower().split('.')
    
    # Check domain length (irrelevant to filtering)
    domain_length = len(domain)
    complexity_score = domain_length * 0.5
    
    # Filter out domains with suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in domain_parts[0]:
            return False
    
    # Calculate trust score (distraction)
    trust_score = 100
    for char in domain:
        if char.isdigit():
            trust_score -= 5
    
    # Check TLD (Top Level Domain)
    valid_tlds = ['com', 'org', 'edu', 'gov', 'net']
    if len(domain_parts) > 1 and domain_parts[-1] in valid_tlds:
        return True
    
    # Additional checks that don't affect result
    security_level = 'medium' if complexity_score > 10 else 'low'
    potential_risk = (100 - trust_score) / 100
    
    return False

# List of domains to check
domains = ['example.com', 'university.edu', 'free-stuff.net', 'government.gov', 
          'nonprofit.org', 'prize.co', 'win-big.com', 'research.net', 'info.xyz']

# Dictionary of domain categories (not used in filtering)
domain_categories = {
    'example.com': 'business',
    'university.edu': 'education',
    'government.gov': 'government',
    'nonprofit.org': 'nonprofit'
}

# Apply the filter
valid_domains = [domain for domain in domains if domain_filter(domain)]

# Count domains by TLD (distraction)
tld_counts = {}
for domain in domains:
    tld = domain.split('.')[-1]
    tld_counts[tld] = tld_counts.get(tld, 0) + 1

print(f"Result: {len(valid_domains)}")