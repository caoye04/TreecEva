#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_TABLE_SIZE 16

// Structure for hash table entries
typedef struct Entry {
    int key;
    float amplitude;
    struct Entry* next;
} Entry;

// Hash table
Entry* hash_table[HASH_TABLE_SIZE];

// Function pointer type for filter operations
typedef float (*FilterFunc)(float);

// Bitmask for filtering
struct FilterConfig {
    unsigned int mask : 8;
    unsigned int reserved : 24;
};

// Filter function using bitwise operations
float apply_bitmask_filter(float amp) {
    union { float f; unsigned int i; } converter;
    converter.f = amp;
    struct FilterConfig config = {0xF0, 0};
    converter.i &= (config.mask << 24); // Apply mask to high bits
    return converter.f;
}

// Hash function
int hash(int key) {
    return key % HASH_TABLE_SIZE;
}

// Insert into hash table
void insert(int key, float amplitude) {
    int index = hash(key);
    Entry* entry = (Entry*)malloc(sizeof(Entry));
    entry->key = key;
    entry->amplitude = amplitude;
    entry->next = hash_table[index];
    hash_table[index] = entry;
}

// Comparator for sorting entries by key
int compare_entries(const void* a, const void* b) {
    Entry* entry_a = *(Entry**)a;
    Entry* entry_b = *(Entry**)b;
    return (entry_a->key > entry_b->key) - (entry_a->key < entry_b->key);
}

int main() {
    // Initialize hash table
    memset(hash_table, 0, sizeof(hash_table));
    
    // Populate hash table with frequency bin data
    insert(3, 12.5f);
    insert(7, 8.2f);
    insert(11, 15.7f);
    insert(15, 6.3f);
    insert(2, 9.1f);
    
    // Collect all entries for sorting
    Entry* entries[32];
    int count = 0;
    for (int i = 0; i < HASH_TABLE_SIZE; i++) {
        for (Entry* e = hash_table[i]; e != NULL; e = e->next) {
            entries[count++] = e;
        }
    }
    
    // Sort entries by key
    qsort(entries, count, sizeof(Entry*), compare_entries);
    
    // Apply filter function through function pointer
    FilterFunc filter = apply_bitmask_filter;
    float filtered_sum = 0.0f;
    for (int i = 0; i < count; i++) {
        entries[i]->amplitude = filter(entries[i]->amplitude);
        // Only sum positive amplitudes after filtering
        if (!(entries[i]->amplitude <= 0.0f)) { // Logical NOT operation
            filtered_sum += entries[i]->amplitude;
        }
    }
    
    printf("Result: %.2f\n", filtered_sum);
    
    // Cleanup
    for (int i = 0; i < HASH_TABLE_SIZE; i++) {
        Entry* e = hash_table[i];
        while (e != NULL) {
            Entry* temp = e;
            e = e->next;
            free(temp);
        }
    }
    
    return 0;
}