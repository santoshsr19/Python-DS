#User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr,n):
    a=0
    for i in range(n):
        a = int(arr[i])+a
        
    for j in range(n):
        arr[j] = a-int(arr[j])
    for k in range(n):
        print(int(arr[k]), end = ' ')
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    t = int(input())
    
    while(t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr,n)
        print ()
        t -= 1
        
if __name__ == '__main__':
    main()
# } Driver Code Ends