def main():
    # Student performance data
    exam_scores = [85, 90, 78, 92, 88]
    project_scores = [88, 84, 96, 90]

    # Convert to sets for overlap analysis
    exam_set = set(exam_scores)
    project_set = set(project_scores)

    # Irrelevant distraction: unused variable (minimal interference)
    attendance_records = [True, True, False, True]

    # Core logic using lambda for scoring transformation
    normalize = lambda x: x * 1.1 if x < 85 else x * 1.05

    def calculate_overlap_bonus(a, b):
        common = a & b  # Set intersection
        return len(common) * 5 if common else 0

    def calculate_final(exams, projects):
        base_exam = sum(map(normalize, exams)) / len(exams)
        base_project = sum(map(lambda x: x * 1.08, projects)) / len(projects)
        total = base_exam + base_project
        bonus = calculate_overlap_bonus(exams, projects)
        total += bonus
        if total > 180:
            return int(total)  # Early return equivalent via control flow
        return int(total + 10)

    final_score = calculate_final(exam_set, project_set)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()