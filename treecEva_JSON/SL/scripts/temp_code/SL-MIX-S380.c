#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct PermissionNode {
    unsigned int user_perm : 3;
    unsigned int group_perm : 3;
    unsigned int others_perm : 3;
    struct PermissionNode* left;
    struct PermissionNode* right;
};

struct PermissionNode* createNode(unsigned int user, unsigned int group, unsigned int others) {
    struct PermissionNode* node = (struct PermissionNode*)malloc(sizeof(struct PermissionNode));
    node->user_perm = user;
    node->group_perm = group;
    node->others_perm = others;
    node->left = NULL;
    node->right = NULL;
    return node;
}

int sumPermissions(struct PermissionNode* root) {
    if (root == NULL) return 0;
    int current = root->user_perm + root->group_perm + root->others_perm;
    return current + sumPermissions(root->left) + sumPermissions(root->right);
}

int main() {
    struct PermissionNode* root = createNode(4, 2, 1);  // r-- -w- --x
    root->left = createNode(7, 0, 5);                   // rwx --- r-x
    root->right = createNode(3, 6, 4);                  // rw- rw- r--
    root->left->left = createNode(1, 1, 1);             // --x --x --x
    root->left->right = createNode(2, 4, 3);            // -w- r-- -wx
    
    int total_permissions = sumPermissions(root);
    printf("Result: %d\n", total_permissions);
    return 0;
}