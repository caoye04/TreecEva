from collections import defaultdict
import math

def analyze_sentiment(text):
    # Irrelevant sentiment analysis function (dead code path)
    words = text.lower().split()
    positive = ['good', 'great', 'excellent', 'amazing']
    negative = ['bad', 'terrible', 'awful', 'poor']
    score = 0
    for word in words:
        if word in positive:
            score += 1
        elif word in negative:
            score -= 1
    return score

def dummy_transform(data):
    # Misleading transformation that isn't used in final computation
    result = []
    for item in data:
        transformed = 0
        for c in item['name']:
            transformed += ord(c) % 5
        result.append(transformed * len(item['content']))
    return result

def compute_entropy(values):
    # Distractor: computes entropy but not used in final result
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def validate_structure(items):
    # Red herring validation function with side computations
    issues = 0
    checksum = 0
    for i, item in enumerate(items):
        if 'id' not in item or 'data' not in item:
            issues += 1
        checksum ^= (i + len(str(item.get('id', ''))))
    return issues == 0, checksum

def accumulate_magnitude(seq):
    # Unused complex accumulation with bit manipulation
    mag = 0
    for i, val in enumerate(seq):
        mag += abs(val) << (i % 4)
        mag = mag ^ (mag >> 3)
    return mag

def extract_keywords(feedback_list):
    # Decoy NLP-style processing
    keywords = defaultdict(int)
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at'}
    for entry in feedback_list:
        words = entry['text'].lower().replace('.', '').replace(',', '').split()
        for w in words:
            if w.isalpha() and w not in stop_words:
                keywords[w] += 1
    return sorted(keywords.items(), key=lambda x: -x[1])[:10]

def process_feedback(reviews, weights):
    # Core relevant logic buried among distractors
    base_scores = []
    adjustment_factors = []
    
    for review in reviews:
        raw_rating = review['rating']
        length_factor = len(review['comment']) / 10.0
        adjusted_rating = raw_rating * (1 + 0.1 * min(length_factor, 5))
        base_scores.append(adjusted_rating)
        
        urgency_modifier = 1.0
        if 'urgent' in review['tags']:
            urgency_modifier *= 1.2
        if 'critical' in review['tags']:
            urgency_modifier *= 1.5
        adjustment_factors.append(urgency_modifier)
    
    weighted_sum = 0.0
    total_weight = 0.0
    for i in range(len(base_scores)):
        weighted_sum += base_scores[i] * weights[i] * adjustment_factors[i]
        total_weight += weights[i] * adjustment_factors[i]
    
    avg_adjusted = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Secondary correction based on reviewer seniority
    senior_bonus = 0
    for review in reviews:
        if review['reviewer_level'] == 'senior':
            senior_bonus += 0.25
    
    final_normalized = avg_adjusted + (senior_bonus / len(reviews))
    return round(final_normalized, 6)

# Main execution block
if __name__ == '__main__':
    # Irrelevant dataset initialization (distractor)
    user_data = [
        {'name': 'Alice', 'content': 'log_01.txt', 'active': True},
        {'name': 'Bob', 'content': 'config.xml', 'active': False}
    ]
    
    dummy_results = dummy_transform(user_data)
    
    # Real input data for the actual computation
    reviews = [
        {
            'rating': 4,
            'comment': 'Good performance overall with excellent response time.',
            'tags': ['urgent'],
            'reviewer_level': 'junior'
        },
        {
            'rating': 5,
            'comment': 'Outstanding system stability under high load conditions.',
            'tags': ['critical'],
            'reviewer_level': 'senior'
        },
        {
            'rating': 3,
            'comment': 'Average throughput, needs optimization in memory usage.',
            'tags': [],
            'reviewer_level': 'mid'
        },
        {
            'rating': 4,
            'comment': 'Solid implementation with good documentation.',
            'tags': ['urgent', 'critical'],
            'reviewer_level': 'senior'
        }
    ]
    
    weights = [0.2, 0.4, 0.1, 0.3]
    
    # Dead code path: unused advanced analytics
    all_ratings = [r['rating'] for r in reviews]
    entropy = compute_entropy(all_ratings)
    structure_ok, checksum = validate_structure([
        {'id': 'A1', 'data': [1,2]},
        {'id': 'B2', 'data': [3,4]}
    ])
    magnitude = accumulate_magnitude([10, -5, 8, 0, 3])
    keywords = extract_keywords(reviews)
    
    # Key statement that produces the answer
    final_score = process_feedback(reviews, weights)
    
    # Output result as required
    print(f"Target result: {final_score}")