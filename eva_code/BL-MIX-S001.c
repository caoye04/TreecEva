#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int *data;
    int capacity;
    int size;
    int total_processed;
    int error_count;
} ProcessResult;

ProcessResult *create_result(int initial_capacity)
{
    ProcessResult *result = malloc(sizeof(ProcessResult));
    if (result == NULL)
        return NULL;

    result->data = malloc(initial_capacity * sizeof(int));
    if (result->data == NULL)
    {
        free(result);
        return NULL;
    }

    result->capacity = initial_capacity;
    result->size = 0;
    result->total_processed = 0;
    result->error_count = 0;
    return result;
}

int recursive_transform(int value, int depth)
{
    if (depth <= 0 || value <= 0)
    {
        return value < 0 ? 0 : value;
    }
    return recursive_transform(value * 2 - 1, depth - 1);
}

ProcessResult *process_complex_array(int *input, int input_size)
{
    ProcessResult *result = create_result(input_size * 2);
    if (result == NULL)
        return NULL;

    int batch_size = 3;
    int current_multiplier = 1;

    for (int batch = 0; batch < (input_size + batch_size - 1) / batch_size; batch++)
    {
        int batch_start = batch * batch_size;
        int batch_end = (batch_start + batch_size < input_size) ? batch_start + batch_size : input_size;

        int batch_sum = 0;
        int valid_count = 0;

        for (int i = batch_start; i < batch_end; i++)
        {
            if (input[i] < 0)
            {
                result->error_count++;
                continue;
            }

            int transformed = recursive_transform(input[i], 2);

            if (transformed > 0)
            {
                if (result->size >= result->capacity)
                {
                    int *new_data = realloc(result->data, result->capacity * 2 * sizeof(int));
                    if (new_data == NULL)
                    {
                        result->error_count++;
                        continue;
                    }
                    result->data = new_data;
                    result->capacity *= 2;
                }

                result->data[result->size] = transformed * current_multiplier;
                result->size++;
                batch_sum += transformed;
                valid_count++;
                result->total_processed++;
            }
        }

        if (valid_count > 0)
        {
            int avg = batch_sum / valid_count;
            if (avg % 2 == 0)
            {
                current_multiplier++;
            }

            for (int j = 0; j < result->size; j++)
            {
                if (result->data[j] % avg == 0)
                {
                    result->data[j] += avg;
                    result->total_processed++;
                }
            }
        }

        if (result->error_count > input_size / 2)
        {
            break;
        }
    }

    return result;
}

int main()
{
    int test_data[] = {2, -1, 4, 0, 3, -2, 1};
    ProcessResult *final_result = process_complex_array(test_data, 7);

    if (final_result)
    {
        printf("Final total_processed: %d\n", final_result->total_processed);
        free(final_result->data);
        free(final_result);
    }

    return 0;
}