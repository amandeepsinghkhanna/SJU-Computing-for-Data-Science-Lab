"""
    Algorithm Number: 08
    Algorithm Name: 'Selection Sort'
    Script Author: Amandeep Singh Khanna
"""


# Defining a function to compute the minimum value from a list
def get_minimum_value_and_index(input_lst: list) -> int:
    """
    Computes the minimum value from a list of integers.
    1. input_lst - list - A list of integers to compute the minimum value.
    Returns:
    1. minimum_value - int - The smallest integer value in the input_lst.
    2. minimum_value_idx - int - The index of the minimum_value in the input_lst.
    """
    minimum_value = input_lst[0]
    minimum_value_idx = 0
    for lst_idx in range(1, len(input_lst)):
        if input_lst[lst_idx] < minimum_value:
            minimum_value = input_lst[lst_idx]
            minimum_value_idx = lst_idx
    return minimum_value, minimum_value_idx


# Defining the function for selection sort
def selection_sort(sort_lst: list) -> None:
    """
    Implements the selection sort for sorting the list sort_lst in ascending order.
    This algorithm makes inplace changes to the list.
    1. sort_lst - list - A list of integers to be sorted in ascending order.
    """
    for lst_idx in sort_list:
        minimum_value, minimum_value_idx = get_minimum_value_and_index(
            input_lst=sort_lst
        )
        if minimum_value_idx != lst_idx:
            # Swapping the minimum value with the value at the i-th index.
            sort_lst[minimum_value_idx] = sort_lst[lst_idx]
            sort_lst[lst_idx] = minimum_value


def main():
    """
    The main function of the program.
    """
    return None


if __name__ == "__main__":
    main()
