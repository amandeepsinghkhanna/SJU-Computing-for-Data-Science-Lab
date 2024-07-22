Table of contents

- [Binary Search](#binary-search)
  - [1. Binary Search Algorithm](#binary-search-algorithm)
  - [2. Binary Search Python Code](#) 

# Binary Search

## Binary Search Algorithm
```
Step 1: Start
Step 2: Create an array of numbers. Sort it in ascending order if it's not sorted.
Step 3: Set ele to the variable you are looking for.
Step 4: Now create 2 more variables, start and end. Set start to the first index of the array. Set end to the last index of the array. 
Step 5: Set mid to the middle position ((start + end) / 2).
Step 6: Check if the mid is equal to the ele. If True, Stop.
Step 7: If the previous step fails, check if ele is greater than mid. Then set start to mid position + 1.
Step 8: Else ele is lesser than mid. Then set end to mid - 1.
Step 9: Repeat steps 5 to 7.
Step 10: Stop
```

## Binary Search Python Code
```python
# Creating the input array.
arr = [2, 10, 25, 30, 49, 110, 167]

# Element you are searching for
ele = 167

# Setting the variables
start = 0
end = len(arr) - 1

# Actual searching logic
while start <= end:
    mid = (start + end) // 2
    if ele == arr[mid]:
        print(f"{ele} found at {mid + 1} position")
        break
    elif ele > arr[mid]:
        start = mid + 1
    else:
        end = mid - 1
```