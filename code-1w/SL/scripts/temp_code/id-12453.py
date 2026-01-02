from collections import defaultdict, Counter
import math

# Simulated employee assessment system with multiple evaluation dimensions
def analyze_feedback(feedback_str):
    words = feedback_str.lower().split()
    word_count = Counter(words)
    positive = ['excellent', 'good', 'efficient', 'reliable', 'proactive']
    negative = ['poor', 'slow', 'error', 'complaint', 'failure']
    
    score = 0
    for word in positive:
        score += word_count.get(word, 0) * 2
    for word in negative:
        score -= word_count.get(word, 0) * 3
    
    # Irrelevant transformation (distractor)
    temp_analysis = ''.join([w[::-1] for w in words if len(w) > 4])
    temp_analysis = temp_analysis.upper().replace('A', 'X')
    return score

# Legacy function - never called (dead code path)
def legacy_evaluation(data):
    total = 0
    for k, v in data.items():
        if len(k) % 2 == 0:
            total += v * 0.75
    return int(total // len(data))

# Decoy function that looks important but isn't used in main logic
def calculate_tenure_bonus(years, rating):
    if years < 1:
        return 0
    bonus = years * rating * 100
    if bonus > 5000:
        bonus = 5000 + (bonus - 5000) // 2
    return round(bonus, 2)

# Complex performance evaluation with red herrings
def process_assessment(raw_data):
    # Initialize various metrics (many are unused later)
    efficiency_metrics = defaultdict(float)
    behavioral_scores = {}
    anomaly_flags = []
    cumulative_weights = [0.1, 0.2, 0.3, 0.4]
    
    for record in raw_data:
        emp_id = record['id']
        efficiency = record['efficiency']
        reliability = record['reliability']
        feedback = record['feedback']
        
        # Real computation branch
        base_score = (efficiency * 0.6) + (reliability * 0.4)
        feedback_influence = analyze_feedback(feedback)
        adjusted_score = base_score + (feedback_influence * 0.5)
        
        # Distractor: complex but unused calculation
        normalized = math.log(max(adjusted_score, 1)) ** 0.5
        weighted_norm = sum([normalized * w for w in cumulative_weights]) / sum(cumulative_weights)
        rounded_norm = round(weighted_norm, 3)
        
        # Store only adjusted_score (others are distractions)
        behavioral_scores[emp_id] = adjusted_score
        
        # Anomaly detection (never used)
        if efficiency < 50 or reliability < 40:
            anomaly_flags.append(emp_id)
    
    return behavioral_scores

# Main evaluation pipeline
def evaluate_performance(log_entries):
    processed = process_assessment(log_entries)
    
    # Compute aggregate using only specific conditions
    high_performers = 0
    total_sum = 0.0
    
    # Another irrelevant intermediate
    stats_summary = []
    for emp, score in processed.items():
        if score >= 85:
            high_performers += 1
        if emp % 2 == 1:  # Only consider odd IDs
            total_sum += score * 1.1  # Bonus factor for odd IDs
        else:
            total_sum += score * 0.9  # Penalty for even IDs
        
        # Dead logic branch (always false in practice)
        if len(str(emp)) == 100:
            stats_summary.append(score * 0.01)
    
    # Final score computed from transformed total and performer count
    adjustment_factor = (high_performers + 1) / (len(processed) + 1)
    final_raw = total_sum * adjustment_factor
    
    # Apply bit manipulation trick (mask lower 16 bits then scale)
    masked = int(final_raw) & 0xFFFF  # Keep only lowest 16 bits
    scaled = masked * 1.05
    
    # This rounding produces the final deterministic answer
    return round(scaled, 4)

# Simulated input data (real signal amidst noise)
assessment_log = [
    {'id': 101, 'efficiency': 90, 'reliability': 88, 'feedback': 'excellent work good efficiency excellent'},
    {'id': 102, 'efficiency': 75, 'reliability': 80, 'feedback': 'good job but some errors'},
    {'id': 103, 'efficiency': 95, 'reliability': 92, 'feedback': 'proactive and reliable excellent'},
    {'id': 104, 'efficiency': 60, 'reliability': 70, 'feedback': 'poor motivation slow delivery'},
    {'id': 105, 'efficiency': 88, 'reliability': 85, 'feedback': 'efficient and excellent teamwork'}
]

# Unused auxiliary data (red herring)
employee_profiles = defaultdict(dict)
for entry in assessment_log:
    pid = entry['id']
    employee_profiles[pid]['category'] = 'STANDARD'
    employee_profiles[pid]['flags'] = []
    if entry['efficiency'] > 90:
        employee_profiles[pid]['flags'].append('HIGH_EFF')

# Key execution point
final_score = evaluate_performance(assessment_log)

# Output result as required
print(f"Target result: {final_score}")