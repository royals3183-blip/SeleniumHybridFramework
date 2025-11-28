arr = [3, 5, 6, 0,1, 2, 4]

min_ = arr[0]

for num in arr:
    if num <= min_:
        min_ = num

new_arr =[]

for num in arr:
    if num != min_:
        new_arr.append(num)

new_arr.append(min_)
print(new_arr)

n = len(new_arr)

for i in range(n):
    for j in range(n - 1):
        if new_arr[j] > new_arr[j + 1]:      # If left > right → swap
            temp = new_arr[j]
            new_arr[j] = new_arr[j + 1]
            new_arr[j + 1] = temp

print("Sorted new_arr:", new_arr)