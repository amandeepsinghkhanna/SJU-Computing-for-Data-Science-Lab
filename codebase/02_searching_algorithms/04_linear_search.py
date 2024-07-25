"""
    Algorithm Number: 04
    Algorithm Name: 'Linear Search'
    Script Author: Amandeep Singh Khanna
"""


# Defining the function for linear search:
def linear_search(search_element: int, search_lst: list) -> str:
    """
    Searches the value stored in the variable search_element,
    in the list provided as search_lst.
    1. search_element - int - Element to be searched.
    2. search_lst - list - List with the elements to be
    searched for.
    """
    # Going through the value stored at each index in the search_lst.
    for lst_idx in range(len(search_lst)):
        # Checking if the element at the current index is the value to
        # be searched for.
        if search_element == search_lst[lst_idx]:
            # If element found at current index.
            return f"Element {search_element} found at list index {lst_idx}"
        else:
            # If element not found at the current index.
            continue
    # If the element is not in search_lst.
    return "Element not in the list"


def main() -> None:
    """
    The main function of the program.
    """
    # Defining the list to be searched
    search_lst = [10, 20, 2, 1, 33, 4]
    search_element = 2  # Element to be searched for

    # Searching for element 2 in the above specified list
    print(linear_search(search_element=search_element, search_lst=search_lst))


if __name__ == "__main__":
    main()
