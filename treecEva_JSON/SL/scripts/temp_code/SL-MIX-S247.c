#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct mem_block {
    int size;
    int status; // 0 = free, 1 = allocated
    struct mem_block* next;
    struct mem_block* prev;
};

volatile int op_counter = 0;

void insert_block(struct mem_block** head, int size) {
    struct mem_block* new_block = (struct mem_block*)malloc(sizeof(struct mem_block));
    new_block->size = size;
    new_block->status = 0;
    new_block->next = *head;
    new_block->prev = NULL;
    if (*head != NULL) (*head)->prev = new_block;
    *head = new_block;
}

int count_free_blocks(struct mem_block* head) {
    int count = 0;
    while (head != NULL) {
        if (head->status == 0) count++;
        head = head->next;
    }
    return count;
}

int main() {
    struct mem_block* head = NULL;
    
    // Initialize free list
    insert_block(&head, 64);
    insert_block(&head, 32);
    insert_block(&head, 128);
    insert_block(&head, 16);
    
    int request_size = 40;
    struct mem_block* current = head;
    int final_block_count = 0;
    
    while (current != NULL) {
        op_counter++;
        int action = (current->size ^ request_size) & 0x3; // Bitwise XOR and mask
        
        switch(action) {
            case 0: // Exact fit
                current->status = 1;
                break;
            case 1: // Split required
                if (current->size > request_size + 16) {
                    struct mem_block* new_block = (struct mem_block*)malloc(sizeof(struct mem_block));
                    new_block->size = current->size - request_size;
                    new_block->status = 0;
                    new_block->next = current->next;
                    new_block->prev = current;
                    if (current->next) current->next->prev = new_block;
                    current->next = new_block;
                    current->size = request_size;
                    current->status = 1;
                }
                break;
            case 2: // Merge with next if both free
                if (current->next && current->next->status == 0 && current->status == 0) {
                    current->size += current->next->size;
                    struct mem_block* temp = current->next;
                    current->next = temp->next;
                    if (temp->next) temp->next->prev = current;
                    free(temp);
                }
                break;
            default: // No operation
                break;
        }
        
        current = current->next;
    }
    
    final_block_count = count_free_blocks(head);
    printf("Result: %d\n", final_block_count);
    
    // Cleanup
    while (head != NULL) {
        struct mem_block* temp = head;
        head = head->next;
        free(temp);
    }
    
    return 0;
}