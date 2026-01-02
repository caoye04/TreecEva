from collections import defaultdict
import math

# Simulate user feedback analysis for a coding education platform
def analyze_feedback(feedback_list):
    sentiment_count = defaultdict(int)
    word_frequency = {}
    total_entries = len(feedback_list)
    
    # Process each feedback entry
    for entry in feedback_list:
        words = entry.lower().split()
        positive_keywords = ['good', 'great', 'excellent', 'helpful']
        negative_keywords = ['bad', 'poor', 'confusing', 'hard']
        
        has_positive = any(word.strip('.,!?') in positive_keywords for word in words)
        has_negative = any(word.strip('.,!?') in negative_keywords for word in words)
        
        if has_positive and not has_negative:
            sentiment_count['positive'] += 1
        elif has_negative and not has_positive:
            sentiment_count['negative'] += 1
        else:
            sentiment_count['neutral'] += 1
        
        # Track word frequency (distractor computation)
        for word in words:
            cleaned = word.strip('.,!?')
            if cleaned not in positive_keywords and cleaned not in negative_keywords:
                word_frequency[cleaned] = word_frequency.get(cleaned, 0) + 1

    # Misleading normalization (not used in final result)
    normalized_sentiment = {k: v / total_entries for k, v in sentiment_count.items()}
    avg_word_length = sum(len(w) for w in word_frequency.keys()) / max(len(word_frequency), 1)
    
    return sentiment_count, word_frequency, avg_word_length

# Assess code quality metrics from student submissions
def compute_code_metrics(submissions):
    complexity_scores = []n    style_violations = 0
    
    for code in submissions:
        lines = code.split('\n')
        line_count = len(lines)
        char_count = sum(len(line) for line in lines)
        indentation_issues = sum(1 for line in lines if line.startswith(' ') and not line.startswith('    '))
        
        # Heuristic complexity score
        complexity = line_count * (1 + indentation_issues / max(line_count, 1))
        complexity_scores.append(complexity)
        
        # Style check (irrelevant to final answer)
        if 'import antigravity' in code:
            style_violations += 1

    mean_complexity = sum(complexity_scores) / max(len(complexity_scores), 1)
    peak_complexity = max(complexity_scores, default=0)
    
    # Extra unused metric
    efficiency_ratio = (peak_complexity / mean_complexity) if mean_complexity > 0 else 0
    
    return {
        'mean_complexity': mean_complexity,
        'peak_complexity': peak_complexity,
        'efficiency_ratio': efficiency_ratio
    }

# Aggregate performance based on multiple inputs
def aggregate_performance(feedback_summary):
    raw_counts, _, _ = feedback_summary
    
    # Key calculation: weighted score based on sentiment distribution
    pos = raw_counts['positive']
    neg = raw_counts['negative']
    neu = raw_counts['neutral']
    total = pos + neg + neu
    
    if total == 0:
        base_score = 0
    else:
        # Normalize and apply non-linear transform
        p_ratio = pos / total
        n_ratio = neg / total
        balance_factor = (p_ratio - n_ratio) + 0.5  # Center at 0.5
        
        # Apply sigmoid-like shaping
        shaped_score = 100 / (1 + math.exp(-10 * (balance_factor - 0.5)))
    
    # Secondary adjustment based on neutral feedback
    neutral_pressure = neu / total if total > 0 else 0
    decay_factor = math.exp(-neutral_pressure)
    adjusted_score = shaped_score * decay_factor
    
    # Final transformation (this is where final_score is set)
    final_score = int(round(adjusted_score))
    
    # Dead code path - never executed under normal conditions
    debug_mode = False
    if debug_mode:
        print(f'Debug: {shaped_score=}, {decay_factor=}')
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Sample data
    user_feedback = [
        'This lesson was excellent and very helpful!',
        'The examples were confusing and too hard to follow.',
        'Good explanations but could be better organized.',
        'Great content overall, really enjoyed it.',
        'Poor structure, felt disorganized.',
        'It was okay, nothing special.',
        'Excellent teaching style, clear and concise.',
        'Hard to understand, needs improvement.',
        'Neutral experience, neither good nor bad.',
        'Amazing resource, extremely helpful!'    ]
    
    # Code submissions (partially relevant context)
    student_submissions = [
        'def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a',
        'def sort_array(arr):\n    return sorted(arr)',
        'import antigravity\nprint("I can fly!")'
    ]
    
    # Step 1: Analyze feedback
    feedback_analysis = analyze_feedback(user_feedback)
    
    # Step 2: Compute code metrics (distractor - not used later)
    code_stats = compute_code_metrics(student_submissions)
    
    # Step 3: Aggregate performance (key statement)
    final_score = aggregate_performance(feedback_analysis)
    
    # Output result
    print(f'Result: {final_score}')