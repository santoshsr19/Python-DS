def cnt(arr,n,x):
    count = 0
    for i in range(n):
        if arr[i]==x or arr[i]<x:
            count += 1
        
    print(count)






t = int(input())

for _ in range(t):
    n=int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    cnt(arr,n,x)