def calculate_user_metrics(active_days=30, premium_threshold=50):
    # User activity tracking
    user_logins = {'user1': 45, 'user2': 15, 'user3': 60, 'user4': 30, 'user5': 10, 'user6': 55}
    purchase_history = {'user1': 65, 'user2': 25, 'user3': 40, 'user4': 55, 'user5': 30}
    
    # Identify active and premium users
    active_users = set()
    premium_users = set()
    potential_vip = set()
    
    for user, logins in user_logins.items():
        if logins >= active_days:
            active_users.add(user)
            
        # Track potential VIP users (not used in final calculation)
        if logins > 40:
            potential_vip.add(user)
    
    for user, amount in purchase_history.items():
        if amount >= premium_threshold:
            premium_users.add(user)
    
    # Calculate overlap statistics
    total_users = len(active_users.union(premium_users))
    duplicates = 0
    
    # Find users who are both active and premium
    common_elements = len(active_users.intersection(premium_users)) - duplicates
    
    # Calculate engagement score (not used in final result)
    engagement_score = total_users * 2 - common_elements
    
    # Simulate some recursive calculation for intervention
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    factorial_5 = factorial(5)
    
    print(f"Total unique users: {total_users}")
    print(f"Result: {common_elements}")
    return common_elements

calculate_user_metrics()