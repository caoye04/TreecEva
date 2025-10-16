class PaperNode:
    def __init__(self, paper_id):
        self.paper_id = paper_id
        self.citations = []
        self.next = None
    
    def add_citation(self, cited_paper):
        self.citations.append(cited_paper)

def build_citation_chain(papers_dict):
    keys = list(papers_dict.keys())
    for i in range(len(keys)-1):
        papers_dict[keys[i]].next = papers_dict[keys[i+1]]
    return papers_dict[keys[0]]

def compute_influence_scores(head_paper):
    visited = set()
    scores = {p: 0.0 for p in ['A', 'B', 'C', 'D', 'E']}
    current = head_paper
    
    while current:
        if current.paper_id not in visited:
            visited.add(current.paper_id)
            base_score = len(current.citations) * 1.5
            scores[current.paper_id] += base_score
            
            # Greedy selection: boost score if citing influential papers
            for cited in current.citations:
                if cited.paper_id in visited:
                    scores[current.paper_id] += scores[cited.paper_id] * 0.1
        
        current = current.next
    
    # Final adjustment using set operations
    high_impact_papers = {p for p, s in scores.items() if s > 3.0}
    adjustment_set = frozenset(['B', 'D'])
    intersection = high_impact_papers & adjustment_set
    
    for p in intersection:
        scores[p] += 2.0
    
    return sum(scores.values())

# Setup papers
papers = {
    'A': PaperNode('A'),
    'B': PaperNode('B'),
    'C': PaperNode('C'),
    'D': PaperNode('D'),
    'E': PaperNode('E')
}

# Define citations
papers['A'].add_citation(papers['B'])
papers['A'].add_citation(papers['C'])
papers['B'].add_citation(papers['D'])
papers['C'].add_citation(papers['E'])
papers['D'].add_citation(papers['A'])

# Build chain and compute scores
head = build_citation_chain(papers)
influence_score = compute_influence_scores(head)
print(f"Result: {influence_score}")