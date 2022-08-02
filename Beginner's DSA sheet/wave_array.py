# # https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1?page=1&curated[]=8&sortBy=submissions
# """
# Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
# In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....

# If there are multiple solutions, find the lexicographically smallest one.

# ## ex.1

# Input:
# n = 5
# arr[] = {1,2,3,4,5}
# Output: 2 1 4 3 5
# Explanation: Array elements after 
# sorting it in wave form are 
# 2 1 4 3 5.

# ## ex.2

# Input:
# n = 6
# arr[] = {2,4,7,8,9,10}
# Output: 4 2 8 7 10 9
# Explanation: Array elements after 
# sorting it in wave form are 
# 4 2 8 7 10 9.

# """


from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for i in range(0, n, 2):
            # if i < n-1:
            if i < n-1 and a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
            # if i > 0:
            if i > 0 and a[i] < a[i-1]:
                a[i], a[i-1] = a[i-1], a[i]


# #{ 
#  # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    # t = int(input())
    # for _ in range(t):
        
        n = int(input())
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# # } Driver Code Ends