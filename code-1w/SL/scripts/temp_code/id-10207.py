from collections import defaultdict

# Simulate developer contribution analysis with noise and distractions
def analyze_developer_impact():
    raw_lines = [120, 245, 89, 156, 301]
    bug_fixes = [5, 12, 3, 8, 15]
    code_reviews = [23, 45, 12, 33, 67]
    deprecated_ratio = [0.05, 0.12, 0.3, 0.08, 0.18]  # Irrelevant in final logic

    # Distractor: unused transformation
    adjusted_reviews = [r * 1.1 for r in code_reviews if r > 20]

    # Core contribution metric per developer
    contributions = []
    for i in range(len(raw_lines)):
        base = raw_lines[i] * 0.1
        bonus = bug_fixes[i] * 2
        review_weight = code_reviews[i] * 0.5
        total_pts = base + bonus + review_weight
        
        # Artificial suppression based on deprecated code (distractor)
        if deprecated_ratio[i] > 0.1:
            total_pts *= 0.9  # Minor distraction, not ultimately decisive
            
        contributions.append(max(total_pts, 0))

    # Penalty system setup (only some entries matter)
    penalty_map = defaultdict(int)
    penalty_map[0] = 5
    penalty_map[1] = 10
    penalty_map[2] = 50  # High penalty, but index 2 has low contribution
    penalty_map[3] = 15
    penalty_map[4] = 0
    penalty_map[5] = 100  # Irrelevant key

    # Noise: extra data not tied to logic
    audit_flags = [False, True, False, True, False]
    compliance_score = sum([1 for f in audit_flags if f]) * 10  # Unused

    def calculate_rating(contribs, penalties):
        weighted_total = 0.0
        for idx, c in enumerate(contribs):
            if idx % 2 == 0:
                c *= 1.1  # Even indices get boost
            elif idx == 3:
                c *= 1.25  # Special case
            weighted_total += c
            
            # Apply penalty only if index < 5 (ignore extraneous keys)
            if idx < 5:
                weighted_total -= penalties[idx]
                
            # Red herring conditional (no effect due to structure)
            if c > 1000:
                weighted_total += 50  # Never reached

        # Normalize by number of developers
        normalized = weighted_total / len(contribs)
        return int(round(normalized))

    final_score = calculate_rating(contributions, penalty_map)
    print(f"Result: {final_score}")

    # Distractor: secondary computation with no output linkage
    phantom_score = sum(contributions) // 5 - sum(penalty_map.values()) // 6

    return final_score

# Execute and ensure deterministic output
analyze_developer_impact()