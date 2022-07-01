"""
    Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

    ##########################################################################################
    Example 1:
    Input:
    N = 5, K = 3
    arr[] = {1,2,3,4,5}
    Output: 3 2 1 5 4
    Explanation: First group consists of elements 1, 2, 3. 
    Second group consists of 4,5.

    Example 2:
    Input:
    N = 4, K = 3
    arr[] = {5,6,8,9}
    Output: 8 6 5 9
    ##########################################################################################

    Your Task: 
    You don't need to read input or print anything. 
    The task is to complete the function reverseInGroups() which takes the array, N and K as input parameters and modifies the array in-place. 
"""

#User function template for Python

#{ 
#  Driver Code Starts
#  Initial template for Python
#  User function template for Python

class Solution:    
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        # code here
        g = math.ceil(N/K)
        reversedd = []
        if K > N:
            reversedd = arr[::-1]
        else:
            start = 0
            end = K
            for i in range(1, g+1):
                reversedd += arr[start:end:][::-1]
                if end - start == K:
                    start = end
                    end += K 
                else:
                    start = end
                    end = N
                    
        for i in range(len(reversedd)):
            arr[i] = reversedd[i]
        # return reversed 

#{ 
#  Driver Code Starts
#  Initial template for Python

import math
def main():
    # T=int(input())
    # while(T>0):
        nk = [int(x) for x in input().strip().split()]
        N = nk[0]
        K = nk[1]
        arr = [int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i, end=" ")
        print()
        # T-=1

if __name__=="__main__":
    main()

# } Driver Code Ends 