#define _USE_MATH_DEFINES
#include <iostream>
#include <memory>
#include <string>
#include <functional>

class TaxonNode {
public:
    std::string name;
    std::shared_ptr<TaxonNode> left;
    std::shared_ptr<TaxonNode> right;
    
    TaxonNode(const std::string& n) : name(n) {}
};

// String hashing lambda using polynomial rolling hash
auto hash_taxon = [](const std::string& s, int base = 31, int mod = 1000000007) {
    long long hash = 0;
    for (char c : s) {
        hash = (hash * base + c) % mod;
    }
    return static_cast<int>(hash);
};

int main() {
    // Constructing a binary taxonomic tree
    auto root = std::make_shared<TaxonNode>("Plantae");
    root->left = std::make_shared<TaxonNode>("Angiosperms");
    root->right = std::make_shared<TaxonNode>("Gymnosperms");
    root->left->left = std::make_shared<TaxonNode>("Eudicots");
    root->left->right = std::make_shared<TaxonNode>("Monocots");
    
    // Hash accumulation using post-order traversal logic
    std::function<int(std::shared_ptr<TaxonNode>)> compute_subtree_hash = 
        [&compute_subtree_hash, &hash_taxon](std::shared_ptr<TaxonNode> node) -> int {
        if (!node) return 0;
        int left_hash = compute_subtree_hash(node->left);
        int right_hash = compute_subtree_hash(node->right);
        int node_hash = hash_taxon(node->name);
        return (left_hash ^ right_hash ^ node_hash) & 0xFFFFFFF;  // Combine with XOR and mask
    };
    
    int final_hash = compute_subtree_hash(root);
    std::cout << "Result: " << final_hash << std::endl;
    return 0;
}