"""
    Algorithm No: 3
    Algorithm Name: 'Linked List'
    Script Author: Amandeep Singh Khanna
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f"{self.data}->{self.next_node}"

    def __str__(self):
        return f"{self.data}->{self.next_node}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.linked_list_size = 0

    def insert(self, data, position="end"):
        new_node = Node(data)  # Create the new node outside the loop

        if position == "end":  # Insert at the end
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next_node is not None:
                    current_node = current_node.next_node
                current_node.next_node = new_node
            self.linked_list_size += 1

        elif position == "start":  # Insert at the beginning
            new_node.next_node = self.head
            self.head = new_node
            self.linked_list_size += 1

        else:  # Insert after a specific value (assuming unique values)
            found = False
            current_node = self.head
            while current_node is not None and not found:
                if current_node.data == position:
                    found = True
                else:
                    current_node = current_node.next_node

            if found:  # Insert after the found node
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                self.linked_list_size += 1
            else:  # Value not found, do nothing (or raise an error)
                print(f"Value {position} not found in the list")

    def delete(self, position="end"):
        if self.head is None:
            print("The linked list is empty")
            return

        if position == "end":
            if self.head.next_node is None:
                self.head = None
            else:
                current_node = self.head
                while current_node.next_node.next_node is not None:
                    current_node = current_node.next_node
                current_node.next_node = None
            self.linked_list_size -= 1

        elif position == "start":
            self.head = self.head.next_node
            self.linked_list_size -= 1

        else:
            found = False
            current_node = self.head
            prev_node = None
            while current_node is not None and not found:
                if current_node.data == position:
                    found = True
                else:
                    prev_node = current_node
                    current_node = current_node.next_node

            if found:
                if prev_node is None:
                    self.head = current_node.next_node
                else:
                    prev_node.next_node = current_node.next_node
                self.linked_list_size -= 1
            else:
                print(f"Value {position} not found in the list")


def main():
    linked_list = LinkedList()
    linked_list.insert(2)
    linked_list.insert(3)
    print(linked_list.head)
    linked_list.insert(data=1, position="start")
    linked_list.insert(data=0, position="start")
    linked_list.insert(data=6, position="end")
    print(linked_list.head)
    linked_list.insert(data=4, position=3)
    linked_list.insert(data=5, position=4)
    linked_list.insert(data=5, position=10)
    linked_list.insert(data=50, position="end")
    print(linked_list.head)
    linked_list.delete()
    print(linked_list.head)
    linked_list.delete(position="start")
    print(linked_list.head)
    linked_list.delete(position=5)
    print(linked_list.head)


if __name__ == "__main__":
    main()
