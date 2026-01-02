from collections import defaultdict
import math

# Simulated employee assessment system with multiple evaluation dimensions
def analyze_productivity(metrics):
    efficiency = metrics.get('tasks_completed', 0) / max(metrics.get('hours_logged', 1), 1)
    error_rate = metrics.get('errors', 0) / max(metrics.get('tasks_completed', 1), 1)
    return efficiency * (1 - min(error_rate, 0.9))

# Irrelevant helper function - decoy for code readers
def calculate_network_latency(packet_sizes):
    if not packet_sizes:
        return 0.0
    mean_size = sum(packet_sizes) / len(packet_sizes)
    variance = sum((s - mean_size) ** 2 for s in packet_sizes) / len(packet_sizes)
    return math.sqrt(variance)

# Core evaluation logic
def process_feedback(feedback_strings):
    word_count = defaultdict(int)
    positive_keywords = ['excellent', 'good', 'improved', 'reliable']
    negative_keywords = ['poor', 'error', 'delay', 'failure']
    
    for fb in feedback_strings:
        words = fb.lower().split()
        for w in words:
            word_count[w] += 1
    
    score = 0
    for kw in positive_keywords:
        score += word_count[kw] * 2
    for kw in negative_keywords:
        score -= word_count[kw] * 3
    
    # Distractor: unused transformation
    normalized = {k: v / max(word_count.values()) for k, v in word_count.items()} if word_count else {}
    return score

# Misleading data processing path - dead code
def infer_team_dynamics(team_data):
    cohesion_index = 0
    for member in team_data:
        if member['seniority'] > 2 and member['peer_reviews'] >= 4:
            cohesion_index += 1.5
    return cohesion_index

# Main evaluation pipeline
def evaluate_performance(log):
    base_score = 0
    
    # Step 1: Process quantitative metrics
    productivity = analyze_productivity(log['metrics'])
    base_score += productivity * 100
    
    # Step 2: Analyze qualitative feedback
    feedback_value = process_feedback(log['feedback'])
    base_score += feedback_value * 5
    
    # Step 3: Apply experience multiplier (conditional)
    experience_years = log['profile']['experience']
    if experience_years > 5:
        base_score *= 1.2
    elif experience_years > 2:
        base_score *= 1.1
    else:
        base_score *= 0.9
    
    # Step 4: Adjustment based on project complexity
    complexity_factor = log['project'].get('complexity', 1)
    base_score += 10 * complexity_factor
    
    # Irrelevant intermediate calculation - red herring
    avg_task_size = sum(len(tsk) for tsk in log['project']['tasks']) / len(log['project']['tasks']) if log['project']['tasks'] else 0
    size_penalty = max(0, avg_task_size - 15) * 0.5
    
    # Final adjustment: cap extreme scores
    final = max(50, min(base_score, 500))
    
    # Distractor variables
    normalized_score = (final - 50) / 4.5  # Not used
    percentile_rank = math.erf(normalized_score / 10)  # Dead computation
    
    return final

# Simulated input data
assessment_log = {
    'metrics': {
        'tasks_completed': 48,
        'hours_logged': 160,
        'errors': 6
    },
    'feedback': [
        'excellent work on the core module',
        'good improvement in reliability',
        'minor errors in documentation',
        'excellent attention to detail'
    ],
    'profile': {
        'experience': 7,
        'role': 'senior_developer'
    },
    'project': {
        'complexity': 3,
        'tasks': ['design', 'implementation', 'testing', 'deployment', 'review']
    }
}

# Unused data - distraction
network_packets = [128, 256, 512, 64, 1024, 256, 128]
latency = calculate_network_latency(network_packets)

team_info = [
    {'seniority': 6, 'peer_reviews': 5},
    {'seniority': 3, 'peer_reviews': 4},
    {'seniority': 8, 'peer_reviews': 3}
]

dummy_cohesion = infer_team_dynamics(team_info)

# Key execution point
final_score = evaluate_performance(assessment_log)
print(f"Result: {final_score}")