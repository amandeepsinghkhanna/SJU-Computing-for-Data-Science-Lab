"""
    Algorithm Number: 05
    Algorithm Name: Binary Search
    Script Author: Syed Hammad
"""

from typing import List


def binary_search(ele: int, arr: List[int]) -> int:
    """
    Binary Search Algorithm
    :param ele: Element to search for
    :param arr: Array to search in
    :return: Index of the element if found, -1 otherwise
    """
    # Setting the variables
    start: int = 0
    end: int = len(arr) - 1
    mid: int

    # Actual searching logic
    while start <= end:
        mid = (start + end) // 2
        if ele == arr[mid]:
            return mid + 1
            break
        elif ele > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        return -1


def main() -> None:
    """
    Main function
    """
    # Creating the input array.
    arr: List[int] = [2, 10, 25, 30, 49, 110, 167]

    # Element you are searching for
    ele: int = int(input("Enter the number you are looking for:"))

    pos: int = binary_search(ele, arr)
    if pos == -1:
        print(f"{ele} not found")
    else:
        print(f"{ele} found at {pos} position")


if __name__ == "__main__":
    main()
