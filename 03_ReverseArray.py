
# Reverse an Array

arr = [4, 5, 2]
l = len(arr)
m = int(l/2)
j = 1
for i in range(m):
    arr[i], arr[l-j] = arr[l-j], arr[i]
    j+=1
print(arr)


# Optimized Solution

class Solution:
    def reverseArray(self, arr):
        # code here
        left = 0
        right = len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr