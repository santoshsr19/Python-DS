def minsubset(arr,n):
    count = 1
    arr.sort()
    for i in range(0,n-1):
        if arr[i]+1!=arr[i+1]:
            count = count+1
    
    print(count)
        


t=int(input())

for _ in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    minsubset(arr,n)


"""
Test Case 1 -
{5, 6, 7}, { 56, 57, 58}, {100, 101, 102, 103} are 3 subset in which numbers are consecutive.

Test Case 2 -
{10}, {100} and {105} are 3 subset in which numbers are consecutive.
 """