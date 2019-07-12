#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    for ticket in tickets:
        # print('s', ticket.source)
        # print('d', ticket.destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    current_ticket = hash_table_retrieve(hashtable, "NONE")
    # print('ct', current_ticket)
    route[0] = current_ticket

    for i in range(1, length):
        dest = hash_table_retrieve(hashtable, current_ticket)
        route[i] = dest
        current_ticket = dest

    return route
