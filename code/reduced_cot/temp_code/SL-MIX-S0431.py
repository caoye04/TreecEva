user_roles = {'admin', 'moderator', 'editor', 'viewer'}
user_permissions = {'read', 'write', 'delete', 'execute'}
verified_users = {'admin', 'editor'}

eligible_roles = user_roles - {'viewer'}
has_permissions = len(user_permissions & {'read', 'write'}) >= 2
is_verified = len(verified_users & eligible_roles) > 0

approved_members = len(eligible_roles) * 3
rejected_members = len(user_roles - eligible_roles) * 2

final_count = approved_members if is_verified else rejected_members
print(f"Result: {final_count}")