"""
    Algorithm Number: 01
    Algorithm Name: 'Stack'
    Script Author: Amandeep Singh Khanna
"""


class Stack(object):
    """
    Implementation of a stack in python.
    """

    stack_data = []  # Empty list to store the data for the stack.

    def push(self, value: object) -> None:
        """
        Pushes/adds a value to end of the stack.
        1. value - object - A value of any datatype that needs to be stored
        in the stack.
        """
        self.stack_data.append(value)

    def pop(self) -> None:
        """
        Pops/removes a value from the begining of the stack.
        """
        self.stack_data.pop()

    def size(self):
        """
        Returns the number of elements present in the stack.
        """
        return len(self.stack_data)

    def is_empty(self):
        """
        Checks for the items inside the stack and returns,
        TRUE -> if stack is empty
        FALSE -> if stack is non_empty
        """
        return len(self.stack_data) == 0
    
    def display_stack(self) -> None:
        """
        Displays the elements present in the stack by printing each element.
        """
        for value in self.stack_data:
            print(value)


def main():
    """
    The main function of the program.
    """
    stack_obj = Stack()  # Creating the stack object.
    stack_obj.display_stack()  # Seeing the contents of the stack.
    # Adding values to the stack:
    stack_obj.push(10)
    stack_obj.push(1)
    stack_obj.push(34)
    stack_obj.push(56)
    stack_obj.display_stack()  # Seeing the contents of the stack.
    stack_obj.pop()  # Poping a value from the stack.
    print("After popping the element")
    print("Size of the stack:",stack_obj.size()) # Gives the size of the stack.
    print("Is the stack empty?:",stack_obj.is_empty()) # Checking for contents in the stack. 
    return None


if __name__ == "__main__":
    main()
