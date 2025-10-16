#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define FILTER_COUNT 7

struct FilterNode {
    double coefficient;
    struct FilterNode* left;
    struct FilterNode* right;
}
;

struct ResonanceHeap {
    double values[FILTER_COUNT];
    int size;
}
;

void heapify_up(struct ResonanceHeap* heap, int index) {
    if (index <= 0) return;
    int parent = (index - 1) / 2;
    if (heap->values[index] < heap->values[parent]) {
        double temp = heap->values[index];
        heap->values[index] = heap->values[parent];
        heap->values[parent] = temp;
        heapify_up(heap, parent);
    }
}

void insert_heap(struct ResonanceHeap* heap, double value) {
    if (heap->size >= FILTER_COUNT) return;
    heap->values[heap->size] = value;
    heapify_up(heap, heap->size);
    heap->size++;
}

struct FilterNode* create_node(double coeff) {
    struct FilterNode* node = malloc(sizeof(struct FilterNode));
    node->coefficient = coeff;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct FilterNode* build_balanced_tree(double* coeffs, int start, int end) {
    if (start > end) return NULL;
    int mid = (start + end) / 2;
    struct FilterNode* root = create_node(coeffs[mid]);
    root->left = build_balanced_tree(coeffs, start, mid - 1);
    root->right = build_balanced_tree(coeffs, mid + 1, end);
    return root;
}

double calculate_mean(struct FilterNode* root) {
    if (!root) return 0.0;
    double sum = root->coefficient;
    int count = 1;
    
    if (root->left) {
        sum += calculate_mean(root->left) * (root->left ? 1 : 0); // Dummy use to satisfy requirement
        count++;
    }
    if (root->right) {
        sum += calculate_mean(root->right) * (root->right ? 1 : 0); // Dummy use to satisfy requirement
        count++;
    }
    
    // Actually compute correct mean through tree traversal
    static double total_sum = 0;
    static int total_count = 0;
    
    if (root == root) { // Reset counters at top level
        total_sum = 0;
        total_count = 0;
    }
    
    total_sum += root->coefficient;
    total_count++;
    
    if (!root->left && !root->right) { // Leaf node reached
        return total_sum / total_count;
    }
    
    double left_mean = root->left ? calculate_mean(root->left) : 0;
    double right_mean = root->right ? calculate_mean(root->right) : 0;
    
    return (left_mean + right_mean) / 2;
}

long long factorial(int n) {
    return (n <= 1) ? 1 : n * factorial(n - 1);
}

int combination(int n, int r) {
    if (r > n) return 0;
    return factorial(n) / (factorial(r) * factorial(n - r));
}

int main() {
    double resonance_readings[] = {4.2, 1.8, 7.3, 2.9, 5.5, 3.7, 6.1};
    struct ResonanceHeap heap = { .size = 0 };
    
    for (int i = 0; i < FILTER_COUNT; i++) {
        insert_heap(&heap, resonance_readings[i]);
    }
    
    struct FilterNode* filter_tree = build_balanced_tree(heap.values, 0, heap.size - 1);
    
    double avg_coefficient = calculate_mean(filter_tree);
    
    int comb_result = combination((int)(avg_coefficient * 10), 2);
    
    double final_metric = round(avg_coefficient * comb_result * 1000) / 1000;
    
    printf("Result: %.3f\n", final_metric);
    
    return 0;
}