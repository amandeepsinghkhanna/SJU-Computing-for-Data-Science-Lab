# Creating the input array.
arr = [2, 10, 25, 30, 49, 110, 167]

# Element you are searching for
ele = int(input("Enter the number you are looking for:"))

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