#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 5
#define MODULUS 7

typedef struct Block {
    int access_counter;
    int data_payload;
    struct Block* next;
} Block;

int transform(int x) {
    return (x * 3 + 1) % MODULUS;
}

int aggregate(Block* head, int (*func)(int)) {
    int sum = 0;
    Block* current = head;
    do {
        sum += func(current->access_counter);
        current = current->next;
    } while (current != head);
    return sum;
}

int main() {
    Block nodes[BUFFER_SIZE];
    for (int i = 0; i < BUFFER_SIZE; i++) {
        nodes[i].access_counter = (i * 2 + 3) % MODULUS;
        nodes[i].data_payload = i * 10;
        nodes[i].next = &nodes[(i + 1) % BUFFER_SIZE];
    }
    
    Block* head = &nodes[0];
    Block* ptr = head;
    int steps = 3;
    for (int i = 0; i < steps; i++) {
        ptr->access_counter = (ptr->access_counter + 5) % MODULUS;
        ptr = ptr->next;
    }
    
    int intermediate_sum = 0;
    for (int i = 0; i < BUFFER_SIZE; i++) {
        intermediate_sum += nodes[i].access_counter;
    }
    
    int final_metric = aggregate(head, transform);
    final_metric = (final_metric + intermediate_sum) % MODULUS;
    
    printf("Result: %d\n", final_metric);
    return 0;
}