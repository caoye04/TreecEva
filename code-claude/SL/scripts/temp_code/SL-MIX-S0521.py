from collections import Counter, defaultdict

def analyze_workflow_metrics(project_data, team_size=5):
    # Initialize tracking variables
    performance_index = 0
    quality_metrics = defaultdict(int)
    team_velocity = team_size * 3.75  # Average velocity per team member
    
    # Process project data
    for phase, tasks in project_data.items():
        if phase == "planning":
            performance_index += sum(task["effort"] for task in tasks) / 2
        quality_metrics[phase] = len(tasks) * 1.5
    
    # Calculate overall quality score (not used in final calculation)
    quality_score = sum(quality_metrics.values()) / len(quality_metrics)
    return team_velocity * 2, performance_index

def calculate_priority(current_tasks, completed_tasks):
    # Extract task types for analysis
    current_types = [task["type"] for task in current_tasks if task["active"]]
    completed_types = [task["type"] for task in completed_tasks]
    
    # Count occurrences of each task type
    current_counter = Counter(current_types)
    completed_counter = Counter(completed_types)
    
    # Calculate task distribution metrics
    pending_bugs = current_counter.get("bug", 0)
    completed_bugs = completed_counter.get("bug", 0)
    pending_features = current_counter.get("feature", 0)
    completed_features = completed_counter.get("feature", 0)
    
    # Calculate various metrics that seem important but most aren't used
    bug_ratio = (pending_bugs / (completed_bugs + 1)) * 10
    feature_completion = (completed_features / (pending_features + completed_features)) * 100 if pending_features + completed_features > 0 else 0
    critical_index = sum(task["priority"] for task in current_tasks if task["priority"] > 7)
    
    # Complex but ultimately unused calculation
    weighted_priority = 0
    for i, task in enumerate(current_tasks):
        if i % 3 == 0 and task["active"]:
            weighted_priority += task["priority"] * 1.5
    
    # The actual priority score calculation
    priority_score = (pending_bugs * 3) - (completed_bugs // 2) + (pending_features // 2)
    
    return priority_score

# Project data setup
project_metrics = {
    "planning": [{"effort": 5}, {"effort": 3}, {"effort": 7}],
    "development": [{"effort": 10}, {"effort": 8}],
    "testing": [{"effort": 6}, {"effort": 4}]
}

# Task data setup
current_tasks = [
    {"id": 1, "type": "bug", "priority": 8, "active": True},
    {"id": 2, "type": "feature", "priority": 6, "active": True},
    {"id": 3, "type": "bug", "priority": 9, "active": False},
    {"id": 4, "type": "feature", "priority": 5, "active": True},
    {"id": 5, "type": "documentation", "priority": 3, "active": True},
    {"id": 6, "type": "bug", "priority": 7, "active": True}
]

completed_tasks = [
    {"id": 101, "type": "bug", "priority": 9},
    {"id": 102, "type": "bug", "priority": 8},
    {"id": 103, "type": "feature", "priority": 7},
    {"id": 104, "type": "documentation", "priority": 4}
]

# Process workflow metrics (not used in final calculation)
velocity, performance = analyze_workflow_metrics(project_metrics)

# Calculate task priorities
task_importance = []
for i, task in enumerate(current_tasks):
    if task["active"]:
        # Misleading calculation not used for final result
        importance = task["priority"] * (3 if task["type"] == "bug" else 2)
        task_importance.append((task["id"], importance))

# Sort tasks by importance (distraction)
task_importance.sort(key=lambda x: x[1], reverse=True)

# This is the key calculation we're asking about
priority_score = calculate_priority(current_tasks, completed_tasks)

# Some more misleading calculations after the key statement
weighted_velocity = velocity * (1 + (priority_score / 100))
adjusted_performance = performance + (len(task_importance) * 0.5)

print(f"Task Analysis Results:")
print(f"Workflow Velocity: {velocity}")
print(f"Performance Index: {performance}")
print(f"Priority Score: {priority_score}")
print(f"Weighted Velocity: {weighted_velocity}")
print(f"Adjusted Performance: {adjusted_performance}")