
def sort012(arr,n):
    return arr.sort()


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends


#repeated problem in geeks for geeks

def nearlysorted (arr, n, k):
    arr.sort()
    for i in arr:
        print(i,end=" ")
    print()
    
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr=[int(x) for x in input().strip().split()]
    nearlysorted (arr, n, k)

"""

Given an array of n elements, where each element is at most k away from its target position. The task is to print array in sorted form.

Input:
First line consists of T test cases. First line of every test case consists of two integers N and K, denoting number of elements in array and at most k positions away from its target position respectively. Second line of every test case consists of elements of array.

Output:
Single line output to print the sorted array.

Constraints:
1<=T<=100
1<=N<=100
1<=K<=N

Example:
Input:
2
3 3
2 1 3
6 3
2 6 3 12 56 8
Output:
1 2 3
2 3 6 8 12 56


"""