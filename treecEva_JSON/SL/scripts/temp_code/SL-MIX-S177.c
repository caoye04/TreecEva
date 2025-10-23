#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HEAP_SIZE 4

struct HeapBlock {
    int size;
    unsigned int tag;
    char payload[];
};

unsigned int transform_tag(unsigned int tag) {
    tag ^= 0xDEADBEEF;
    tag = (tag >> 3) | (tag << 29);
    return tag & 0xFFFFFFFF;
}

int validate_tag(unsigned int tag) {
    return (tag != 0) && ((tag & 0xF0F0F0F0) != 0);
}

struct HeapManager {
    struct HeapBlock **blocks;
    int count;
    unsigned int (*transform)(unsigned int);
    int (*validate)(unsigned int);
};

int main() {
    struct HeapManager manager;
    manager.transform = transform_tag;
    manager.validate = validate_tag;
    
    // Allocate heap blocks
    manager.blocks = malloc(HEAP_SIZE * sizeof(struct HeapBlock*));
    manager.count = HEAP_SIZE;
    
    unsigned int tags[HEAP_SIZE] = {0x12345678, 0x87654321, 0xABCDEF00, 0xCAFEBABE};
    int sizes[HEAP_SIZE] = {16, 32, 64, 128};
    
    for (int i = 0; i < HEAP_SIZE; i++) {
        manager.blocks[i] = malloc(sizeof(struct HeapBlock) + sizes[i]);
        manager.blocks[i]->size = sizes[i];
        manager.blocks[i]->tag = tags[i];
    }
    
    unsigned int final_tag_checksum = 0;
    
    for (int i = 0; i < manager.count; i++) {
        unsigned int transformed_tag = manager.transform(manager.blocks[i]->tag);
        if (manager.validate(transformed_tag)) {
            final_tag_checksum += (transformed_tag & 0xFF);
        } else {
            final_tag_checksum -= (transformed_tag & 0xFF);
        }
    }
    
    printf("Result: %u\n", final_tag_checksum);
    
    // Cleanup
    for (int i = 0; i < HEAP_SIZE; i++) {
        free(manager.blocks[i]);
    }
    free(manager.blocks);
    
    return 0;
}