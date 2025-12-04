from itertools import combinations

# Analyze voting patterns in a small committee
committee_members = ['Alice', 'Bob', 'Charlie', 'Diana']
voting_records = {
    'Alice': {'proposal_a': True, 'proposal_b': False},
    'Bob': {'proposal_a': True, 'proposal_b': True},
    'Charlie': {'proposal_a': False, 'proposal_b': False},
    'Diana': {'proposal_a': True, 'proposal_b': True}
}

# Count unanimous voting pairs
pair_count = 0
for member1, member2 in combinations(committee_members, 2):
    votes1 = voting_records[member1]
    votes2 = voting_records[member2]
    
    # Check if both members voted the same on all proposals
    agreement_count = 0
    for proposal in ['proposal_a', 'proposal_b']:
        if votes1[proposal] == votes2[proposal]:
            agreement_count += 1
    
    if agreement_count == 2:
        pair_count += 1

# Final calculation
final_count = pair_count * 3
result = final_count
print(f"Result: {result}")