from collections import Counter, defaultdict

# Simulate user feedback analysis in a code review system
def analyze_feedback(reviews):
    feedback_counter = Counter()
    temp_tracker = defaultdict(int)
    
    for review in reviews:
        tokens = review.lower().split()
        positive_triggers = ['good', 'great', 'excellent', 'well', 'efficient']
        negative_triggers = ['poor', 'bad', 'worse', 'inefficient', 'buggy']
        
        # Count relevant feedback
        for word in tokens:
            if word in positive_triggers:
                feedback_counter['positive'] += 1
            elif word in negative_triggers:
                feedback_counter['negative'] += 1

        # Irrelevant tracking (distractor)
        for token in tokens:
            temp_tracker[token] += 1
            
    return feedback_counter

# Baseline calibration function (some irrelevant logic included)
def calibrate_system(feedback_data, history_log=None):
    if history_log is None:
        history_log = [1, 1, 2, 3, 5, 8]  # Fibonacci distractor
    
    adjustment = 0
    cumulative = 0
    
    # Useless loop over history (semi-relevant but not used later)
    for i in range(len(history_log)):
        cumulative += history_log[i]
        if cumulative > 10:
            adjustment = cumulative // 4
            break
    
    # Actual relevant computation
    scale_factor = len(history_log) if history_log else 1
    return adjustment + scale_factor

# Main evaluation logic
def evaluate_performance(counter, base):
    pos = counter.get('positive', 0)
    neg = counter.get('negative', 0)
    
    # Core formula
    raw_score = (pos * 3) - (neg * 2)
    
    # Distractor variables and operations
    intermediate = (pos + neg) ** 0.5 if (pos + neg) > 0 else 0
    noise_offset = sum([i * 2 for i in range(3)]) // 3  # Always evaluates to 2
    
    # Final adjustment using base
    final_score = raw_score + base - noise_offset
    
    # Additional red herring: unused conditional with complex condition
    if pos > neg and (intermediate * 2) > base and base % 2 == 0:
        final_score *= 1.1
    
    return int(final_score)

# Simulated input data
review_set = [
    "The code is excellent and well structured",
    "Poor error handling and buggy logic",
    "Great job on optimization",
    "Inefficient memory usage, needs improvement",
    "Good modular design"
]

# Execution flow
feedback_results = analyze_feedback(review_set)
calibration_base = calibrate_system(feedback_results, [2, 4, 6])
final_score = evaluate_performance(feedback_results, calibration_base)

# Output result
print(f"Result: {final_score}")