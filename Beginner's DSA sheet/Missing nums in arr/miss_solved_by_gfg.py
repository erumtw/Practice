#User function Template for python3


class Solution:
    
    def MissingNumber(self,array,n):
        # code here
        # 1 to (n-1) ต้องอยู่ใน array
        sum_of_n_natural = n * (n+1) // 2
        sum_in_arr = sum(array)
        return sum_of_n_natural - sum_in_arr
        

        
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
Method 1: This method uses the technique of the Summation formula. 

Approach: The length of the array is n-1. So, the sum of all n elements 
        i.e. sum of numbers from 1 to n can be calculated using the formula n*(n+1)/2. 
        Now find the sum of all the elements in the array and subtract it from the sum of the first n natural numbers, 
        it will give us the value of the missing element.

Algorithm: 
1. Calculate the sum of the first n natural numbers as sumtotal= n*(n+1)/2
2. Create a variable sum to store the sum of the array elements.
3. find sum of giving array
4. Print the missing number as SumTotal - sum

in my program 
Sumtotal - > sum_of_n_natural
sum -> sum_in_arr
"""