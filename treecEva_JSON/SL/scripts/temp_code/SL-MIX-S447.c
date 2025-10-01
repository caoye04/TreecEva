#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_NODES 5

struct Node {
    int value;
    struct Node* next;
};

struct DataContainer {
    int array[3][3];
    struct Node* head;
    char buffer[64];
};

int compute_checksum(struct DataContainer* dc) {
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum += dc->array[i][j] * (i + 1) * (j + 1);
        }
    }
    struct Node* current = dc->head;
    while (current != NULL) {
        sum ^= current->value;
        current = current->next;
    }
    return sum;
}

int main() {
    struct DataContainer container;
    memset(&container, 0, sizeof(container));

    // Initialize array with computed values
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            container.array[i][j] = (int)(pow(i + 1, j + 1) + sin(M_PI * i / 4));
        }
    }

    // Create linked list with dynamic values
    struct Node nodes[3];
    for (int i = 0; i < 3; i++) {
        nodes[i].value = (i + 1) << (2 + i);
        nodes[i].next = (i < 2) ? &nodes[i + 1] : NULL;
    }
    container.head = &nodes[0];

    // Process string with mathematical transformation
    char base_str[] = "ComplexEvaluation";
    int len = strlen(base_str);
    for (int i = 0; i < len; i++) {
        container.buffer[i] = base_str[i] ^ (i % 8);
    }
    container.buffer[len] = '\0';

    // Perform final computation
    int checksum = compute_checksum(&container);
    int final_xor = 0;
    for (int i = 0; i < len; i++) {
        final_xor ^= container.buffer[i];
    }
    int result = (checksum & 0xFF) | ((final_xor & 0xFF) << 8);
    result = result ^ (int)sqrt(result);

    printf("Result: %d\n", result);
    return 0;
}