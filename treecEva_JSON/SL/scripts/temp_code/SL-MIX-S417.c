#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int mask;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* createNode(int mask) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->mask = mask;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int computeEncryptedValue(struct TreeNode* node, int* dp) {
    if (node == NULL) return 0;
    
    int left_val = computeEncryptedValue(node->left, dp);
    int right_val = computeEncryptedValue(node->right, dp);
    
    int combined = left_val ^ right_val;
    int result = node->mask ^ combined;
    
    (*dp) += result & 0xF;  // Only consider last 4 bits for DP accumulation
    
    return result;
}

int main() {
    volatile int dp_accumulator = 0;
    
    // Constructing a binary tree
    struct TreeNode* root = createNode(0b1100);
    root->left = createNode(0b1010);
    root->right = createNode(0b0110);
    root->left->left = createNode(0b1111);
    root->left->right = createNode(0b0001);
    root->right->left = createNode(0b1001);
    root->right->right = createNode(0b0101);
    
    int encrypted_root = computeEncryptedValue(root, &dp_accumulator);
    
    printf("Result: %d\n", encrypted_root);
    
    return 0;
}