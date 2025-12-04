def parse_student_data(raw_data):
    # Parse student submission data from raw format
    parsed = {}
    for entry in raw_data.split(';'):
        if not entry.strip():
            continue
        parts = entry.split('|')
        if len(parts) < 3:
            continue
        student_id, score_str, timestamp = parts[0], parts[1], parts[2]
        try:
            score = float(score_str)
            parsed[student_id] = {'score': score, 'timestamp': timestamp}
        except ValueError:
            # Skip invalid scores
            pass
    return parsed

def filter_submissions(submissions, cutoff_date='2023-04-15'):
    # Filter submissions based on timestamp and validity
    valid = {}
    potential_duplicates = set()
    
    # Track potential late submissions for analysis (not used in final calculation)
    late_submissions = []
    
    for student_id, data in submissions.items():
        # Track duplicates for later analysis
        if student_id in valid:
            potential_duplicates.add(student_id)
        
        # Process submission date (not relevant to final calculation)
        submission_date = data['timestamp'].split(' ')[0]
        if submission_date > cutoff_date:
            late_submissions.append(student_id)
            continue
            
        # Store valid submission
        valid[student_id] = data['score']
    
    # This calculation doesn't affect the result
    duplicate_rate = len(potential_duplicates) / len(submissions) if submissions else 0
    
    return valid

def apply_bonus_penalty(score_dict):
    # Apply bonus/penalty based on complex rules (distractor function)
    bonus_threshold = 85
    penalty_threshold = 40
    result = {}
    
    for student_id, score in score_dict.items():
        adjusted = score
        if score > bonus_threshold:
            adjusted += (score - bonus_threshold) * 0.1
        elif score < penalty_threshold:
            adjusted -= (penalty_threshold - score) * 0.05
        result[student_id] = adjusted
    
    return result

def calculate_weighted_score(submissions):
    # Calculate final weighted score based on valid submissions
    if not submissions:
        return 0
    
    # Extract scores and convert student IDs to integers where possible
    scores = list(submissions.values())
    
    # These calculations don't affect the final result
    median_score = sorted(scores)[len(scores)//2] if scores else 0
    score_range = max(scores) - min(scores) if scores else 0
    
    # Core calculation logic
    total = sum(scores)
    count = len(scores)
    average = total / count if count else 0
    
    # Apply weighting formula
    weight_factor = 0.75
    base_score = 65
    
    # This lambda isn't used but serves as distraction
    normalization = lambda x: (x - min(scores)) / (max(scores) - min(scores)) if max(scores) != min(scores) else 0.5
    
    # Conditional expression for final calculation
    weighted_score = base_score + (average - base_score) * weight_factor if average > base_score else average
    
    # Round to 2 decimal places for final result
    return round(weighted_score, 2)

# Sample raw data with student submissions
raw_data = "2301|78.5|2023-04-01 09:30;2302|92.0|2023-04-10 14:15;2303|invalid|2023-04-12 11:45;" + \
          "2304|45.5|2023-04-20 16:30;2305|81.0|2023-04-14 10:20;2306|67.5|2023-04-08 13:40;" + \
          "2307|88.5|2023-04-13 15:10;2308|59.0|2023-04-11 08:55;2301|82.0|2023-04-14 12:05"

# Parse and process student data
parsed_data = parse_student_data(raw_data)

# Apply additional processing (not relevant to final calculation)
processed_data = {k: v for k, v in parsed_data.items() if '23' in k}

# Calculate statistics on raw scores (distractor)
all_scores = [data['score'] for data in parsed_data.values()]
raw_average = sum(all_scores) / len(all_scores) if all_scores else 0

# Filter submissions based on cutoff date
valid_submissions = filter_submissions(parsed_data)

# Apply bonus/penalty rules (distractor - not used in final calculation)
adjusted_submissions = apply_bonus_penalty(valid_submissions)

# Calculate weighted final score
final_score = calculate_weighted_score(valid_submissions)

print(f"Result: {final_score}")