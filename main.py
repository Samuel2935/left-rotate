arr = [1, 3, 2, 7, 4, 6]
# p determine the number of times an array should be rotated
p = 3

# Displays original array
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i]),

# Rotate the given array by n times toward left
for d in range(0, p):
    # Stores the first element of the array
    first = arr[0]

    for j in range(0, len(arr) - 1):
        # Shift element of array by one
        arr[j] = arr[j + 1]

        # First element of array will be added to the end
    arr[len(arr) - 1] = first

print()

# Displays resulting array after rotation
print("Array after left rotation: ")
for d in range(0, len(arr)):
    print(arr[d])