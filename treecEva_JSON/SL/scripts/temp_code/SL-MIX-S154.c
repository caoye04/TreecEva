#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct Node {
    double amplitude;
    struct Node* next;
} Node;

int main() {
    // Create linked list: 100 -> 1000 -> 10000 -> 100000
    Node* head = (Node*)malloc(sizeof(Node));
    head->amplitude = 100.0;
    head->next = (Node*)malloc(sizeof(Node));
    head->next->amplitude = 1000.0;
    head->next->next = (Node*)malloc(sizeof(Node));
    head->next->next->amplitude = 10000.0;
    head->next->next->next = (Node*)malloc(sizeof(Node));
    head->next->next->next->amplitude = 100000.0;
    head->next->next->next->next = NULL;
    
    Node* current = head;
    double processed_amplitude = 0.0;
    int position = 0;
    
    while (current != NULL && position < 3) {
        // Logarithmic transformation: log10(amplitude)
        double log_value = log10(current->amplitude);
        
        // Exponential adjustment: e^(log_value/2)
        processed_amplitude = exp(log_value/2.0);
        
        current = current->next;
        position++;
    }
    
    printf("Result: %.2f\n", processed_amplitude);
    
    // Free allocated memory
    current = head;
    while (current != NULL) {
        Node* temp = current;
        current = current->next;
        free(temp);
    }
    
    return 0;
}