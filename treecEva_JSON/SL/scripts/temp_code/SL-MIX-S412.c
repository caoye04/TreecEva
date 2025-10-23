#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define EVEN_PARITY(x) ((__builtin_popcount(x) % 2) == 0)

struct ComponentState {
    unsigned int active : 1;
    unsigned int powered : 1;
    unsigned int error : 1;
    unsigned int reserved : 5;
};

union SignalData {
    struct ComponentState bits;
    unsigned char raw;
};

struct TreeNode {
    union SignalData data;
    struct TreeNode* left;
    struct TreeNode* right;
};

unsigned int factorial(unsigned int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

// C(6,2) = 6!/(2!*(6-2)!) = 15
unsigned int combinations_6_2() {
    return factorial(6) / (factorial(2) * factorial(4));
}

// P(5,3) = 5!/(5-3)! = 60
unsigned int permutations_5_3() {
    return factorial(5) / factorial(2);
}

struct TreeNode* create_node(unsigned char value) {
    struct TreeNode* node = malloc(sizeof(struct TreeNode));
    node->data.raw = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int main() {
    // Create a complete binary tree of depth 3
    struct TreeNode* root = create_node(0);
    root->left = create_node(0b00000101);  // 5
    root->right = create_node(0b00000011); // 3
    root->left->left = create_node(0b00000110);  // 6
    root->left->right = create_node(0b00000001); // 1
    root->right->left = create_node(0b00000100); // 4
    root->right->right = create_node(0b00000010); // 2
    
    // Propagate signals up the tree using XOR
    root->left->data.raw = root->left->left->data.raw ^ root->left->right->data.raw;
    root->right->data.raw = root->right->left->data.raw ^ root->right->right->data.raw;
    root->data.raw = root->left->data.raw ^ root->right->data.raw;
    
    // Count combinations/permutations based on root parity
    int propagation_result = EVEN_PARITY(root->data.raw) ? combinations_6_2() : permutations_5_3();
    
    // Clean up memory
    free(root->left->left);
    free(root->left->right);
    free(root->right->left);
    free(root->right->right);
    free(root->left);
    free(root->right);
    free(root);
    
    printf("Result: %d\n", propagation_result);
    return 0;
}