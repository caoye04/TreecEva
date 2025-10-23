#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define QUEUE_SIZE 100

typedef struct TreeNode {
    int growth_factor;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

typedef struct Queue {
    TreeNode* items[QUEUE_SIZE];
    int front;
    int rear;
} Queue;

union DataPun {
    int as_int;
    float as_float;
};

void enqueue(Queue* q, TreeNode* node) {
    if (q->rear == QUEUE_SIZE - 1) return;
    if (q->front == -1) q->front = 0;
    q->rear++;
    q->items[q->rear] = node;
}

TreeNode* dequeue(Queue* q) {
    if (q->front == -1 || q->front > q->rear) return NULL;
    TreeNode* node = q->items[q->front];
    q->front++;
    if (q->front > q->rear) {
        q->front = -1;
        q->rear = -1;
    }
    return node;
}

int fibonacci_sum(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    int a = 0, b = 1, sum = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        sum += temp;
        a = b;
        b = temp;
    }
    return sum;
}

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

int combinatorial_value(int n, int k) {
    if (k > n || k < 0) return 0;
    return factorial(n) / (factorial(k) * factorial(n - k));
}

int main() {
    // Create tree nodes
    TreeNode n1 = {4, NULL, NULL};
    TreeNode n2 = {7, NULL, NULL};
    TreeNode n3 = {2, NULL, NULL};
    TreeNode n4 = {9, NULL, NULL};
    TreeNode n5 = {1, NULL, NULL};
    TreeNode n6 = {8, NULL, NULL};
    TreeNode n7 = {3, NULL, NULL};
    
    // Build tree structure
    n1.left = &n2; n1.right = &n3;
    n2.left = &n4; n2.right = &n5;
    n3.left = &n6; n3.right = &n7;
    
    Queue q = {{0}, -1, -1};
    enqueue(&q, &n1);
    
    union DataPun accumulator;
    accumulator.as_int = 0;
    int combinatorial_accumulator = 0;
    int processed_count = 0;
    
    while (q.front != -1 && processed_count < 7) {
        TreeNode* current = dequeue(&q);
        if (!current) break;
        
        processed_count++;
        
        switch (processed_count) {
            case 1:
            case 4:
            case 6:
                if (current->growth_factor % 2 == 0) {
                    accumulator.as_int += fibonacci_sum(current->growth_factor);
                } else {
                    combinatorial_accumulator += combinatorial_value(current->growth_factor, 2);
                }
                break;
            case 2:
            case 5:
                if (current->growth_factor > 5) {
                    accumulator.as_int += fibonacci_sum(current->growth_factor);
                    if (current->growth_factor == 9) {
                        break;
                    }
                } else {
                    combinatorial_accumulator += combinatorial_value(current->growth_factor, 1);
                }
                break;
            case 3:
            case 7:
                if (current->growth_factor < 5) {
                    combinatorial_accumulator += combinatorial_value(current->growth_factor, 1);
                } else {
                    accumulator.as_int += fibonacci_sum(current->growth_factor);
                }
                break;
            default:
                break;
        }
        
        if (current->left) enqueue(&q, current->left);
        if (current->right) enqueue(&q, current->right);
        
        if (processed_count == 4) {
            if (combinatorial_accumulator > 10) {
                break;
            }
        }
    }
    
    int final_metric = accumulator.as_int + combinatorial_accumulator;
    printf("Result: %d\n", final_metric);
    return 0;
}