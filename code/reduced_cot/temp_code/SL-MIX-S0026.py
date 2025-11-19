from collections import defaultdict

class PermissionNode:
    def __init__(self, level):
        self.level = level
        self.left = None
        self.right = None

def build_permission_tree():
    root = PermissionNode(1)
    root.left = PermissionNode(2)
    root.right = PermissionNode(3)
    root.left.left = PermissionNode(4)
    root.left.right = PermissionNode(5)
    return root

def calculate_clearance(node):
    if not node:
        return 0
    return node.level + max(calculate_clearance(node.left), calculate_clearance(node.right))

# Staff roles with base access levels
staff_roles = {
    'junior_researcher': 10,
    'senior_researcher': 20,
    'curator': 30,
    'senior_curator': 40
}

# Additional access points from special projects
special_projects = {
    'egyptian_collection',
    'renaissance_paintings',
    'modern_sculptures'
}

# Seniority bonuses (years of service)
seniority_bonus = defaultdict(int, {
    'junior_researcher': 2,
    'senior_researcher': 5,
    'curator': 8,
    'senior_curator': 12
})

# Calculate base clearance
permission_tree = build_permission_tree()
tree_clearance_value = calculate_clearance(permission_tree)

# Greedy assignment of project access
project_access = {}
roles_list = sorted(staff_roles.keys(), key=lambda x: staff_roles[x], reverse=True)
projects_list = list(special_projects)

for i, role in enumerate(roles_list):
    if i < len(projects_list):
        project_access[role] = {projects_list[i]}
    else:
        project_access[role] = set()

# Calculate final clearance for senior curator
base_clearance = staff_roles['senior_curator']
tree_bonus = tree_clearance_value
seniority_points = seniority_bonus['senior_curator']
project_bonus = len(project_access['senior_curator']) * 3

# Apply a greedy optimization for maximum access
available_clearance_points = {1, 2, 4, 8, 16}
used_points = set()
total_bonus = 0

for point in sorted(available_clearance_points, reverse=True):
    if point <= (tree_bonus + seniority_points + project_bonus) and point not in used_points:
        total_bonus += point
        used_points.add(point)

senior_curator_clearance = base_clearance + tree_bonus + seniority_points + project_bonus + total_bonus

print(f"Result: {senior_curator_clearance}")