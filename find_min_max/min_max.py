#User function Template for python3

def getMinMax(a, n):
    max = a[0]
    min = a[0]
    # for temp in a:
    #     if temp > max:
    #         max = temp
    #     if temp < min:
    #         min = temp
    
    for i in range(n):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
            
    return min, max
    # return min(a), max(a)
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends