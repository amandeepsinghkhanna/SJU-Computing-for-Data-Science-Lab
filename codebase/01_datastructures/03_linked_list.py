"""
    Algorithm No: 3
    Algorithm Name: 'Linked List'
    Script Author: Amandeep Singh Khanna
"""


# %%
class Node:
    """
    Defining a custom object for capturing data and the next node.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None


class LinkedList:
    """
    Implementing a Linked List in Python.
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_element_at_start(self, data) -> None:
        """
        Adds an element at the begining of the linked list.
        """
        if self.head == None:
            self.head = Node(data)
            self.size += 1
        else:
            first_node = self.head.next_node
            self.head = Node(data)
            self.head.next_node = first_node
            self.size += 1

    def insert_element_at_end(self, data) -> None:
        """ """
        if self.head == None:  # If the linked list is empty.
            self.head = Node(data)
            self.size += 1
        else:  # If the linked list has at least one value.
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = Node(data)
            self.size += 1

    def insert_element_at_position(self, data: object, position: int) -> None:
        """ """
        pass

    def print_linkedlist(self):
        """ """
        if self.head == None:  # If the linked list is empty.
            print("The linked list is empty!")
        else:  # If the linked list has at least one value.
            current_node = self.head
            linkedlist_str = ""  # To generate the linked list visualization.
            while current_node != None:
                linkedlist_str += f"{current_node.data}->"
                current_node = current_node.next_node
            print(f"{linkedlist_str}NULL")


def main():
    """
    The main program.
    """
    linked_list = LinkedList()  # Initializing the linked list.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.insert_element_at_end(10)  # Inserting element at the end.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.print_linkedlist()  # Printing the linked list.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.insert_element_at_end(1)  # Inserting element at the end.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.print_linkedlist()  # Printing the linked list.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.insert_element_at_end(11)  # Inserting element at the end.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.print_linkedlist()  # Printing the linked list.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.insert_element_at_end(13)  # Inserting element at the end.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.print_linkedlist()  # Printing the linked list.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.insert_element_at_start(0)  # Inserting element at the start.
    print(f"The size of the linked list {linked_list.size}")
    linked_list.print_linkedlist()  # Printing the linked list.


if __name__ == "__main__":
    main()

# %%
