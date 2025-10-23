#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>

struct TelemetryNode {
    int temperature;
    struct TelemetryNode* next;
};

int main() {
    struct TelemetryNode* head = NULL;
    struct TelemetryNode* second = NULL;
    struct TelemetryNode* third = NULL;
    
    head = (struct TelemetryNode*)malloc(sizeof(struct TelemetryNode));
    second = (struct TelemetryNode*)malloc(sizeof(struct TelemetryNode));
    third = (struct TelemetryNode*)malloc(sizeof(struct TelemetryNode));
    
    head->temperature = 20;
    head->next = second;
    
    second->temperature = 25;
    second->next = third;
    
    third->temperature = 30;
    third->next = NULL;
    
    int sum = 0;
    int count = 0;
    struct TelemetryNode* current = head;
    
    while (current != NULL) {
        sum += current->temperature;
        count++;
        current = current->next;
    }
    
    int average_temperature = sum / count;
    
    printf("Result: %d\n", average_temperature);
    
    free(third);
    free(second);
    free(head);
    
    return 0;
}