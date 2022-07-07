#User function Template for python3

class Solution:
    def MissingNumber(self,array,n):
        # code here
        # 1 to (n-1) ต้องอยู่ใน array
        for i in range (1, n+1):
            if i not in array:
                return i
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends

""" 
Test Cases Passed: 
108 / 307

Time Limit Exceeded

Your program took more time than expected.Time Limit Exceeded
Expected Time Limit 1.61sec
Hint : Please optimize your code and submit again.
"""