# Online shopping recommendation system - Finding common preferences

# Available items in the store catalog
available_items = {'laptop', 'headphones', 'smartphone', 'tablet', 'camera', 'speaker'}

# User's browsing history and preferences
user_history = ['laptop', 'smartphone', 'smartwatch', 'headphones']
wishlist = {'tablet', 'camera', 'ebook_reader'}

# Convert history to set for operations
user_history_set = set(user_history)

# Combine user preferences from history and wishlist
user_preferences = user_history_set.union(wishlist)

# Calculate statistics
total_available = len(available_items)
total_preferences = len(user_preferences)

# Find items that match user preferences
common_elements = len(user_preferences.intersection(available_items))

# Calculate percentage match for user dashboard
match_percentage = (common_elements / total_preferences) * 100

# Prepare recommendation strength indicator
if match_percentage > 60:
    recommendation_strength = "Strong"
else:
    recommendation_strength = "Moderate"

print(f"Result: {common_elements}")