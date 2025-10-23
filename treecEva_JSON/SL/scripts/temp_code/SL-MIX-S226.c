#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int leaves;
    struct Node* left;
    struct Node* right;
} Node;

Node* create_node(int leaves) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->leaves = leaves;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int main() {
    // Create a simple binary tree
    Node* root = create_node(5);
    root->left = create_node(3);
    root->right = create_node(2);
    root->left->left = create_node(1);
    root->left->right = create_node(4);
    
    int total_leaves = 0;
    Node* nodes[10];
    int count = 0;
    
    // Add nodes to array for processing
    nodes[count++] = root;
    nodes[count++] = root->left;
    nodes[count++] = root->right;
    nodes[count++] = root->left->left;
    nodes[count++] = root->left->right;
    
    // Process each node using switch
    for (int i = 0; i < count; i++) {
        Node* current = nodes[i];
        switch (current->leaves) {
            case 1:
                total_leaves += 1;
                break;
            case 2:
                total_leaves += 2;
                break;
            case 3:
                total_leaves += 3;
                break;
            case 4:
                total_leaves += 4;
                break;
            case 5:
                total_leaves += 5;
                break;
            default:
                total_leaves += 0;
        }
    }
    
    printf("Result: %d\n", total_leaves);
    
    // Free allocated memory
    for (int i = 0; i < count; i++) {
        free(nodes[i]);
    }
    
    return 0;
}