
# Move all Zeros to End

arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(arr)
for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)
print(arr)



# Optimizes Solution


class Solution:
    def pushZerosToEnd(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[count] = arr[count], arr[i]
                count += 1
        return arr