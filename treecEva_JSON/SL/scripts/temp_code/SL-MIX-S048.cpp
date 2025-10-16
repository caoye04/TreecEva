#define _USE_MATH_DEFINES
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class RoboticArmController {
private:
    std::stack<int> operation_codes;
    std::queue<int> positional_adjustments;
    TreeNode* operation_history;
    int completed_operations;
    
    void insert_operation(int op) {
        TreeNode** current = &operation_history;
        while (*current) {
            if (op < (*current)->val)
                current = &(*current)->left;
            else
                current = &(*current)->right;
        }
        *current = new TreeNode(op);
    }
    
public:
    RoboticArmController() : operation_history(nullptr), completed_operations(0) {}
    
    ~RoboticArmController() {
        std::vector<TreeNode*> nodes;
        nodes.push_back(operation_history);
        while (!nodes.empty()) {
            TreeNode* node = nodes.back();
            nodes.pop_back();
            if (node) {
                nodes.push_back(node->left);
                nodes.push_back(node->right);
                delete node;
            }
        }
    }
    
    void load_operations(const std::vector<int>& ops) {
        for (int op : ops) {
            operation_codes.push(op);
        }
    }
    
    void load_adjustments(const std::vector<int>& adj) {
        for (int a : adj) {
            positional_adjustments.push(a);
        }
    }
    
    void process() {
        while (!operation_codes.empty() || !positional_adjustments.empty()) {
            // Greedy: prioritize operation codes (1, 2, 3) over adjustments
            if (!operation_codes.empty()) {
                int op = operation_codes.top();
                operation_codes.pop();
                
                // State machine logic
                switch (op) {
                    case 1: // Move
                        if (!positional_adjustments.empty()) {
                            positional_adjustments.pop();
                        }
                        completed_operations += 2;
                        insert_operation(op);
                        break;
                    case 2: // Grab
                        completed_operations += 3;
                        insert_operation(op);
                        break;
                    case 3: // Release
                        completed_operations += 1;
                        insert_operation(op);
                        break;
                }
            } else {
                // Process remaining adjustments
                positional_adjustments.pop();
                completed_operations += 1;
            }
        }
    }
    
    int get_completed_operations() const {
        return completed_operations;
    }
};

int main() {
    RoboticArmController controller;
    
    // Load operation codes: 1 (move), 2 (grab), 3 (release)
    std::vector<int> ops = {1, 3, 2, 1, 2, 3, 1};
    controller.load_operations(ops);
    
    // Load positional adjustments
    std::vector<int> adj = {10, 20, 30, 40, 50};
    controller.load_adjustments(adj);
    
    // Process all operations
    controller.process();
    
    // Output the result
    std::cout << "Result: " << controller.get_completed_operations() << std::endl;
    
    return 0;
}