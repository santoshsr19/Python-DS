t=int(input())
for _ in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    count=0
    a=1
    for i in range(n):
        for j in range(a,n):
            if arr[i]==arr[j]:
                count+=1
        a+=1
    print(count)