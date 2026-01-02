def main():
    # Student assessment scores and category weights
    assessments = {
        'quiz': [85, 90, 78],
        'midterm': 88,
        'project': 92,
        'final': 84
    }

    weight_map = {
        'quiz': 0.2,
        'midterm': 0.25,
        'project': 0.15,
        'final': 0.4
    }

    # Irrelevant utility (minimal interference)
    get_avg = lambda lst: sum(lst) / len(lst)

    def calculate_total(grades, weights):
        total = 0.0
        for category, score in grades.items():
            if isinstance(score, list):
                avg_score = get_avg(score)
                total += avg_score * weights[category]
            else:
                total += score * weights[category]
        return round(total, 3)

    # Computation of final score
    final_score = calculate_total(assessments, weight_map)

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()