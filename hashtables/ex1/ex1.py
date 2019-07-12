#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    hash_table_insert(ht, weights[0], 0)
    index = 1

    while index < length:
        weight = weights[index]
        hash_table_insert(ht, weight, index)
        answer = limit - weight
        found_index = hash_table_retrieve(ht, answer)
        if found_index:
            if length <= 2:
                return (index, 0)
            elif found_index > index:
                return (found_index, index)
            else:
                return (index, found_index)
        index += 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
