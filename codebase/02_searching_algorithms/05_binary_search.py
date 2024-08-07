"""
    Algorithm Number: 05
    Algorithm Name: Binary Search
    Script Author: Syed Hammad
"""

from typing import List


def binary_search(ele: int, arr: List[int]) -> int:
    """
    Perform binary search on a sorted list to find the target value.
        1. Check the middle item.
        2. If it matches the target, return its index.
        3. If the target is smaller, repeat with the left half.
        4. If the target is larger, repeat with the right half.
        5. Continue until the target is found or the list is exhausted.
    Parameters:
    ----------
    ele: int
        Element to search for
    arr: List[int]
        Array to search in
    Returns:
    ----------
    int: Index of the element if found, -1 otherwise
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
