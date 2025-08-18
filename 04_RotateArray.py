# Optimizes Solution

def rotateArr(arr, d):
    n = len(arr)
    d %= n

    reverse(arr, 0, d-1)

    reverse(arr, d, n-1)

    reverse(arr, 0, n-1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5]
d = 2
rotateArr(arr, d)
print(arr)

# Another Optimized Solution
import math
class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n 
        cycles = math.gcd(n, d)

        for i in range(cycles):
            startEle = arr[i]
            currIdx = i

            while True:
                nextIdx = (currIdx + d) % n

                if nextIdx == i:
                    break

                arr[currIdx] = arr[nextIdx]
                currIdx = nextIdx

            arr[currIdx] = startEle

arr = [1, 2, 3, 4, 5]
d = 2
ob = Solution()
ob.rotateArr(arr, d)
print(arr)
