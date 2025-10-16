#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct CommandNode {
    char direction;
    int distance;
    struct CommandNode* left;
    struct CommandNode* right;
};

int position_offsets[2] = {0, 0}; // x, y

void process_command(char dir, int dist) {
    if (dir == 'N') position_offsets[1] += dist;
    else if (dir == 'S') position_offsets[1] -= dist;
    else if (dir == 'E') position_offsets[0] += dist;
    else if (dir == 'W') position_offsets[0] -= dist;
}

void inorder_traverse(struct CommandNode* root) {
    if (root != NULL) {
        inorder_traverse(root->left);
        // Short-circuit: only process if distance > 0 AND direction is valid
        if (root->distance > 0 && (root->direction == 'N' || root->direction == 'S' || root->direction == 'E' || root->direction == 'W')) {
            process_command(root->direction, root->distance);
        }
        inorder_traverse(root->right);
    }
}

int main() {
    // Building command tree:
    //       E(3)
    //      /    \
    //    N(2)   W(4)
    //   /      /    \
    // S(1)   N(5)   S(0)  <-- S(0) should be skipped due to short-circuit
    
    struct CommandNode* root = malloc(sizeof(struct CommandNode));
    root->direction = 'E';
    root->distance = 3;
    
    root->left = malloc(sizeof(struct CommandNode));
    root->left->direction = 'N';
    root->left->distance = 2;
    
    root->right = malloc(sizeof(struct CommandNode));
    root->right->direction = 'W';
    root->right->distance = 4;
    
    root->left->left = malloc(sizeof(struct CommandNode));
    root->left->left->direction = 'S';
    root->left->left->distance = 1;
    root->left->left->left = NULL;
    root->left->left->right = NULL;
    
    root->left->right = NULL;
    
    root->right->left = malloc(sizeof(struct CommandNode));
    root->right->left->direction = 'N';
    root->right->left->distance = 5;
    root->right->left->left = NULL;
    root->right->left->right = NULL;
    
    root->right->right = malloc(sizeof(struct CommandNode));
    root->right->right->direction = 'S';
    root->right->right->distance = 0; // This node will be skipped
    root->right->right->left = NULL;
    root->right->right->right = NULL;
    
    root->left->left->left = NULL;
    root->left->left->right = NULL;
    
    inorder_traverse(root);
    
    // Calculate Manhattan distance using pointer arithmetic
    int* ptr = position_offsets;
    int final_distance = abs(*ptr) + abs(*(ptr + 1));
    
    printf("Result: %d\n", final_distance);
    
    // Free allocated memory
    free(root->right->right);
    free(root->right->left);
    free(root->right);
    free(root->left->left);
    free(root->left);
    free(root);
    
    return 0;
}