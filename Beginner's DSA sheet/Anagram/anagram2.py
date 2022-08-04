## solution by gfg ##

# User function Template for python3

#Back-end complete function Template for Python 3

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        
        #an array of size 26, to store count of characters.
        mp = {}
        
        #storing count of each character in first string.
        for i in a:
            if i in mp.keys ():
                mp[i] += 1
            else:
                mp[i] = 1
        
        #decrementing the count of characters encountered in the second string.
        for i in b:
            if i not in mp.keys ():
                return False
            else:
                mp[i] -= 1
        
        #iterating over the array in which we stored the count initially 
        #to check if count at every index is equal to 0 or not.
        #count 0 indicates that number of characters in both strings are same.
        for i in mp.keys ():
            if mp[i] != 0:
                return False
        
        #returning the result.       
        return True
        


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