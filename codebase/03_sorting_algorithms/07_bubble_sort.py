"""
    Algorithm Number: 07
    Algorithm Name: 'Selection Sort'
    Script Author: Amandeep Singh Khanna
"""


def bubble_sort(sort_lst: list) -> None:
    """
    Implement the bubble sort to sort a list of integers in ascending order.
    This algorithm makes changes inplace changes in the list.
    1. sort_lst - int - A list of integers to be sorted.
    """
    for pass_id in range(len(sort_lst) - 1):
        for lst_idx in range(len(sort_lst) - pass_id - 1):
            # print(f"List status: {sort_lst} at pass: {pass_id}, iteration: {lst_idx}")
            if sort_lst[lst_idx] > sort_lst[lst_idx + 1]:
                temp = sort_lst[lst_idx]
                sort_lst[lst_idx] = sort_lst[lst_idx + 1]
                sort_lst[lst_idx + 1] = temp


def main() -> None:
    """
    The main function of the program.
    """
    pass


if __name__ == "__main__":
    main()
