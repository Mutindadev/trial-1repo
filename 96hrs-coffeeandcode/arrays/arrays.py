# In Python, arrays are represented by lists
# index: 0  1   2   3   4
# array: [10, 20, 30, 40, 50]

# Define a list
arr = [10, 20, 30, 40, 50]

# Access an element
print(f"Element at index 2: {arr[2]}")

# Update an element
arr[2] = 55
print(f"Array after updating element at index 2: {arr}")

# Insert at the end
arr.append(60)
print(f"Array after appending 60: {arr}")

# Insert at a specific position
arr.insert(2, 25)
print(f"Array after inserting 25 at index 2: {arr}")

# Delete an element
arr.pop(3)
print(f"Array after popping element at index 3: {arr}")

# Search for a value
if 10 in arr:
    print("Found 10 in the array")
else:
    print("Did not find 10 in the array")

print(f"Final array: {arr}")