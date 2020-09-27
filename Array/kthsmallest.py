def kthsmallest(arr, n, x):
    arr.sort()
    s=arr[x-1]
    print(s)



t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x=int(input())
    kthsmallest(arr, n, x)


"""
Example:
Input:
2
6
7 10 4 3 20 15
3
5
7 10 4 20 15
4
Output:
7
15
"""