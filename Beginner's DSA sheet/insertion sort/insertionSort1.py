#Sort the array using insertion sort

class Solution:
    ##1
    def insert(self, alist, index, n):
        #code here
        currentElement = alist[index]
        pos = index
        
        while pos > 0 and alist[pos-1] > currentElement:
            alist[pos] = alist[pos-1]
            pos -= 1
        
        alist[pos] = currentElement
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(1, n):
            self.insert(alist, i, n)

    ##2
    # def insert(self, alist, index, n):
    #     #code here
    #     currentElement = alist[index]
    #     previousPos = index - 1 
        
    #     while previousPos >= 0 and alist[previousPos] > currentElement:
    #         alist[previousPos+1] = alist[previousPos]
    #         previousPos -= 1
        
    #     alist[previousPos + 1] = currentElement
        
        
    # #Function to sort the list using insertion sort algorithm.    
    # def insertionSort(self, alist, n):
    #     #code here
    #     for i in range(1, n):
    #         self.insert(alist, i, n)

#{ 
 # Driver Code Starts
if __name__=="__main__":
    # t=int(input())
    # for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends