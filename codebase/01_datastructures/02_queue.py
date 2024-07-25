"""
    Algorithm Number: 02
    Algorithm Name: 'queue'
    Script Author: Amandeep Singh Khanna
"""


class Queue(object):
    """
        Implementation of a queue in python.
    """
    queue_data = [] # Empty list to store the data for the queue.

    def push(self, value:object)->None:
        """
            Pushes/adds a value to end of the queue.
            1. value - object - A value of any datatype that needs to be stored
            in the queue.
        """
        self.queue_data.append(value)
    
    def pop(self)->None:
        """
            Pops/removes a value from the end of the queue.
        """
        self.queue_data.pop(0)

    def display_queue(self)->None:
        """
            Displays the elements present in the queue by printing each element.
        """
        for value in self.queue_data:
            print(value)


def main():
    """
        The main function of the program.
    """
    queue_obj = Queue() # Creating the queue object.
    queue_obj.display_queue() # Seeing the contents of the queue.
    # Adding values to the queue:
    queue_obj.push(10)
    queue_obj.push(1)
    queue_obj.push(34)
    queue_obj.push(56)
    queue_obj.display_queue() # Seeing the contents of the queue.
    queue_obj.pop() # Poping a value from the queue.
    queue_obj.pop() # Poping a value from the queue.
    return None


if __name__ == "__main__":
    main()
