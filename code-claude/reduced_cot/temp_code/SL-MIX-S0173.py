import itertools
from collections import Counter

def calculate_customer_priority(customer_data, purchase_history):
    # Extract customer loyalty tier and account age
    loyalty_tier = customer_data.get('tier', 'bronze')
    account_age = customer_data.get('account_age', 0)
    
    # Calculate base priority based on tier
    tier_values = {
        'bronze': 10,
        'silver': 20,
        'gold': 35,
        'platinum': 50,
        'diamond': 75
    }
    
    # Marketing campaign settings (unused - distractor)
    campaign_multipliers = {
        'email': 1.2,
        'sms': 1.5,
        'push': 1.1,
        'direct_mail': 2.0
    }
    
    # Calculate engagement score (distractor calculation)
    engagement_metrics = customer_data.get('engagement', {})
    email_opens = engagement_metrics.get('email_opens', 0)
    app_visits = engagement_metrics.get('app_visits', 0)
    engagement_score = email_opens * 0.5 + app_visits * 0.8
    
    # Process purchase history
    if not purchase_history:
        return tier_values.get(loyalty_tier, 5) + (account_age // 12)
    
    # Calculate purchase frequency and recency
    purchase_frequency = len(purchase_history)
    most_recent = min([p.get('days_ago', 365) for p in purchase_history])
    recency_factor = max(0, 1 - (most_recent / 100))
    
    # Extract product categories from purchases
    categories = []
    for purchase in purchase_history:
        categories.extend(purchase.get('categories', []))
    
    # Calculate category diversity score
    category_counts = Counter(categories)
    diversity_score = len(category_counts)
    
    # Potential referral calculation (distractor)
    referral_bonus = 0
    if customer_data.get('referrals', 0) > 0:
        referral_bonus = customer_data['referrals'] * 5
        if loyalty_tier in ['gold', 'platinum', 'diamond']:
            referral_bonus *= 1.5
    
    # Calculate average purchase value
    purchase_values = [p.get('value', 0) for p in purchase_history]
    avg_value = sum(purchase_values) / len(purchase_values) if purchase_values else 0
    
    # Seasonal adjustment (distractor calculation)
    seasonal_factors = {'winter': 1.1, 'summer': 1.2, 'spring': 1.0, 'fall': 1.15}
    current_season = 'winter'  # Assume current season
    seasonal_adjustment = seasonal_factors.get(current_season, 1.0)
    
    # Combine factors to calculate customer value (distractor path)
    if customer_data.get('vip', False):
        customer_value = tier_values.get(loyalty_tier, 10) * 2 + engagement_score
        if avg_value > 500:
            customer_value += 50
    else:
        customer_value = tier_values.get(loyalty_tier, 10) + (engagement_score / 2)
    
    # Calculate actual priority score
    base_score = tier_values.get(loyalty_tier, 10)
    loyalty_bonus = min(25, account_age // 12)
    purchase_score = min(15, purchase_frequency) + (avg_value / 20)
    recency_points = int(recency_factor * 15)
    diversity_points = min(10, diversity_score * 2)
    
    # Final calculation
    priority_score = base_score + loyalty_bonus + purchase_score + recency_points + diversity_points
    return int(priority_score)

# Customer data
customer_data = {
    'id': 'C123456',
    'tier': 'gold',
    'account_age': 38,
    'vip': False,
    'referrals': 3,
    'engagement': {
        'email_opens': 12,
        'app_visits': 8,
        'social_clicks': 5
    },
    'segment': 'high_value'
}

# Purchase history
purchase_history = [
    {'id': 'P001', 'value': 120, 'days_ago': 15, 'categories': ['electronics', 'accessories']},
    {'id': 'P002', 'value': 85, 'days_ago': 45, 'categories': ['clothing']},
    {'id': 'P003', 'value': 210, 'days_ago': 7, 'categories': ['electronics', 'home']},
    {'id': 'P004', 'value': 65, 'days_ago': 60, 'categories': ['books', 'gifts']}
]

# Calculate potential cross-sell opportunities (distractor)
def find_cross_sell_opportunities(purchase_history):
    all_categories = list(itertools.chain.from_iterable([p.get('categories', []) for p in purchase_history]))
    category_counts = {cat: all_categories.count(cat) for cat in set(all_categories)}
    missing_categories = ['beauty', 'fitness', 'travel', 'food']
    opportunities = [cat for cat in missing_categories if cat not in category_counts]
    return opportunities

# Calculate marketing channel preferences (distractor)
def calculate_channel_preferences(engagement_metrics):
    channels = {'email': 0, 'app': 0, 'social': 0, 'sms': 0}
    if engagement_metrics.get('email_opens', 0) > 10:
        channels['email'] = 3
    elif engagement_metrics.get('email_opens', 0) > 5:
        channels['email'] = 2
    else:
        channels['email'] = 1
        
    if engagement_metrics.get('app_visits', 0) > 5:
        channels['app'] = 3
    else:
        channels['app'] = 1
        
    channels['social'] = min(3, engagement_metrics.get('social_clicks', 0) // 2)
    return channels

# Process data and calculate priority
cross_sell = find_cross_sell_opportunities(purchase_history)
channel_prefs = calculate_channel_preferences(customer_data['engagement'])

# Calculate customer priority score
priority_score = calculate_customer_priority(customer_data, purchase_history)

# Apply seasonal adjustment (distractor - not actually used)
seasonal_factors = {'winter': 1.1, 'summer': 1.2, 'spring': 1.0, 'fall': 1.15}
current_season = 'winter'
seasonal_priority = priority_score * seasonal_factors[current_season]

print(f"Result: {priority_score}")