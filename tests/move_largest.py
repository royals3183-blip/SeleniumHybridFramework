arr = [3, 5, 1, 0, 2, 4]

# Step 1: Find max manually
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

# Step 2: Remove & append
new_arr = []
for num in arr:
    if num != largest:
        new_arr.append(num)

new_arr.append(largest)

print(new_arr)
