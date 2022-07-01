#User function template for Python

"""
    Binary Search 
    Given a sorted array of size N and an integer K, find the position at which K is present in the array using binary search.
"""

class Solution:    
    def binarysearch(self, arr, n, k):
        low = 0
        high = n - 1
        mid = (low + high) // 2 
        if arr[mid] == k:
            return mid
        else :
            while arr[mid] != k:
                if low > high:
                    return -1
                elif k < arr[mid]:
                    high = mid - 1
                    mid = (low + high) // 2
                else:
                    low = mid + 1
                    mid = (low + high) // 2
            return mid

    def binarysearch_better(self, arr, n, k):
        return self.bin_search(arr, 0, n-1, k)

    def bin_search(self, arr, low, high, k):
        mid = (low + high) // 2
        if low > high:
            return -1
        else:
            if arr[mid] == k:
                return mid
            elif k < arr[mid]:
                return self.bin_search(arr, low, mid-1, k)
            else:
                return self.bin_search(arr, mid+1, high, k)
#{ 
#  Driver Code Starts
#Initial template for Python1

if __name__ == '__main__':
    # t = int(input())
    # for i in range(t):
        n = int(input("N(number of list): "))
        arr = list(map(int, input("List: ").strip().split(' ')))
        k = int(input("K(find): "))
        ob = Solution()
        # print(ob.binarysearch(arr, n, k))
        if ob.binarysearch_better != -1:
            print(f"{k} is in list: index = {ob.binarysearch_better(arr, n, k)}")
        else:
            print(f"{k} is not in list")



# } Driver Code Ends