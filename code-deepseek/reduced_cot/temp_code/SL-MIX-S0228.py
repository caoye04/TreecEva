team_effort = [3, 5, 2, 4]
project_workloads = [7, 2, 8, 5]
total_effort = sum(effort * workload for effort, workload in zip(team_effort, project_workloads))
print(f"Result: {total_effort}")