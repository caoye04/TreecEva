#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 101

typedef struct Block {
    size_t address;
    size_t size;
    int is_free;
    struct Block* next;
} Block;

typedef struct {
    Block* buckets[HASH_SIZE];
} HashTable;

HashTable* create_table() {
    HashTable* table = malloc(sizeof(HashTable));
    for (int i = 0; i < HASH_SIZE; i++) {
        table->buckets[i] = NULL;
    }
    return table;
}

void insert_block(HashTable* table, size_t addr, size_t sz) {
    int index = addr % HASH_SIZE;
    Block* new_block = malloc(sizeof(Block));
    new_block->address = addr;
    new_block->size = sz;
    new_block->is_free = 1;
    new_block->next = table->buckets[index];
    table->buckets[index] = new_block;
}

Block* find_block(HashTable* table, size_t addr) {
    int index = addr % HASH_SIZE;
    Block* current = table->buckets[index];
    while (current && current->address != addr) {
        current = current->next;
    }
    return current;
}

size_t merge_adjacent_blocks(HashTable* table) {
    size_t max_size = 0;
    for (int i = 0; i < HASH_SIZE; i++) {
        Block* current = table->buckets[i];
        while (current) {
            if (current->is_free) {
                Block* next_block = find_block(table, current->address + current->size);
                while (next_block && next_block->is_free) {
                    current->size += next_block->size;
                    next_block->is_free = 0; // Mark as merged
                    next_block = find_block(table, current->address + current->size);
                }
                if (current->size > max_size) {
                    max_size = current->size;
                }
            }
            current = current->next;
        }
    }
    return max_size;
}

int main() {
    HashTable* mem_table = create_table();
    
    // Simulate allocations and deallocations
    insert_block(mem_table, 1000, 256);
    insert_block(mem_table, 1256, 128);
    insert_block(mem_table, 1384, 64);
    insert_block(mem_table, 2000, 512);
    insert_block(mem_table, 2512, 256);
    
    // Mark some blocks as free to enable merging
    Block* b1 = find_block(mem_table, 1000);
    Block* b2 = find_block(mem_table, 1256);
    Block* b3 = find_block(mem_table, 1384);
    if (b1 && b2 && b3) {
        b1->is_free = 1;
        b2->is_free = 1;
        b3->is_free = 1;
    }
    
    size_t largest_merged = merge_adjacent_blocks(mem_table);
    printf("Result: %zu\n", largest_merged);
    
    return 0;
}