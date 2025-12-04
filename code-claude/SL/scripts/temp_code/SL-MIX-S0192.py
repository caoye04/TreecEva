from collections import Counter, defaultdict

def calculate_weighted_score(data, weights):
    """Calculate weighted score based on filtered data and weight factors"""
    if not data or sum(weights.values()) == 0:
        return 0
    
    # Extract only relevant values
    relevant_values = [v for k, v in data.items() if k in weights]
    
    # Calculate weighted sum
    weighted_sum = sum(v * weights.get(k, 0) for k, v in data.items())
    normalization = sum(weights.values())
    
    return weighted_sum / normalization

# Student performance analysis system
student_records = [
    {'id': 101, 'name': 'Alice', 'scores': [85, 92, 78], 'attendance': 0.95},
    {'id': 102, 'name': 'Bob', 'scores': [76, 88, 90], 'attendance': 0.85},
    {'id': 103, 'name': 'Charlie', 'scores': [92, 95, 88], 'attendance': 0.99},
    {'id': 104, 'name': 'Diana', 'scores': [65, 72, 68], 'attendance': 0.7},
]

# Process student records - this is mostly distraction
def process_records(records):
    score_counter = Counter()
    attendance_data = {}
    performance_index = defaultdict(int)
    
    for i, student in enumerate(records):
        # Calculate average score
        avg_score = sum(student['scores']) / len(student['scores'])
        score_counter[int(avg_score // 10 * 10)] += 1  # Group by tens
        
        # Track attendance
        attendance_data[student['id']] = student['attendance']
        
        # Calculate misleading performance index
        factor = i % 2 + 1  # Irrelevant factor
        performance_index[student['id']] = avg_score * student['attendance'] * factor
    
    return score_counter, attendance_data, performance_index

# Generate some distraction metrics
score_distribution, attendance_data, performance_index = process_records(student_records)

# More distraction - calculate class statistics
class_avg = sum(sum(s['scores']) / len(s['scores']) for s in student_records) / len(student_records)
max_score = max(max(s['scores']) for s in student_records)
min_score = min(min(s['scores']) for s in student_records)
attendance_avg = sum(s['attendance'] for s in student_records) / len(student_records)

# Some bit operations as distractions
def encode_student_id(student_id):
    magic_number = 0x5A3C
    return (student_id << 4) ^ magic_number

encoded_ids = [encode_student_id(s['id']) for s in student_records]

# This looks important but is a distraction
def calculate_performance_metric(scores, attendance):
    base_score = sum(scores) / len(scores)
    attendance_factor = 1 + (attendance - 0.8) * 0.5 if attendance > 0.8 else 1
    return base_score * attendance_factor

# Calculate metrics for all students - more distraction
performance_metrics = {}
for student in student_records:
    metric = calculate_performance_metric(student['scores'], student['attendance'])
    performance_metrics[student['id']] = metric

# Here's the relevant part - prepare filtered data
raw_data = {'exam': 85, 'project': 92, 'participation': 78, 'extra_credit': 15}
bonus_points = raw_data['extra_credit'] * 0.5  # Half of extra credit points

# This is the key operation
filtered_data = {
    'exam': raw_data['exam'],
    'project': raw_data['project'], 
    'participation': raw_data['participation'],
    'bonus': bonus_points
}

# Define weights - these are actually used
weight_factors = {
    'exam': 0.4,
    'project': 0.35,
    'participation': 0.15,
    'bonus': 0.1
}

# Distraction - create alternative weights that won't be used
alternative_weights = {k: v * 1.2 for k, v in weight_factors.items()}
scaled_weights = {k: v / sum(weight_factors.values()) for k, v in weight_factors.items()}

# This is the key statement
target_score = calculate_weighted_score(filtered_data, weight_factors)

# Distraction - calculate other metrics that won't be used
adjusted_score = target_score * (1 + attendance_avg / 10)
curved_score = target_score + (100 - class_avg) * 0.1

# More distractions
if target_score > 90:
    grade = 'A'
elif target_score > 80:
    grade = 'B'
elif target_score > 70:
    grade = 'C'
else:
    grade = 'D'

print(f"Target result: {target_score}")