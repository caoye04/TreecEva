#define _USE_MATH_DEFINES
#include <iostream>
#include <optional>

template<typename T>
struct TreeNode {
    T data;
    std::optional<TreeNode<T>> left;
    std::optional<TreeNode<T>> right;
    
    constexpr TreeNode(T val) : data(val) {}
};

template<typename T>
class BotanicalSimulator {
public:
    constexpr static int MOD = 1000000007;
    
    constexpr static T calculateVitality(const TreeNode<T>& node) {
        T current = node.data % MOD;
        T leftContribution = 0;
        T rightContribution = 0;
        
        if (node.left.has_value()) {
            leftContribution = calculateVitality(node.left.value());
        }
        
        if (node.right.has_value()) {
            rightContribution = calculateVitality(node.right.value());
        }
        
        return (current + leftContribution + rightContribution) % MOD;
    }
};

constexpr int growthFactor1 = 8421;
constexpr int growthFactor2 = 1975;
constexpr int growthFactor3 = 3301;

int main() {
    // Constructing the botanical growth tree
    TreeNode<int> root(growthFactor1);
    root.left = TreeNode<int>(growthFactor2);
    root.right = TreeNode<int>(growthFactor3);
    
    // Adding sub-branches
    root.left.value().left = TreeNode<int>(1111);
    root.left.value().right = TreeNode<int>(2222);
    root.right.value().left = TreeNode<int>(3333);
    
    // Calculating the vitality score
    int vitalityScore = BotanicalSimulator<int>::calculateVitality(root);
    
    std::cout << "Result: " << vitalityScore << std::endl;
    return 0;
}