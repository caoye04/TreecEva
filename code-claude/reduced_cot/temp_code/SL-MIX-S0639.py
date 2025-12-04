# User profile data validation
user_data = {
    'name': 'Alex Johnson',
    'email': 'alex@example.com',
    'age': 28,
    'location': 'Seattle'
}

# Fields that must be present
required_fields = ['name', 'email', 'password', 'phone']

# Count fields that are both required and present
common_elements = len(set(user_data.keys()) & set(required_fields))

# Generate list of missing required fields
missing_fields = [field for field in required_fields if field not in user_data]

# Total fields to be collected
total_fields_needed = len(missing_fields)

# Display validation results
print(f"Result: {common_elements}")