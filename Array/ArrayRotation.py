a=int(input())

for i in range(a):
    n,d=input().split()
    x=int(d)
    arr=list(map(int,input().split()))
    print(*(arr[x:] + arr[:x]))
    t=-1
    5