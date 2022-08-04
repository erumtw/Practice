    #  https://practice.geeksforgeeks.org/problems/anagram-1587115620/1?page=1&curated[]=8&sortBy=submissions
"""
    Given two strings a and b consisting of lowercase characters. 
    The task is to check whether two given strings are an anagram of each other or not. 
    An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
    For example, act and tac are an anagram of each other.
    
    Example 1:

    Input:a = geeksforgeeks, b = forgeeksgeeks
    Output: YES
    Explanation: Both the string have samecharacters with
            same frequency. So, both are anagrams.
            
            
    Example 2:
    
    Input:a = allergy, b = allergic
    Output: NO
    Explanation:Characters in both the strings are 
        not same, so they are not anagrams.
"""
    
#User function Template for python3

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        #code here
        aa = list(a)
        aa.sort()
        bb = list(b)
        bb.sort()
        return aa == bb
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    # t = int(input())
    # for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
    
# } Driver Code Ends