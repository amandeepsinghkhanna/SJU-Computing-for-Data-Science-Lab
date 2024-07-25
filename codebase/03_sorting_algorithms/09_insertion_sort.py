"""
    Algorithm Number: 09
    Algorithm Name: Insertions Sort
    Script Author: Amandeep Singh Khanna
"""


def insertion_sort(sort_lst: list) -> None:
    """
    Sorts a list of integers in ascending order using the insertion sort
    algorithm. This algorithm makes inplace changes to the list.
    1. sort_lst - list - A list of integers to be sorted.
    """
    for lst_idx in range(len(sort_lst)):
        for sub_lst_idx in range(lst_idx):
            if sort_lst[lst_idx] < sort_lst[sub_lst_idx]:
                temp = sort_lst[sub_lst_idx]
                sort_lst[sub_lst_idx] = sort_lst[lst_idx]
                sort_lst[lst_idx] = temp


def main() -> None:
    pass


if __name__ == "__main__":
    main()
