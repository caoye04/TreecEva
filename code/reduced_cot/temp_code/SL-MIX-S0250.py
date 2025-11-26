data_records = ["user_001", "ADMIN_002", "user_003", "GUEST_004", "user_005"]

# Process user records
lowercase_users = [record.lower() for record in data_records if record.startswith('user')]
admin_users = [record for record in data_records if 'admin' in record.lower()]

# Count processed items
processed_items = lowercase_users + admin_users
final_count = len(processed_items)

print(f"Result: {final_count}")