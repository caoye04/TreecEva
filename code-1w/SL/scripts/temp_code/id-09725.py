from collections import defaultdict

# Simulate employee review data with mixed feedback signals
def generate_feedback():
    raw_scores = [4.2, 3.8, 4.5, 4.0, 3.9]
    comments = ['excellent', 'good', 'excellent', 'satisfactory', 'good']
    categories = ['communication', 'teamwork', 'leadership', 'punctuality', 'teamwork']
    
    feedback_list = []
    for i in range(len(raw_scores)):
        feedback_list.append({
            'score': raw_scores[i],
            'comment': comments[i],
            'domain': categories[i]
        })
    
    return feedback_list

# Analyze domain-specific trends
def analyze_domain_trends(feedback):
    domain_count = defaultdict(int)
    domain_total = defaultdict(float)
    
    for entry in feedback:
        d = entry['domain']
        s = entry['score']
        domain_count[d] += 1
        domain_total[d] += s
    
    avg_by_domain = {k: domain_total[k] / domain_count[k] for k in domain_count}
    
    # Distractor: unused computation
    max_domain_score = max(avg_by_domain.values()) if avg_by_domain else 0
    sorted_domains = sorted(avg_by_domain.keys())
    
    return avg_by_domain

# Count qualitative labels (irrelevant to final score but plausible)
def count_comments(feedback):
    comment_freq = {}
    for f in feedback:
        c = f['comment']
        comment_freq[c] = comment_freq.get(c, 0) + 1
    
    # Dead code path - never used later
    if 'outstanding' in comment_freq:
        comment_freq['excellent'] += comment_freq['outstanding']
    
    return comment_freq

# Core evaluation logic
def evaluate_performance(feedback_map):
    base_score = 0.0
    multiplier = 1.0
    
    # Extract numeric contributions
    for entry in feedback_map:
        score = entry['score']
        comment = entry['comment']
        
        if score >= 4.0:
            base_score += 2
        elif score >= 3.5:
            base_score += 1
        else:
            base_score -= 1
    
    # Apply artificial penalty for inconsistency (logic red herring)
    domains = [f['domain'] for f in feedback_map]
    unique_domains = set(domains)
    if len(unique_domains) > 3:
        multiplier *= 0.9
    
    # Real adjustment: bonus for high average
    total = sum(f['score'] for f in feedback_map)
    avg = total / len(feedback_map)
    if avg > 4.0:
        base_score += 3
    
    result = base_score * multiplier
    
    # Intermediate transformation (distractor)
    normalized = round(result * 1.1, 2)
    scaled = int(normalized)
    
    return scaled

# Main execution flow
feedback_data = generate_feedback()
domain_analysis = analyze_domain_trends(feedback_data)
comment_counts = count_comments(feedback_data)

# Key statement
final_score = evaluate_performance(feedback_data)

print(f"Result: {final_score}")