# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1?page=1&curated[]=8&sortBy=submissions
"""
Bitonic Point
    Given an array arr of n elements which is first increasing and then may be decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the maximum value.

Example 1:
Input: 
n = 9
arr[] = {1,15,25,45,42,21,17,12,11}
Output: 45
Explanation: Maximum element is 45.

"""

#User function Template for python3
class Solution:
    def findMaxTil(self, arr, left, right):
        if left > right:
            return -1
        if left == right: # 1 element left case
            return arr[right]
        if left+1 == right and arr[left] >= arr[right]: # 2 elements left case
            return arr[left] 
        if left+1 == right and arr[left] <= arr[right]: # 2 elements left case
            return arr[right] 
        
        mid = (left+right) // 2
        
        if arr[mid-1] <= arr[mid] >= arr[mid+1]:
            return arr[mid]
        elif arr[mid-1] <= arr[mid] <= arr[mid+1]:
            return self.findMaxTil(arr, mid+1, right)
        else:
            return self.findMaxTil(arr, 0, mid-1)
        
    def findMaximum(self,arr, n):
        # code here
        return self.findMaxTil(arr, 0, n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    # tc = int(input())
    # while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        # tc -= 1

# } Driver Code Ends