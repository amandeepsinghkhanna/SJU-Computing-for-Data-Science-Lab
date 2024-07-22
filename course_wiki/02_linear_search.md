Table of contents
- [Linear Search](#linear-search)
  - [1. Code for the algorithm](#1-code-for-the-algorithm)

# Linear Search

## 1. Code for the algorithm

```python
# Defining the function for linear search:
def linear_search(search_element: int,search_lst:list)->str:
    for lst_idx in range(len(search_lst)):
        if search_element == search_lst[lst_idx]:
            return f"Element {search_element} found at list index {lst_idx}"
        else:
            continue
    return "Element not in the list"

# Defining the list to be searched
search_lst = [10, 20, 2, 1, 33, 4]
search_element = 2 # Element to be searched for

# Searching for element 2 in the above specified list
print(
    linear_search(
        search_element=search_element, 
        search_lst=search_lst
    )
)
```
