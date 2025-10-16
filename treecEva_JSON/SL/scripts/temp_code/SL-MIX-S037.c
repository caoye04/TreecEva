#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct TreeNode {
    int allocation_size;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

TreeNode* createNode(int size) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->allocation_size = size;
    node->left = NULL;
    node->right = NULL;
    return node;
}

void insertNode(TreeNode* root, int size) {
    TreeNode** current = &root;
    while (*current != NULL) {
        current = (size < (*current)->allocation_size) ? &(*current)->left : &(*current)->right;
    }
    *current = createNode(size);
}

int main() {
    TreeNode* root = createNode(128);
    insertNode(root, 64);
    insertNode(root, 256);
    insertNode(root, 32);
    insertNode(root, 96);
    insertNode(root, 192);
    insertNode(root, 512);
    
    int target_result = root->right->allocation_size;
    printf("Target result: %d\n", target_result);
    
    return 0;
}