def sumit(arr,n):
    a=0
    if len(arr)!=n:
        print("Invalid input")
    else:
        for j in range(n):
            a=a+arr[j]
        return a

n=int(input())
arr=list(map(int, input().split()))
sumit(arr,n)