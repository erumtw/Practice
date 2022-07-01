#Back-end complete function template for Python by GeeksforGeeks practice

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
	    i = 0
	    while i < N:
	        # If (ith index +k) is less than total number of elements it means
            # k elements exist from current index so we reverse k elements 
            # starting from current index.
	        if (i+K<N):
	            # reversed function used to reverse any part of the array.
	            arr[i:i+K] = reversed(arr[i:i+K])
	            # updating index from i to i+k.
	            i += K
	        # Else k elements from current index doesn't exist. 
            # In that case we just reverse the remaining elements.
	        else:
	            # reversed function used to reverse any part of the array.
	            arr[i:] = reversed(arr[i:])
	            # updating index from i to i+k.
	            i += K
             
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