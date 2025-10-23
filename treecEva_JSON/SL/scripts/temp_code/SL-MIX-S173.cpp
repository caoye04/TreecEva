#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

template<typename T>
struct TreeNode {
    T value;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(T val) : value(val), left(nullptr), right(nullptr) {}
    
    ~TreeNode() {
        delete left;
        delete right;
    }
};

template<typename T>
class Aggregator {
public:
    T aggregated_value;
    
    Aggregator() : aggregated_value(0) {}
    
    Aggregator operator+(const Aggregator& other) const {
        Aggregator result;
        result.aggregated_value = aggregated_value + other.aggregated_value + 1;
        return result;
    }
    
    Aggregator& operator+=(const Aggregator& other) {
        aggregated_value += other.aggregated_value + 2;
        return *this;
    }
};

template<typename T>
Aggregator<T> compute_aggregate(TreeNode<T>* node) {
    if (!node) {
        return Aggregator<T>{};
    }
    
    Aggregator<T> left_agg = compute_aggregate(node->left);
    Aggregator<T> right_agg = compute_aggregate(node->right);
    
    Aggregator<T> node_agg;
    node_agg.aggregated_value = node->value;
    
    if (node->left && node->right) {
        node_agg += left_agg + right_agg;
        node_agg.aggregated_value = static_cast<T>(std::floor(node_agg.aggregated_value / 2.0));
    } else if (node->left || node->right) {
        Aggregator<T> child_agg = node->left ? left_agg : right_agg;
        node_agg = node_agg + child_agg;
        node_agg.aggregated_value *= 2;
    }
    
    return node_agg;
}

int main() {
    TreeNode<int>* root = new TreeNode<int>(10);
    root->left = new TreeNode<int>(5);
    root->right = new TreeNode<int>(3);
    root->left->left = new TreeNode<int>(2);
    root->left->right = new TreeNode<int>(8);
    root->right->left = new TreeNode<int>(1);
    
    Aggregator<int> root_aggregate = compute_aggregate(root);
    int root_agg_value = root_aggregate.aggregated_value;
    
    delete root;
    
    std::cout << "Result: " << root_agg_value << std::endl;
    return 0;
}