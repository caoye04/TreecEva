from collections import Counter

def analyze_engagement(logs):
    activity_counts = Counter(logs)
    unique_users = len(activity_counts)
    total_actions = sum(activity_counts.values())
    avg_per_user = total_actions / unique_users if unique_users else 0
    return avg_per_user

def calculate_rating(data):
    base_score = analyze_engagement(data)
    bonus = len([x for x in data if 'post' in x]) * 0.1
    adjustment = (lambda x: x * 1.2 if x > 5 else x * 0.9)(base_score)
    final_rating = adjustment + bonus
    return round(final_rating, 3)

def monitor_system():
    # Simulated user engagement logs
    logs = ['user1:view', 'user2:like', 'user1:share', 'user3:like', 'user2:post', 'user1:post']
    
    # Irrelevant utility variable (minor distraction)
    temp_status = "active"
    
    final_score = calculate_rating(logs)
    
    # Additional unrelated operation (low interference)
    status_count = {"active": 1}
    
    print(f"Result: {final_score}")
    
    return final_score

# Execute
monitor_system()