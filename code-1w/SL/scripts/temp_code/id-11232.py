def main():
    # Student grades and performance modifiers
    grades = [85, 90, 78, 92]
    attendance_ratio = 0.95
    participation = True

    # Bonus function based on participation and attendance
    bonus_fn = lambda x: x * 1.1 if attendance_ratio > 0.9 else x * 1.05

    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = 100

    def calculate_total(scores, bonus):
        base_total = sum(scores)
        adjusted = bonus(base_total)
        if participation:
            adjusted += 5  # Extra credit for participation
            return adjusted
        return adjusted

    final_score = calculate_total(grades, bonus_fn)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()