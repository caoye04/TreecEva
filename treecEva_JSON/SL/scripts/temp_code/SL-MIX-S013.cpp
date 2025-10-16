#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>

struct GrowthNode {
    int growthFactor;
    GrowthNode* left;
    GrowthNode* right;
    
    GrowthNode(int factor) : growthFactor(factor), left(nullptr), right(nullptr) {}
    
    ~GrowthNode() {
        delete left;
        delete right;
    }
};

class GrowthSimulator {
private:
    int cumulativeGrowth;
    
public:
    GrowthSimulator() : cumulativeGrowth(0) {}
    
    void processNode(GrowthNode* node) {
        if (!node) return;
        
        int factor = node->growthFactor;
        int adjustment = 0;
        
        switch (factor % 5) {
            case 0:
                adjustment = factor * 2;
                break;
            case 1:
                adjustment = static_cast<int>(std::pow(factor, 2));
                break;
            case 2:
                adjustment = factor & 0x0F; // Bitwise AND with 15
                break;
            case 3:
                adjustment = factor << 1; // Left shift by 1
                break;
            case 4:
                adjustment = ~factor & 0xFF; // Bitwise NOT then AND with 255
                break;
            default:
                adjustment = 0;
        }
        
        if (adjustment > 20) {
            cumulativeGrowth += adjustment;
        } else {
            cumulativeGrowth -= (adjustment >> 1); // Right shift by 1
        }
        
        processNode(node->left);
        processNode(node->right);
    }
    
    int getCumulativeGrowth() const { return cumulativeGrowth; }
};

int main() {
    // Creating a binary tree representing plant growth factors
    GrowthNode* root = new GrowthNode(7);
    root->left = new GrowthNode(3);
    root->right = new GrowthNode(12);
    root->left->left = new GrowthNode(5);
    root->left->right = new GrowthNode(9);
    root->right->left = new GrowthNode(15);
    root->right->right = new GrowthNode(2);
    
    GrowthSimulator simulator;
    simulator.processNode(root);
    
    std::cout << "Result: " << simulator.getCumulativeGrowth() << std::endl;
    
    delete root;
    return 0;
}