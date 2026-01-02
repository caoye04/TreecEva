def analyze_feedback(reviews):
    # Irrelevant processing of text reviews
    words = []
    for r in reviews:
        words.extend(r.lower().split())
    word_count = len(words)
    unique_words = len(set(words))
    avg_length = sum(len(w) for w in words) / word_count if word_count else 0
    
    # Distractor: sentiment analysis that isn't used
    positive_terms = ['good', 'great', 'excellent', 'well']
    negative_terms = ['bad', 'poor', 'terrible', 'awful']
    pos_score = sum(1 for w in words if w in positive_terms)
    neg_score = sum(1 for w in words if w in negative_terms)
    sentiment_ratio = (pos_score + 1) / (neg_score + 1)

    # Red herring: unused transformation
    processed = [w[::-1] for w in words if len(w) > 3][:10]
    return unique_words  # Only this matters, rest is distraction


def compute_efficiency(tasks, errors):
    base_rate = len(tasks) * 2.5
    penalty = sum(errors) * 10
    bonus = 0
    
    if len(tasks) > 5:
        bonus += 20
    if sum(errors) == 0:
        bonus += 30
    
    # Complex but irrelevant branching
    status_log = []
    for i, e in enumerate(errors):
        if e > 2:
            status_log.append(f'Task{i}: CRITICAL')
        elif e == 1:
            status_log.append(f'Task{i}: WARNING')
        else:
            status_log.append(f'Task{i}: OK')
    
    # Dead code path
    final_status = None
    if False and len(status_log) > 10:
        final_status = 'AUDIT_REQUIRED'
    else:
        final_status = 'STABLE'
    
    return base_rate - penalty + bonus


def validate_compliance(entries):
    # Bit manipulation red herring
    flags = 0
    for e in entries:
        if 'urgent' in e:
            flags |= 1 << 3
        if 'reviewed' in e:
            flags ^= 1 << 1
    
    # Unused checksum
    checksum = 0
    for e in entries:
        checksum += sum(ord(c) for c in e) % 7
    
    # Actual logic
    valid_entries = [e for e in entries if 'valid' in e and 'expired' not in e]
    return len(valid_entries) * 5


def calculate_risk_factor(exposure, history):
    # Recursive distractor
    def fib(n):
        return n if n <= 1 else fib(n-1) + fib(n-2)
    
    risk = exposure * 0.5
    if len(history) > 3:
        risk *= 1.2
    
    # Useless recursive call with bounded input
    dummy = fib(6)  # 8, but irrelevant
    
    return int(risk)


def process_performance(metrics, bonuses):
    score = 0
    
    # Key data transformations
    if 'efficiency' in metrics:
        score += metrics['efficiency']
    if 'compliance' in metrics:
        score += metrics['compliance']
    if 'feedback_quality' in metrics:
        score += metrics['feedback_quality'] * 2
    
    # Conditional bonus application
    total_bonus = 0
    for b in bonuses:
        if b['type'] == 'performance' and b['status'] == 'approved':
            total_bonus += b['amount']
    
    # Critical adjustment: only even-numbered bonuses count
    filtered_bonus = sum(b['amount'] for b in bonuses if b['id'] % 2 == 0)
    score += filtered_bonus
    
    # Final non-linear scaling
    if score > 100:
        score = 90 + (score - 100) * 0.5  # Diminishing returns
    
    return int(score)

# Main execution with multiple distractions
if __name__ == '__main__':
    # Real input data
    user_reviews = [
        'Great performance overall well done',
        'Excellent work on the tasks good effort',
        'Well executed all areas excellent'
    ]
    
    task_list = ['t1','t2','t3','t4','t5','t6']
    error_log = [0, 1, 0, 0, 2, 0]
    
    compliance_entries = [
        'entry0 valid urgent',
        'entry1 valid reviewed',
        'entry2 expired',
        'entry3 valid',
        'entry4 valid reviewed urgent'
    ]
    
    exposure_level = 80
    history_records = ['h1','h2','h3','h4']
    
    # Irrelevant string processing
    metadata_tags = ['PERFv2', 'URGENT', 'Q4', 'FINAL']
    encoded = ''.join(tag[0] for tag in metadata_tags if len(tag) > 3).lower()
    key_hash = sum(ord(c) for c in encoded) % 100
    
    # Actual metric computation
    feedback_metric = analyze_feedback(user_reviews)
    efficiency_metric = compute_efficiency(task_list, error_log)
    compliance_metric = validate_compliance(compliance_entries)
    risk_metric = calculate_risk_factor(exposure_level, history_records)
    
    # Build metrics dictionary (only some fields are used)
    performance_metrics = {
        'efficiency': efficiency_metric,
        'compliance': compliance_metric,
        'feedback_quality': feedback_metric,
        'risk': risk_metric,  # unused field
        'version': '2.1'     # unused
    }
    
    # Bonus list with mixed statuses and types
    bonus_pool = [
        {'id': 1, 'type': 'performance', 'status': 'approved', 'amount': 15},
        {'id': 2, 'type': 'retention',   'status': 'approved', 'amount': 10},
        {'id': 3, 'type': 'performance', 'status': 'pending',  'amount': 20},
        {'id': 4, 'type': 'performance', 'status': 'approved', 'amount': 25}
    ]
    
    # Dead variable assignment
    audit_trail = []
    for item in bonus_pool:
        audit_trail.append(f"{item['id']}:{item['status']}")
    
    # Key statement
    final_score = process_performance(performance_metrics, bonus_pool)
    
    # Output result
    print(f"Result: {final_score}")