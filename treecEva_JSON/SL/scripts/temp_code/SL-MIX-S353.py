from collections import defaultdict, deque
from itertools import combinations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def tokenize(doc):
    return [word.strip('.,!?;') for word in doc.lower().split()]

def remove_stopwords(tokens, stops):
    return [t for t in tokens if t not in stops]

def stem_tokens(tokens):
    # Simple stemming: remove common suffixes
    stemmed = []
    for t in tokens:
        if t.endswith('ing'):
            stemmed.append(t[:-3])
        elif t.endswith('ed'):
            stemmed.append(t[:-2])
        else:
            stemmed.append(t)
    return stemmed

def build_cooccurrence(tokens, window=3):
    cooccur = defaultdict(int)
    for i in range(len(tokens)):
        for j in range(i+1, min(i+window+1, len(tokens))):
            pair = tuple(sorted([tokens[i], tokens[j]]))
            cooccur[pair] += 1
    return cooccur

def cluster_recursive(cooccur_map, min_freq):
    filtered_pairs = {p for p, f in cooccur_map.items() if f > min_freq}
    if not filtered_pairs:
        return []
    
    # Build adjacency list
    adj = defaultdict(set)
    for a, b in filtered_pairs:
        adj[a].add(b)
        adj[b].add(a)
    
    visited = set()
    clusters = []
    
    def dfs(node, cluster):
        visited.add(node)
        cluster.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor, cluster)
    
    for node in adj:
        if node not in visited:
            cluster = set()
            dfs(node, cluster)
            clusters.append(cluster)
    
    return clusters

doc1 = "The runner was running swiftly through the forest."
doc2 = "He had painted the running track with bright colors."
doc3 = "The painting depicted a swift river running through the woods."

stop_words = frozenset(['the', 'was', 'with', 'a', 'through'])

tokenized_docs = [tokenize(doc) for doc in [doc1, doc2, doc3]]
filtered_docs = [remove_stopwords(tokens, stop_words) for tokens in tokenized_docs]
stemmed_docs = [stem_tokens(tokens) for tokens in filtered_docs]

# Flatten all tokens
all_tokens = [token for doc in stemmed_docs for token in doc]

cooccur_map = build_cooccurrence(all_tokens)
clusters = cluster_recursive(cooccur_map, 2)
total_clusters = len(clusters)

print(f"Result: {total_clusters}")