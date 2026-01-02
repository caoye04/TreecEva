def analyze_priority_tasks():
    # Define sets of tasks assigned to different teams
    team_a_tasks = {1, 2, 3, 4, 5, 6}
    team_b_tasks = {4, 5, 6, 7, 8, 9}
    team_c_tasks = {5, 6, 7, 8, 10, 11}

    # Find common tasks between all three teams
    common_ab = team_a_tasks & team_b_tasks
    common_abc = common_ab & team_c_tasks  # Tasks common to all teams

    # Simulate a priority filter for urgent tasks
    priority_set = {5, 6, 12, 13}

    # Final overlap: common tasks that are also in priority set
    final_overlap = common_abc & priority_set

    # Irrelevant metric (minor distraction)
    task_volume = len(team_a_tasks) + len(team_b_tasks)

    # Output result
    print(f"Result: {final_overlap}")

analyze_priority_tasks()