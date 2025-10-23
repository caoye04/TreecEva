#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct Transaction {
    int id;
    int amount;
    struct Transaction* left;
    struct Transaction* right;
} Transaction;

typedef struct StackNode {
    int value;
    struct StackNode* next;
} StackNode;

Transaction* insert_transaction(Transaction* root, int id, int amount) {
    if (root == NULL) {
        Transaction* new_transaction = (Transaction*)malloc(sizeof(Transaction));
        new_transaction->id = id;
        new_transaction->amount = amount;
        new_transaction->left = NULL;
        new_transaction->right = NULL;
        return new_transaction;
    }
    
    if (id < root->id) {
        root->left = insert_transaction(root->left, id, amount);
    } else {
        root->right = insert_transaction(root->right, id, amount);
    }
    return root;
}

void push(StackNode** stack, int value) {
    StackNode* new_node = (StackNode*)malloc(sizeof(StackNode));
    new_node->value = value;
    new_node->next = *stack;
    *stack = new_node;
}

int pop(StackNode** stack) {
    if (*stack == NULL) return 0;
    StackNode* temp = *stack;
    int value = temp->value;
    *stack = (*stack)->next;
    free(temp);
    return value;
}

int account_balance = 1000;

int process_transaction(Transaction* root, int target_id, StackNode** rollback_stack) {
    if (root == NULL) return 0;
    
    switch (root->id) {
        case 5:
            if (account_balance < 500) {
                return -1;
            }
            break;
        case 15:
            if (account_balance > 2000) {
                push(rollback_stack, account_balance);
                account_balance -= 300;
                return 1;
            }
            break;
        default:
            break;
    }
    
    push(rollback_stack, account_balance);
    account_balance += root->amount;
    
    if (root->id == target_id) {
        return 1;
    }
    
    if (target_id < root->id) {
        return process_transaction(root->left, target_id, rollback_stack);
    } else {
        return process_transaction(root->right, target_id, rollback_stack);
    }
}

int main() {
    Transaction* root = NULL;
    StackNode* rollback_stack = NULL;
    
    // Build transaction tree
    root = insert_transaction(root, 10, 200);
    root = insert_transaction(root, 5, -100);
    root = insert_transaction(root, 15, 300);
    root = insert_transaction(root, 3, -50);
    root = insert_transaction(root, 7, 150);
    root = insert_transaction(root, 12, -200);
    root = insert_transaction(root, 18, 400);
    
    // Process transactions with rollbacks
    process_transaction(root, 15, &rollback_stack);
    
    // Greedy rollback of last 3 transactions
    for (int i = 0; i < 3; i++) {
        account_balance = pop(&rollback_stack);
    }
    
    // Apply final adjustment
    if (account_balance > 1200) {
        account_balance -= 100;
    } else {
        account_balance += 50;
    }
    
    printf("Result: %d\n", account_balance);
    return 0;
}