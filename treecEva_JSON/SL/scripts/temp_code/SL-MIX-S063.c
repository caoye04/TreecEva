#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX_TREES 100

struct Tree {
    int age;
    double height;
};

// Binary min-heap implementation
struct Heap {
    struct Tree* data;
    int size;
};

void push_heap(struct Heap* h, struct Tree t) {
    int i = h->size++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (h->data[parent].age <= t.age) break;
        h->data[i] = h->data[parent];
        i = parent;
    }
    h->data[i] = t;
}

struct Tree pop_heap(struct Heap* h) {
    struct Tree result = h->data[0];
    struct Tree last = h->data[--h->size];
    
    if (h->size == 0) return result;
    
    int i = 0;
    while (2*i + 1 < h->size) {
        int child = 2*i + 1;
        if (child + 1 < h->size && h->data[child].age > h->data[child+1].age)
            child++;
        if (last.age <= h->data[child].age) break;
        h->data[i] = h->data[child];
        i = child;
    }
    h->data[i] = last;
    return result;
}

volatile int update_count = 3;
double calculate_priority(struct Tree t) {
    // Priority = log(age+1) * sqrt(height) mod 100
    double base = log(t.age + 1) * sqrt(t.height);
    return fmod(base, 100.0);
}

int main() {
    struct Heap forest = { (struct Tree[MAX_TREES]){}, 0 };
    
    // Initialize forest
    struct Tree initial_trees[] = {{5, 10.5}, {12, 25.3}, {8, 15.7}, {20, 30.2}};
    for(int i=0; i<4; i++) {
        push_heap(&forest, initial_trees[i]);
    }
    
    // Process growth updates
    double total_growth = 0;
    for(volatile int u=0; u<update_count; u++) {
        struct Tree current = pop_heap(&forest);
        current.height += 1.5;
        current.age += 1;
        push_heap(&forest, current);
        total_growth += 1.5;
    }
    
    // Calculate final priority of youngest tree
    struct Tree target_tree = pop_heap(&forest);
    double final_priority = calculate_priority(target_tree);
    
    //END_CALC
    printf("Result: %.0f\n", final_priority);
    return 0;
}