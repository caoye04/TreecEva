#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

typedef struct BlockNode {
    size_t address;
    size_t size;
    unsigned int checksum;
    struct BlockNode* next;
} BlockNode;

union MemoryInspector {
    size_t address_value;
    unsigned char bytes[sizeof(size_t)];
};

volatile int checksum_errors = 0;

unsigned int compute_checksum(size_t addr, size_t sz) {
    union MemoryInspector inspector;
    inspector.address_value = addr;
    unsigned int sum = 0;
    for (int i = 0; i < sizeof(size_t); i++) {
        sum += inspector.bytes[i];
    }
    return (sum ^ (unsigned int)(sz >> 3)) & 0xFFFF;
}

int audit_blocks(BlockNode* node) {
    if (node == NULL) return 0;
    unsigned int expected = compute_checksum(node->address, node->size);
    if (node->checksum != expected) {
        checksum_errors++;
    }
    return audit_blocks(node->next) + (node->checksum == expected ? 1 : 0);
}

int main() {
    BlockNode n3 = {0x7fff8000, 2048, 0, NULL};
    n3.checksum = compute_checksum(n3.address, n3.size);
    
    BlockNode n2 = {0x7fff4000, 1024, 0, &n3};
    n2.checksum = compute_checksum(n2.address, n2.size) ^ 0x1;
    
    BlockNode n1 = {0x7fff0000, 512, 0, &n2};
    n1.checksum = compute_checksum(n1.address, n1.size);
    
    audit_blocks(&n1);
    printf("Result: %d\n", checksum_errors);
    return 0;
}