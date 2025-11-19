import re
import statistics

class DocumentNode:
    def __init__(self, content, next_node=None):
        self.content = content
        self.next = next_node

def extract_semantic_terms(text):
    pattern = r'\b[a-zA-Z]{4,}\b'
    return set(re.findall(pattern, text))

def calculate_cluster_density(term_set):
    if not term_set:
        return 0
    return sum(hash(term) % 100 for term in term_set) / len(term_set)

documents_head = DocumentNode('Machine learning algorithms optimize performance')
documents_head.next = DocumentNode('Deep neural networks process complex data structures')
documents_head.next.next = DocumentNode('Natural language processing enables text understanding')

term_clusters = []
current = documents_head
while current:
    terms = extract_semantic_terms(current.content)
    term_clusters.append(terms)
    current = current.next

common_terms = frozenset(term_clusters[0])
for cluster in term_clusters[1:]:
    common_terms = common_terms & frozenset(cluster)

with open('temp_analysis.txt', 'w') as f:
    f.write(str(common_terms))

cluster_densities = []
for cluster in term_clusters:
    density = calculate_cluster_density(cluster)
    cluster_densities.append(density)

harmonic_mean_lambda = lambda vals: len(vals) / sum(1/v if v != 0 else 0 for v in vals)
final_metric = harmonic_mean_lambda(cluster_densities)

print(f'Result: {int(final_metric)}')