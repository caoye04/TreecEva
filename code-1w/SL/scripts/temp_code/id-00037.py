import math
import hashlib

user_segments = ['tech_enthusiast', 'casual_browser', 'content_creator', 'social_influencer']
interaction_weights = {'like': 1.2, 'share': 2.5, 'comment': 3.0, 'follow': 1.8}
base_transforms = {'tech_enthusiast': 'click_stream', 'casual_browser': 'view_history', 'content_creator': 'post_activity', 'social_influencer': 'engagement_matrix'}

entropy_components = []
for segment in user_segments:
    transform_key = base_transforms[segment]
    combined_string = f"{segment}_{transform_key}"
    hashed = hashlib.md5(combined_string.encode()).hexdigest()
    hash_sum = sum(ord(c) for c in hashed[:8])
    
    if hash_sum % 3 == 0:
        weighted_value = hash_sum * interaction_weights['share']
    elif hash_sum % 3 == 1:
        weighted_value = hash_sum * interaction_weights['comment']
    else:
        weighted_value = hash_sum * interaction_weights['follow']
    
    log_scaled = math.log(weighted_value + 1)
    entropy_components.append(log_scaled)

product_accum = 1.0
for component in entropy_components:
    product_accum *= math.exp(component)

final_metric = round(product_accum / len(entropy_components), 6)
print(f"Result: {final_metric}")