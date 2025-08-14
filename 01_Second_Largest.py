# Second Largest Element in array

class Solution:
    def getSecondLargest(self, arr):
        s = sorted(set(arr))
        l = len(s)
        last = s[len(s)-1]
        for i in range(len(s)):
            if s[l-1] > s[l-2]:
                return s[l-2]
            else:
                return -1
            


# Optimized Solution

class Solution:
    def secondLargest(self, arr):
        n = len(arr)
        first = second = float('-inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        if second == float('-inf'):
            return -1
        else:
            return second
        
ans = Solution()
res = ans.secondLargest([12, 35, 1, 10, 34, 1])
print("Second Largest Element of Array is: ", res)